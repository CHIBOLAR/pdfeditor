@echo off
cd /d "C:\Custom PDF editor"

echo Current directory: %CD%
echo Cleaning previous build...
if exist build rmdir /s /q build
if exist dist rmdir /s /q dist

echo Installing/updating dependencies...
pip install --upgrade -r requirements.txt

echo Building executable with PyInstaller...
pyinstaller PDF_Text_Editor.spec --clean --noconfirm

echo Build complete!
if exist "dist\PDF_Text_Editor.exe" (
    echo SUCCESS: PDF_Text_Editor.exe created in dist folder
) else (
    echo ERROR: Build failed - executable not found
)

pause
