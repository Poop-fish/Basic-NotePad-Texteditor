from imports import *
from GT_NotePad import *
from GT_Style import *
  
def main():

    root = tk.Tk()
    
    root.title("Random NotePad")
    
    root.geometry("1200x800")
    
    root.iconbitmap("Assets/FaceLogo.ico")  
    
    Apply_GTstyle(root)  #! \\ Apply the custom style (this effects the interface i.e buttons ,menus , etc ...) \\
    
    text_editor = GTextEditor(wd=800, ht=600, default_font=("Arial", 15), bg="black", fg="lime")
    text_editor._build(root) 
    
    root.mainloop()

if __name__ == "__main__":
    main()

