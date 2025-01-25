from GT_imports import *
from GT_Style import *
from GT_keybinds import *
from GT_Tab_Management import *
from GT_Widgets_Editor import * 
from GT_File_Operations import * 
from GT_Menu_Toolbar_Management import *
import subprocess

#! ----------------------- CORE MANAGEMENT--------------------------------------------------- 
class GTextEditor( TabManagement , Font_Text_Editor , FileOps , UIMenuToolbarManagement):
    def __init__(self, x=0, y=0, wd=600, ht=400, default_font=("Arial", 12), bg="white", fg="black"):
        self.x = x
        self.y = y
        self.width = wd
        self.height = ht
        self.default_font = default_font
        self.bg = bg
        self.fg = fg
        self.font_var = tk.StringVar(value=self.default_font[0])
        self.size_var = tk.IntVar(value=self.default_font[1])
        self.color_var = tk.StringVar(value=fg)
        self.tabs = []  
        self.keybindings = Keybindings(self)  
        
    
    def _build(self, root):
        self.create_menu_bar(root)
        self.create_toolbar(root)
        self.create_tabbed_text_area(root)
        self.create_output_window(root) 
        self.keybindings.setup(root)
    
    
    def _run_code(self):
        text_area = self._get_current_text_area()
        code = text_area.get("1.0", "end-1c").strip() 
        
        if not code:
            return  
        
        try:
            result = subprocess.run(
                ["python", "-c", code], capture_output=True, text=True
            )
            output = result.stdout + result.stderr
            
            if self.output_window:
                self.output_window.insert(tk.END, f"Output:\n{output}\n")
                self.output_window.see(tk.END) 
        except Exception as e:
            if self.output_window:
                self.output_window.insert(tk.END, f"Error: {str(e)}\n")
                self.output_window.see(tk.END)
    
    # ---------------------- Create the output window ----------------------
    def create_output_window(self, parent):
        self.output_window = tk.Text(parent, wrap=tk.WORD, height=10 , background="black", foreground="lime" ,relief="raised", borderwidth=15 , cursor="plus")
        self.output_window.pack(fill=tk.BOTH, padx=5, pady=5)
    

    
