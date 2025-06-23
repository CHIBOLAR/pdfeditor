"""
Build script to create a standalone executable for the PDF Text Editor
"""
import os
import sys
import subprocess

def build_executable():
    """Build the executable using PyInstaller"""
    
    print("PDF Text Editor - Build Script")
    print("=" * 50)
    
    # Check if PyInstaller is installed
    try:
        import PyInstaller
        print("[OK] PyInstaller is installed")
    except ImportError:
        print("[ERROR] PyInstaller not found. Installing...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])
        print("[OK] PyInstaller installed")
    
    # Build command
    build_cmd = [
        sys.executable, "-m", "PyInstaller",
        "--onefile",           # Single executable file
        "--windowed",          # No console window
        "--name", "PDF_Text_Editor",  # Name of the executable
        "--icon", "NONE",      # No icon (you can add your own .ico file)
        "--add-data", "requirements.txt;.",  # Include requirements file
        "gui.py"               # Main script
    ]
    
    print("\nBuilding executable...")
    print(f"Command: {' '.join(build_cmd)}")
    
    try:
        subprocess.check_call(build_cmd)
        print("\n[SUCCESS] Build successful!")
        print(f"Executable location: {os.path.join('dist', 'PDF_Text_Editor.exe')}")
        print("\nYou can now distribute the PDF_Text_Editor.exe file.")
        print("Users won't need Python installed to run it!")
    except subprocess.CalledProcessError as e:
        print(f"\n[ERROR] Build failed: {e}")
        return False
    
    return True

if __name__ == "__main__":
    build_executable()
    input("\nPress Enter to exit...")