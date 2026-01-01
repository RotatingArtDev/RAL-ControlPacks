#!/usr/bin/env python3
"""
自动生成 repository.json
扫描 packs/ 目录，读取每个包的 manifest.json，自动生成仓库索引
"""

import os
import sys
import json
from datetime import datetime
from pathlib import Path

# 修复 Windows 控制台编码问题
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

# 仓库配置
REPO_CONFIG = {
    "version": 1,
    "name": "RAL Official Control Packs",
    "description": "RotatingArt Launcher 官方控件包仓库",
    "author": "RotatingArtDev",
    "website": "https://github.com/RotatingArtDev/RAL-ControlPacks",
    "categories": [
        {
            "id": "keyboard",
            "name": "键盘+鼠标",
            "icon": "keyboard",
            "order": 1
        },
        {
            "id": "gamepad",
            "name": "手柄",
            "icon": "sports_esports",
            "order": 2
        }
    ]
}

def get_directory_size(path):
    """计算目录总大小"""
    total = 0
    for entry in os.scandir(path):
        if entry.is_file():
            total += entry.stat().st_size
        elif entry.is_dir():
            total += get_directory_size(entry.path)
    return total

def find_preview_images(pack_dir):
    """查找预览图"""
    previews = []
    for ext in ['*.png', '*.jpg', '*.jpeg', '*.webp']:
        for f in Path(pack_dir).glob(ext):
            if f.name.startswith('preview') or f.name.startswith('screenshot'):
                previews.append(f.name)
    
    # 如果没找到 preview 开头的，查找任意图片
    if not previews:
        for ext in ['.png', '.jpg', '.jpeg', '.webp']:
            for f in Path(pack_dir).iterdir():
                if f.suffix.lower() == ext and f.name not in ['icon.png']:
                    previews.append(f.name)
                    break
    
    return previews

def find_asset_files(pack_dir):
    """查找 assets 目录下的所有文件"""
    assets = []
    assets_dir = os.path.join(pack_dir, 'assets')
    
    if not os.path.exists(assets_dir):
        return assets
    
    for root, dirs, files in os.walk(assets_dir):
        for file in files:
            # 获取相对于 assets 目录的路径
            full_path = os.path.join(root, file)
            rel_path = os.path.relpath(full_path, assets_dir)
            # 统一使用正斜杠
            rel_path = rel_path.replace('\\', '/')
            assets.append(rel_path)
    
    return assets

def scan_packs(packs_dir):
    """扫描所有控件包"""
    packs = []
    
    for pack_name in os.listdir(packs_dir):
        pack_path = os.path.join(packs_dir, pack_name)
        
        if not os.path.isdir(pack_path):
            continue
        
        manifest_path = os.path.join(pack_path, 'manifest.json')
        
        if not os.path.exists(manifest_path):
            print(f"⚠️  跳过 {pack_name}: 缺少 manifest.json")
            continue
        
        try:
            with open(manifest_path, 'r', encoding='utf-8') as f:
                manifest = json.load(f)
            
            # 计算文件大小
            file_size = get_directory_size(pack_path)
            
            # 查找预览图
            preview_images = find_preview_images(pack_path)
            if not preview_images and manifest.get('previewImagePaths'):
                preview_images = manifest['previewImagePaths']
            
            # 查找 assets 文件
            asset_files = find_asset_files(pack_path)
            
            # 构建包信息
            pack_info = {
                "id": manifest.get('id', pack_name),
                "name": manifest.get('name', pack_name),
                "author": manifest.get('author', ''),
                "version": manifest.get('version', '1.0.0'),
                "versionCode": manifest.get('versionCode', 1),
                "description": manifest.get('description', ''),
                "category": manifest.get('category', 'keyboard'),
                "tags": manifest.get('tags', []),
                "iconPath": manifest.get('iconPath', ''),
                "previewImagePaths": preview_images,
                "assetFiles": asset_files,  # 添加 assets 文件列表
                "downloadUrl": manifest.get('downloadUrl', ''),
                "fileSize": file_size
            }
            
            packs.append(pack_info)
            print(f"✅ 添加 {pack_info['name']} ({pack_info['id']})")
            
        except json.JSONDecodeError as e:
            print(f"❌ 解析失败 {pack_name}: {e}")
        except Exception as e:
            print(f"❌ 错误 {pack_name}: {e}")
    
    return packs

def generate_repository(packs_dir, output_file):
    """生成 repository.json"""
    print(f"\n📦 扫描控件包目录: {packs_dir}\n")
    
    packs = scan_packs(packs_dir)
    
    # 按名称排序
    packs.sort(key=lambda x: x['name'])
    
    # 构建仓库数据
    repository = REPO_CONFIG.copy()
    repository['lastUpdated'] = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')
    repository['packs'] = packs
    
    # 写入文件
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(repository, f, ensure_ascii=False, indent=4)
    
    print(f"\n✨ 已生成 {output_file}")
    print(f"   共 {len(packs)} 个控件包")

def main():
    # 获取脚本所在目录
    script_dir = os.path.dirname(os.path.abspath(__file__))
    packs_dir = os.path.join(script_dir, 'packs')
    output_file = os.path.join(script_dir, 'repository.json')
    
    if not os.path.exists(packs_dir):
        print(f"❌ packs 目录不存在: {packs_dir}")
        return
    
    generate_repository(packs_dir, output_file)

if __name__ == '__main__':
    main()

