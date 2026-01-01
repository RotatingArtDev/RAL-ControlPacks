#!/bin/bash
echo ""
echo "========================================"
echo "  RAL 控件包仓库 - 自动更新脚本"
echo "========================================"
echo ""

cd "$(dirname "$0")"

echo "[1/3] 生成 repository.json..."
python3 generate_repository.py
if [ $? -ne 0 ]; then
    echo "错误: 生成失败！"
    exit 1
fi

echo ""
echo "[2/3] 添加到 Git..."
git add .

echo ""
echo "[3/3] 提交并推送..."
git commit -m "🔄 更新控件包仓库"
git push

echo ""
echo "========================================"
echo "  完成！"
echo "========================================"

