from imports import *
from GT_NotePad import GTextEditor

def main():
    root = tk.Tk()
    root.title("Text Editor")
    root.geometry("800x600")
    root.iconbitmap("Assets/FaceLogo.ico")  
    text_editor = GTextEditor(x=0, y=0, wd=800, ht=600, default_font=("Arial", 12), bg="white", fg="black")
    text_editor._build(root)
    
    root.mainloop()

if __name__ == "__main__":
    main()
