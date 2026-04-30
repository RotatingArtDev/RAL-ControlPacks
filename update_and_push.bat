@echo off
chcp 65001 >nul
echo.
echo ========================================
echo   RAL 控件包仓库 - 自动更新脚本
echo ========================================
echo.

cd /d "%~dp0"

echo [1/3] 生成 repository.json...
python generate_repository.py
if errorlevel 1 (
    echo 错误: 生成失败！
    pause
    exit /b 1
)

echo.
echo [2/3] 添加到 Git...
git add .

echo.
echo [3/3] 提交并推送...
git commit -m "🔄 更新控件包仓库"
git push

echo.
echo ========================================
echo   完成！
echo ========================================
pause

