# Release Instructions

## Creating a GitHub Release

To share the executable with others, create a GitHub Release:

1. Go to https://github.com/CHIBOLAR/pdfeditor
2. Click on "Releases" (right side of the page)
3. Click "Create a new release"
4. Choose a tag (e.g., v1.0.0)
5. Set release title: "PDF Text Editor v1.0.0"
6. Add description:
   ```
   ## Offline PDF Text Editor
   
   A simple tool to search and replace text in PDF files without internet connection.
   
   ### Download
   - Download `PDF_Text_Editor_Portable.zip`
   - Extract and run `PDF_Text_Editor.exe`
   - No installation or Python required!
   
   ### Features
   - Search and replace text across all PDF pages
   - Case-sensitive/insensitive search
   - Preview PDF content
   - Preserves original formatting
   ```
7. Upload the file: `dist/PDF_Text_Editor_Portable.zip`
8. Click "Publish release"

## Building the Executable

To build a new executable:
```bash
python build_exe.py
```

The executable will be created in the `dist` folder.

## Distribution Options

1. **GitHub Releases** (Recommended)
   - Best for public distribution
   - Users can download directly from GitHub

2. **Direct File Sharing**
   - Email the `dist/PDF_Text_Editor_Portable.zip`
   - Upload to cloud storage (Google Drive, Dropbox, etc.)
   - Transfer via USB drive

## File Locations
- Executable: `dist/PDF_Text_Editor.exe`
- Portable ZIP: `dist/PDF_Text_Editor_Portable.zip`