from GT_imports import *
from GT_NotePad import *

# \\ This is how you can build the NotePad into a tk window \\
def Example():

    root = tk.Tk()
    
    root.title("Random NotePad")
    
    root.geometry("1200x800")
    
    root.iconbitmap("Assets/FaceLogo.ico")  
    
    Apply_GTstyle(root)  #! \\ Apply the custom style (this effects the interface i.e buttons ,menus , etc ...) 
    
    #! \\ Create a GTextEditor Widget and build it into the tk window \\
    text_editor = GTextEditor(wd=800, ht=600, default_font=("Arial", 15), bg="black", fg="lime")
    text_editor._build(root ) 
    
    root.mainloop()

if __name__ == "__main__":
    Example()


