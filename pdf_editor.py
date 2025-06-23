import pikepdf
from pathlib import Path
import re

class PDFTextEditor:
    def __init__(self):
        self.pdf = None
        self.filepath = None
        self.original_content = {}
    
    def load_pdf(self, filename):
        """Load PDF file"""
        try:
            self.pdf = pikepdf.open(filename)
            self.filepath = filename
            # Store original content for potential undo functionality
            self.original_content = {}
            return True
        except Exception as e:
            print(f"Error loading PDF: {e}")
            return False
    
    def save_pdf(self, save_as=None):
        """Save changes to PDF file"""
        if self.pdf:
            try:
                if save_as:
                    self.pdf.save(save_as)
                else:
                    self.pdf.save(self.filepath)
                return True
            except Exception as e:
                print(f"Error saving PDF: {e}")
                return False
        return False    
    def search_and_replace(self, search_text, replace_text, case_sensitive=True):
        """Find and replace text in PDF"""
        changes_made = 0
        modified_pages = []
        
        if not self.pdf:
            return 0
        
        try:
            for page_num, page in enumerate(self.pdf.pages):
                page_modified = False
                
                # Extract content streams
                if '/Contents' in page:
                    contents = page['/Contents']
                    
                    # Handle both single content stream and array of streams
                    if hasattr(contents, '__iter__') and not isinstance(contents, (str, bytes)):
                        content_list = contents
                    else:
                        content_list = [contents]
                    
                    for content in content_list:
                        try:
                            # Read content as bytes
                            content_bytes = content.read_bytes()
                            
                            # Try to decode content
                            try:
                                content_str = content_bytes.decode('utf-8')
                            except:
                                content_str = content_bytes.decode('latin-1')                            
                            # Perform search and replace
                            if case_sensitive:
                                if search_text in content_str:
                                    new_content = content_str.replace(search_text, replace_text)
                                    page_modified = True
                            else:
                                # Case insensitive search
                                pattern = re.compile(re.escape(search_text), re.IGNORECASE)
                                if pattern.search(content_str):
                                    new_content = pattern.sub(replace_text, content_str)
                                    page_modified = True
                            
                            # Update content if modified
                            if page_modified:
                                # Write back the modified content
                                content.write(new_content.encode('utf-8'))
                                changes_made += 1
                                
                        except Exception as e:
                            print(f"Error processing content stream on page {page_num + 1}: {e}")
                            continue
                
                if page_modified:
                    modified_pages.append(page_num + 1)
        
        except Exception as e:
            print(f"Error during search and replace: {e}")
        
        return changes_made, modified_pages    
    def get_page_count(self):
        """Get total number of pages in PDF"""
        if self.pdf:
            return len(self.pdf.pages)
        return 0
    
    def extract_text_preview(self, page_num=0, max_chars=500):
        """Extract text preview from a specific page"""
        if not self.pdf or page_num >= len(self.pdf.pages):
            return ""
        
        try:
            page = self.pdf.pages[page_num]
            text = ""
            
            if '/Contents' in page:
                contents = page['/Contents']
                
                if hasattr(contents, '__iter__') and not isinstance(contents, (str, bytes)):
                    content_list = contents
                else:
                    content_list = [contents]
                
                for content in content_list:
                    try:
                        content_bytes = content.read_bytes()
                        try:
                            text += content_bytes.decode('utf-8')
                        except:
                            text += content_bytes.decode('latin-1')
                    except:
                        continue
            
            # Clean up the text for preview
            text = re.sub(r'[^\x20-\x7E\n]', ' ', text)
            return text[:max_chars] + "..." if len(text) > max_chars else text
            
        except Exception as e:
            print(f"Error extracting text preview: {e}")
            return ""