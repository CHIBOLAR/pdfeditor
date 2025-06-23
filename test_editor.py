import os
from pdf_editor import PDFTextEditor
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

def create_test_pdf(filename="test_document.pdf"):
    """Create a simple test PDF with some text"""
    c = canvas.Canvas(filename, pagesize=letter)
    
    # Add some test text
    c.drawString(100, 750, "Test PDF Document")
    c.drawString(100, 700, "This is a sample text that we will search and replace.")
    c.drawString(100, 650, "The quick brown fox jumps over the lazy dog.")
    c.drawString(100, 600, "Another line with the word fox in it.")
    c.drawString(100, 550, "Testing case sensitivity: FOX, Fox, fox")
    
    # Add a second page
    c.showPage()
    c.drawString(100, 750, "Page 2")
    c.drawString(100, 700, "This page also contains the word fox.")
    c.drawString(100, 650, "We can replace text across multiple pages.")
    
    c.save()
    print(f"Created test PDF: {filename}")

def test_pdf_editor():
    """Test the PDF editor functionality"""
    print("PDF Editor Test Suite")
    print("=" * 50)    
    # Create test PDF
    test_file = "test_document.pdf"
    create_test_pdf(test_file)
    
    # Initialize editor
    editor = PDFTextEditor()
    
    # Test 1: Load PDF
    print("\nTest 1: Loading PDF")
    if editor.load_pdf(test_file):
        print("✓ PDF loaded successfully")
        print(f"  Pages: {editor.get_page_count()}")
    else:
        print("✗ Failed to load PDF")
        return
    
    # Test 2: Extract preview
    print("\nTest 2: Text Preview")
    preview = editor.extract_text_preview()
    if preview:
        print("✓ Text preview extracted")
        print(f"  Preview: {preview[:100]}...")
    else:
        print("✗ Failed to extract preview")
    
    # Test 3: Search and Replace (case sensitive)
    print("\nTest 3: Case-sensitive search and replace")
    changes, pages = editor.search_and_replace("fox", "cat", case_sensitive=True)
    print(f"✓ Replaced {changes} occurrences on pages: {pages}")
    
    # Test 4: Save PDF
    print("\nTest 4: Saving PDF")
    output_file = "test_document_modified.pdf"
    if editor.save_pdf(output_file):
        print(f"✓ PDF saved as: {output_file}")
    else:
        print("✗ Failed to save PDF")
    
    # Test 5: Case-insensitive search
    print("\nTest 5: Case-insensitive search and replace")
    editor.load_pdf(test_file)  # Reload original
    changes, pages = editor.search_and_replace("FOX", "BEAR", case_sensitive=False)
    print(f"✓ Replaced {changes} occurrences on pages: {pages}")
    
    print("\n" + "=" * 50)
    print("All tests completed!")

if __name__ == "__main__":
    # Check if reportlab is available for creating test PDFs
    try:
        test_pdf_editor()
    except ImportError:
        print("Note: reportlab is required to create test PDFs")
        print("Install it with: pip install reportlab")