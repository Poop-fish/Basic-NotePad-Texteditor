from GT_imports import *
from GT_Style import *
class UIMenuToolbarManagement:
    def __init__(self):
        # Initialize any necessary variables
        pass
    def create_menu_bar(self, root):
        menu_bar = tk.Menu(root, bg="lightgray", fg="black", font=("Arial", 10))

        file_menu = tk.Menu(menu_bar, tearoff=0, bg="Gray", fg="black", font=("Arial", 12))
        file_menu.add_command(label="New Tab", command=self._new_tab, foreground="Black", font=("Arial", 12, "bold"))
        file_menu.add_command(label="Rename Tab", command=self._rename_tab, foreground="Black", font=("Arial", 12, "bold"))
        file_menu.add_command(label="Close Tab", command=self._close_tab, foreground="Black", font=("Arial", 12, "bold"))
        file_menu.add_command(label="Save", command=self._save_as_text, foreground="Black", font=("Arial", 12, "bold"))
        file_menu.add_command(label="Load", command=self._load_text, foreground="Black", font=("Arial", 12, "bold"))
        file_menu.add_command(label="Clear", command=self._clear_text, foreground="Black", font=("Arial", 12, "bold"))
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=root.quit, foreground="red", font=("Arial", 12, "bold"))
        
        menu_bar.add_cascade(label="File", menu=file_menu)

        edit_menu = tk.Menu(menu_bar, tearoff=0, bg="Gray", fg="black", font=("Arial", 12))
        edit_menu.add_command(label="Undo", command=self._undo, foreground="Black", font=("Arial", 12))
        edit_menu.add_command(label="Redo", command=self._redo, foreground="Black", font=("Arial", 12))
        edit_menu.add_separator()
        edit_menu.add_command(label="Find and Replace", command=self._find_and_replace, foreground="Black", font=("Arial", 12))
        edit_menu.add_separator()
        edit_menu.add_command(label="Highlight", command=self._toggle_Highlight_Box, foreground="Black", font=("Arial", 12))
        edit_menu.add_command(label="Bold", command=self._toggle_bold, foreground="Black", font=("Arial", 12))
        edit_menu.add_command(label="Italic", command=self._toggle_italic, foreground="Black", font=("Arial", 12))
        edit_menu.add_command(label="Underline", command=self._toggle_underline, foreground="Black", font=("Arial", 12))
        edit_menu.add_command(label="Strike", command=self._toggle_strike, foreground="Black", font=("Arial", 12))
        edit_menu.add_separator()
        edit_menu.add_command(label="Left Align", command=self._align_left, foreground="Black", font=("Arial", 12))
        edit_menu.add_command(label="Center Align", command=self._align_center, foreground="Black", font=("Arial", 12))
        edit_menu.add_command(label="Right Align", command=self._align_right, foreground="Black", font=("Arial", 12))

        menu_bar.add_cascade(label="Edit", menu=edit_menu)

        help_menu = tk.Menu(menu_bar, tearoff=0, bg="gray", fg="black", font=("Arial", 12))
        help_menu.add_command(label="About", command=self._show_about, foreground="black", font=("Arial", 12, "italic"))
        menu_bar.add_cascade(label="About", menu=help_menu)

        root.config(menu=menu_bar)

    def create_toolbar(self, root):
        toolbar = tk.Frame(root)
        toolbar.pack(side=tk.TOP, fill=tk.X)
        
        customize_menu = Apply_GTstyle(root)
        
        font_dropdown = ttk.OptionMenu(toolbar, self.font_var, *families(), command=self._update_font)
        font_dropdown.pack(side=tk.LEFT, padx=5)
        customize_menu(font_dropdown)
        
        size_dropdown = ttk.OptionMenu(toolbar, self.size_var, *[str(i) for i in range(5, 72)], command=self._update_font)
        size_dropdown.pack(side=tk.LEFT, padx=5)
        customize_menu(size_dropdown)

        color_button = ttk.Button(toolbar, text="Text Color", command=self._choose_color)
        color_button.pack(side=tk.LEFT, padx=5)

        bg_button = ttk.Button(toolbar, text="Tab Color", command=lambda: self._update_bg_fg('bg'))
        bg_button.pack(side=tk.LEFT, padx=5)
        
        datetime_button = ttk.Button(toolbar, text="Insert Date & Time", command=self._insert_datetime)
        datetime_button.pack(side=tk.LEFT, padx=5)
    
        bullet_button = ttk.Button(toolbar, text="Bullet Points", command=self._insert_bullets)
        bullet_button.pack(side=tk.LEFT, padx=5)

        numbered_button = ttk.Button(toolbar, text="Numbered List", command=self._insert_numbered_list)
        numbered_button.pack(side=tk.LEFT, padx=5) 

        spell_check_button = ttk.Button(toolbar, text="Spell Check", command=self._spell_check)
        spell_check_button.pack(side=tk.LEFT, padx=5)
