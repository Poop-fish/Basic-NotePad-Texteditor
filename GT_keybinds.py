class Keybindings:
    def __init__(self, editor):
        self.editor = editor  
    
    def setup(self, root):
        root.bind_all("<Control-z>", lambda event: self.editor._new_tab())
        root.bind_all("<Control-x>", lambda event: self.editor._close_tab())
        root.bind_all("<Control-c>", lambda event: self.editor. _rename_tab())       
        root.bind_all("<Control-s>", lambda event: self.editor._save_as_text()) 
        root.bind_all("<Control-a>", lambda event: self.editor._load_text())   
        root.bind_all("<Control-q>", lambda event: root.quit())          

        root.bind_all("<Control-e>", lambda event: self.editor._undo())        
        root.bind_all("<Control-r>", lambda event: self.editor._redo())         
        root.bind_all("<Control-w>", lambda event: self.editor._find_and_replace()) 

        root.bind_all("<Control-b>", lambda event: self.editor._toggle_bold()) 
        root.bind_all("<Control-v>", lambda event: self.editor._toggle_italic())
        root.bind_all("<Control-n>", lambda event: self.editor._toggle_underline()) 

        root.bind_all("<Control-f>", lambda event: self.editor._align_left())   
        root.bind_all("<Control-g>", lambda event: self.editor._align_center()) 
        root.bind_all("<Control-h>", lambda event: self.editor._align_right())  
        
        
