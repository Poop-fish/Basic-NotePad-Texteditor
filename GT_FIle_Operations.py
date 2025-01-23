from GT_imports import *
class FileOps:
    def __init__(self):
        pass
#! ----------------------- FILE OPERATIONS MANAGEMENT -----------------------------------------------------
    def _save_as_text(self):
        file_path = asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
            title="Save As"
        )
        if file_path:
            with open(file_path, "w") as file:
                file.write(self._get_current_text_area().get("1.0", "end-1c"))

    def _load_text(self):
        """Open a file using a file dialog and load its content into the current tab."""
        file_path = askopenfilename(
            title="Open File",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
        if file_path:
            try:
                with open(file_path, "r") as file:
                    self._get_current_text_area().delete("1.0", "end")
                    self._get_current_text_area().insert("1.0", file.read())
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred while loading the file: {e}")
    
    def _show_about(self):
        messagebox.showinfo("About", "This is an basic text editor with tabs, find & replace, and more.") 

#! -----------------------END OF FILE OPERATIONS MANAGEMENT -----------------------------------------------------