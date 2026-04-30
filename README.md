# RAL Control Packs

<p align="center">
  <img src="https://img.shields.io/badge/Platform-Android-green?style=flat-square" alt="Platform">
  <img src="https://img.shields.io/badge/Version-1.0.0-blue?style=flat-square" alt="Version">
  <img src="https://img.shields.io/badge/License-MIT-yellow?style=flat-square" alt="License">
</p>

RotatingArt Launcher 官方控件包仓库，提供预设的虚拟控件布局配置。

## 📦 可用控件包

| 控件包 | 描述 | 模式 |
|--------|------|------|
| **键盘+鼠标模式** | WASD移动 + 触控板瞄准 + 鼠标按键操作 | 键盘/鼠标 |
| **手柄模式** | Xbox 手柄布局：双摇杆 + ABXY + 方向键 + 肩键 | Gamepad |



## 📥 如何使用

1. 打开 **RotatingArt Launcher**
2. 进入 **控件布局** 页面
3. 点击 **控件商店** 按钮
4. 选择需要的控件包进行下载
5. 下载完成后点击 **应用** 即可使用

## 🔧 仓库结构

```
RAL-ControlPacks/
├── README.md                          # 说明文档
├── repository.json                    # 仓库索引
└── packs/
    ├── keyboard-terraria/
    │   └── keyboard-terraria.ralpack  # 键盘+鼠标模式
    └── gamepad-terraria/
        └── gamepad-terraria.ralpack   # 手柄模式
```

## 📋 控件包格式

### repository.json
仓库索引文件，包含所有可用控件包的元数据。

### .ralpack 文件
ZIP 格式的控件包，包含：
- `manifest.json` - 控件包元数据
- `layout.json` - 控件布局配置

## 🤝 贡献

欢迎提交 Pull Request 贡献新的控件布局！

### 创建新控件包

1. 在 RotatingArt Launcher 中创建并编辑控件布局
2. 导出布局为 JSON 文件
3. 创建 `manifest.json` 描述文件
4. 打包为 `.ralpack` 文件
5. 更新 `repository.json` 索引
6. 提交 PR

## 📄 License

MIT License

---

<p align="center">
  Made with ❤️ by <a href="https://github.com/RotatingArtDev">RotatingArtDev</a>
</p>

