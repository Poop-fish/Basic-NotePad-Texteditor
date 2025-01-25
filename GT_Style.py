from GT_imports import *

def Apply_GTstyle(root):
    style = ttk.Style(root)
    style.theme_use("alt")
    
    #* \\ Notebook Custom Style (Tabbed Interface) \\
    style.configure("TNotebook", background="#a1a1a1", tabmargins=[5, 5, 5, 0])
    style.configure("TNotebook.Tab" , background="Gray", foreground="Black", padding=[10, 5], font=("Arial", 12))
    style.map("TNotebook.Tab", background=[("selected", "Gray")])

    #* \\ Entry Widget Style \\
    style.configure("TEntry", fieldbackground="#444444", foreground="#00db00", font=("Arial", 14))
    
    #* \\ Button Styles (Text and Tab Color Buttons) \\
    style.configure("TButton", background="Gray", foreground="Black", font=("Arial", 14) ,relief="ridge", borderwidth=10)
    style.map("TButton", background=[("active", "darkgray")])
    
    #* \\ Scrollbar Style \\
    style.configure("TScrollbar", background="black", troughcolor="#444444", arrowcolor="#00db00" )
    
    #* \\ OptionMenu Styles (Font Menu: Size and Font Buttons) \\
    style.configure("TMenubutton", background="gray", foreground="Black", font=("Arial", 14) ,relief="ridge", borderwidth=10)
    style.map("TMenubutton", background=[("active", "darkgray")])
    
    #* \\ Dropdown Menu Customization for OptionMenu \\
    def customize_menu(option_menu):
        menu = option_menu["menu"]  #* \\ this gains Access to underlying Menu widget 
        menu.configure(
            bg="Gray",          #* \\ Background color
            fg="Black",             #* \\ Foreground (text) color
            font=("Arial", 12),  
            activebackground="light gray",  #* \\ Hover background
            activeforeground="#00db00"       #* \\ Hover text color
        )
        return menu
    
    return customize_menu 

