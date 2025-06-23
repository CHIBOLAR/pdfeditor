import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from pdf_editor import PDFTextEditor
import os

class PDFEditorGUI:
    def __init__(self):
        self.editor = PDFTextEditor()
        self.current_file = None
        self.setup_gui()
        
    def setup_gui(self):
        self.window = tk.Tk()
        self.window.title("Offline PDF Text Editor")
        self.window.geometry("700x600")
        
        # Create menu bar
        menubar = tk.Menu(self.window)
        self.window.config(menu=menubar)
        
        # File menu
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Open PDF", command=self.load_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_command(label="Save As...", command=self.save_file_as)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.window.quit)        
        # Main frame
        main_frame = ttk.Frame(self.window, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # File info frame
        info_frame = ttk.LabelFrame(main_frame, text="PDF Information", padding="10")
        info_frame.grid(row=0, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=5)
        
        self.file_label = ttk.Label(info_frame, text="No file loaded")
        self.file_label.grid(row=0, column=0, sticky=tk.W)
        
        self.pages_label = ttk.Label(info_frame, text="Pages: 0")
        self.pages_label.grid(row=1, column=0, sticky=tk.W)
        
        # Search and Replace frame
        search_frame = ttk.LabelFrame(main_frame, text="Search and Replace", padding="10")
        search_frame.grid(row=1, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=10)
        
        # Search field
        ttk.Label(search_frame, text="Search for:").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.search_entry = ttk.Entry(search_frame, width=50)
        self.search_entry.grid(row=0, column=1, padx=10, pady=5)
        
        # Replace field
        ttk.Label(search_frame, text="Replace with:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.replace_entry = ttk.Entry(search_frame, width=50)
        self.replace_entry.grid(row=1, column=1, padx=10, pady=5)        
        # Options
        self.case_sensitive_var = tk.BooleanVar(value=True)
        case_check = ttk.Checkbutton(search_frame, text="Case sensitive", 
                                    variable=self.case_sensitive_var)
        case_check.grid(row=2, column=1, sticky=tk.W, padx=10, pady=5)
        
        # Buttons
        button_frame = ttk.Frame(search_frame)
        button_frame.grid(row=3, column=0, columnspan=2, pady=10)
        
        ttk.Button(button_frame, text="Find & Replace All", 
                  command=self.find_replace).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Clear", 
                  command=self.clear_fields).pack(side=tk.LEFT, padx=5)
        
        # Preview frame
        preview_frame = ttk.LabelFrame(main_frame, text="Text Preview (First Page)", padding="10")
        preview_frame.grid(row=2, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S), pady=10)
        
        # Text widget with scrollbar
        text_scroll = ttk.Scrollbar(preview_frame)
        text_scroll.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.preview_text = tk.Text(preview_frame, height=10, width=60, 
                                   yscrollcommand=text_scroll.set)
        self.preview_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        text_scroll.config(command=self.preview_text.yview)
        
        # Status bar
        self.status_bar = ttk.Label(self.window, text="Ready", relief=tk.SUNKEN)
        self.status_bar.grid(row=1, column=0, sticky=(tk.W, tk.E))
        
        # Configure grid weights
        self.window.rowconfigure(0, weight=1)
        self.window.columnconfigure(0, weight=1)
        main_frame.rowconfigure(2, weight=1)    
    def load_file(self):
        """Load a PDF file"""
        filename = filedialog.askopenfilename(
            title="Select PDF file",
            filetypes=[("PDF files", "*.pdf"), ("All files", "*.*")]
        )
        
        if filename:
            self.status_bar.config(text="Loading PDF...")
            self.window.update()
            
            if self.editor.load_pdf(filename):
                self.current_file = filename
                self.file_label.config(text=f"File: {os.path.basename(filename)}")
                self.pages_label.config(text=f"Pages: {self.editor.get_page_count()}")
                
                # Show text preview
                preview = self.editor.extract_text_preview()
                self.preview_text.delete(1.0, tk.END)
                self.preview_text.insert(1.0, preview)
                
                self.status_bar.config(text="PDF loaded successfully")
                messagebox.showinfo("Success", "PDF loaded successfully!")
            else:
                self.status_bar.config(text="Failed to load PDF")
                messagebox.showerror("Error", "Failed to load PDF file")
    
    def save_file(self):
        """Save the current PDF"""
        if not self.current_file:
            messagebox.showwarning("Warning", "No file is currently loaded")
            return
        
        self.status_bar.config(text="Saving PDF...")
        self.window.update()
        
        if self.editor.save_pdf():
            self.status_bar.config(text="PDF saved successfully")
            messagebox.showinfo("Success", "PDF saved successfully!")
        else:
            self.status_bar.config(text="Failed to save PDF")
            messagebox.showerror("Error", "Failed to save PDF")    
    def save_file_as(self):
        """Save the PDF with a new name"""
        if not self.current_file:
            messagebox.showwarning("Warning", "No file is currently loaded")
            return
        
        filename = filedialog.asksaveasfilename(
            title="Save PDF as",
            defaultextension=".pdf",
            filetypes=[("PDF files", "*.pdf"), ("All files", "*.*")]
        )
        
        if filename:
            self.status_bar.config(text="Saving PDF...")
            self.window.update()
            
            if self.editor.save_pdf(filename):
                self.current_file = filename
                self.file_label.config(text=f"File: {os.path.basename(filename)}")
                self.status_bar.config(text="PDF saved successfully")
                messagebox.showinfo("Success", "PDF saved successfully!")
            else:
                self.status_bar.config(text="Failed to save PDF")
                messagebox.showerror("Error", "Failed to save PDF")
    
    def find_replace(self):
        """Perform find and replace operation"""
        if not self.current_file:
            messagebox.showwarning("Warning", "Please load a PDF file first")
            return
        
        search_text = self.search_entry.get()
        replace_text = self.replace_entry.get()
        
        if not search_text:
            messagebox.showwarning("Warning", "Please enter text to search for")
            return
        
        self.status_bar.config(text="Performing search and replace...")
        self.window.update()
        
        case_sensitive = self.case_sensitive_var.get()
        changes, pages = self.editor.search_and_replace(search_text, replace_text, case_sensitive)
        
        if changes > 0:
            pages_str = ", ".join(map(str, pages))
            self.status_bar.config(text=f"Made {changes} replacements on pages: {pages_str}")
            
            # Update preview
            preview = self.editor.extract_text_preview()
            self.preview_text.delete(1.0, tk.END)
            self.preview_text.insert(1.0, preview)
            
            messagebox.showinfo("Success", 
                              f"Replaced {changes} occurrence(s) on page(s): {pages_str}")
        else:
            self.status_bar.config(text="No matches found")
            messagebox.showinfo("Result", "No matches found")    
    def clear_fields(self):
        """Clear search and replace fields"""
        self.search_entry.delete(0, tk.END)
        self.replace_entry.delete(0, tk.END)
        self.status_bar.config(text="Fields cleared")
    
    def run(self):
        """Start the GUI application"""
        self.window.mainloop()


if __name__ == "__main__":
    app = PDFEditorGUI()
    app.run()