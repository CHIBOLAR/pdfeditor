# Offline PDF Text Editor

A simple offline PDF text editor that allows you to search and replace text in PDF files without requiring an internet connection.

## Features

- Load and edit PDF files offline
- Search and replace text across all pages
- Case-sensitive and case-insensitive search options
- Preview text content from PDFs
- Save edited PDFs with original formatting preserved
- Simple and intuitive GUI interface

## Requirements

- Python 3.8 or higher
- pikepdf library

## Installation

1. Navigate to the project directory:
   ```
   cd "C:\Custom PDF editor"
   ```

2. Install required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

### Running the Application

Run the GUI application:```
python gui.py
```

### How to Use

1. **Load a PDF**: Click "File" → "Open PDF" or use the "Load PDF" button
2. **Enter Search Text**: Type the text you want to find in the "Search for" field
3. **Enter Replacement Text**: Type the replacement text in the "Replace with" field
4. **Choose Options**: Check/uncheck "Case sensitive" as needed
5. **Find & Replace**: Click "Find & Replace All" to replace all occurrences
6. **Save Changes**: Click "File" → "Save" to save changes to the original file, or "Save As" to save with a new name

### Testing

To run the test suite:
```
python test_editor.py
```

Note: The test script requires `reportlab` to create test PDFs:
```
pip install reportlab
```

## Creating a Standalone Executable

To create a standalone .exe file (no Python required):

1. Install PyInstaller:
   ```
   pip install pyinstaller
   ```

2. Create the executable:
   ```
   pyinstaller --onefile --windowed --name "PDF_Text_Editor" gui.py
   ```

3. The executable will be created in the `dist` folder

## Limitations

- Works with text-based PDFs (not scanned images)
- May not preserve complex formatting in some PDFs
- Text in images or complex graphics cannot be edited

## Troubleshooting

- **"Failed to load PDF"**: Ensure the PDF is not corrupted or password-protected
- **No text found**: The PDF might contain scanned images instead of text
- **Encoding issues**: Some special characters might not display correctly

## License

This is a custom offline tool for personal use.