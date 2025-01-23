from GT_imports import *
from GT_Style import *
from GT_keybinds import *
from GT_Tab_Management import *
from GT_Editor import * 
from GT_FIle_Operations import * 
from GT_Menu_Toolbar_Management import *

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
        self.keybindings.setup(root)

