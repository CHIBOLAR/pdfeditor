@echo off
echo PDF Text Editor Setup
echo ====================
echo.
echo Installing required dependencies...
echo.

pip install pikepdf

echo.
echo Optional: Installing test dependencies...
pip install reportlab

echo.
echo Setup complete!
echo.
echo To run the editor, double-click 'run_editor.bat' or run 'python gui.py'
echo.
pause