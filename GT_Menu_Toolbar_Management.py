from GT_imports import *
from GT_Style import *
class UIMenuToolbarManagement:
    def __init__(self):
        # Initialize any necessary variables
        pass
    
    def create_menu_bar(self, root):
        
        menu_bar = tk.Menu(root, bg="lightgray", fg="black", font=("Arial", 10))
        
        file_menu = tk.Menu(menu_bar, tearoff=0, bg="Gray", fg="black", font=("Arial", 12))
        file_menu.add_command(label="New Tab", command=self._new_tab, foreground="Black", font=("Arial", 12, "bold"),activebackground="lightgray", activeforeground="Lime")
        file_menu.add_command(label="Rename Tab", command=self._rename_tab, foreground="Black", font=("Arial", 12, "bold"),activebackground="lightgray", activeforeground="Lime")
        file_menu.add_command(label="Close Tab", command=self._close_tab, foreground="Black", font=("Arial", 12, "bold"),activebackground="lightgray", activeforeground="Lime")
        file_menu.add_separator()
        file_menu.add_command(label="Save", command=self._save_as_text, foreground="Black", font=("Arial", 12, "bold"),activebackground="lightgray", activeforeground="Lime")
        file_menu.add_command(label="Load", command=self._load_text, foreground="Black", font=("Arial", 12, "bold"),activebackground="lightgray", activeforeground="Lime")
        file_menu.add_command(label="Clear", command=self._clear_text, foreground="Black", font=("Arial", 12, "bold"),activebackground="lightgray", activeforeground="Lime")
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=root.quit, foreground="red", font=("Arial", 12, "bold"),activebackground="Yellow", activeforeground="red")
        
        menu_bar.add_cascade(label="File", menu=file_menu)

        edit_menu = tk.Menu(menu_bar, tearoff=0, bg="Gray", fg="black", font=("Arial", 12))
        edit_menu.add_command(label="Undo", command=self._undo, foreground="Black", font=("Arial", 12),activebackground="lightgray", activeforeground="Lime")
        edit_menu.add_command(label="Redo", command=self._redo, foreground="Black", font=("Arial", 12),activebackground="lightgray", activeforeground="Lime")
        edit_menu.add_separator()
        edit_menu.add_command(label="Find and Replace", command=self._find_and_replace, foreground="Black", font=("Arial", 12),activebackground="lightgray", activeforeground="Lime")
        edit_menu.add_separator()
        edit_menu.add_command(label="Frame", command=self._toggle_border, foreground="Black", font=("Arial", 12),activebackground="lightgray", activeforeground="Lime")
        edit_menu.add_command(label="Highlight", command=self._toggle_Highlight_Box, foreground="Black", font=("Arial", 12),activebackground="lightgray", activeforeground="Lime")
        edit_menu.add_command(label="Bold", command=self._toggle_bold, foreground="Black", font=("Arial", 12),activebackground="lightgray", activeforeground="Lime")
        edit_menu.add_command(label="Italic", command=self._toggle_italic, foreground="Black", font=("Arial", 12),activebackground="lightgray", activeforeground="Lime")
        edit_menu.add_command(label="Underline", command=self._toggle_underline, foreground="Black", font=("Arial", 12),activebackground="lightgray", activeforeground="Lime")
        edit_menu.add_command(label="Strike", command=self._toggle_strike, foreground="Black", font=("Arial", 12),activebackground="lightgray", activeforeground="Lime")
        edit_menu.add_separator()
        edit_menu.add_command(label="Bullet Points", command=self._insert_bullets, foreground="Black", font=("Arial", 12),activebackground="lightgray", activeforeground="Lime")
        edit_menu.add_command(label="Numbered List", command=self._insert_numbered_list, foreground="Black", font=("Arial", 12),activebackground="lightgray", activeforeground="Lime")
        edit_menu.add_separator()
        edit_menu.add_command(label="Left Align", command=self._align_left, foreground="Black", font=("Arial", 12),activebackground="lightgray", activeforeground="Lime")
        edit_menu.add_command(label="Center Align", command=self._align_center, foreground="Black", font=("Arial", 12),activebackground="lightgray", activeforeground="Lime")
        edit_menu.add_command(label="Right Align", command=self._align_right, foreground="Black", font=("Arial", 12),activebackground="lightgray", activeforeground="Lime")
        edit_menu.add_separator()
        edit_menu.add_command(label="Insert Hyperlink", command=self._insert_hyperlink, foreground="Blue", font=("Arial", 12),activebackground="lightgray", activeforeground="Lime")
        edit_menu.add_separator()
        edit_menu.add_command(label="Text Color", command=self. _choose_color, foreground="Black", font=("Arial", 12),activebackground="lightgray", activeforeground="Lime")
        edit_menu.add_command(label="Tab Color", command=lambda: self._update_bg_fg('bg'), foreground="Black", font=("Arial", 12),activebackground="lightgray", activeforeground="Lime")
        menu_bar.add_cascade(label="Edit", menu=edit_menu)


        Widget_menu = tk.Menu(menu_bar, tearoff=0, bg="gray", fg="black", font=("Arial", 12))
        Widget_menu.add_command(label="Show Clock", command=self._add_clock, foreground="black", font=("Arial", 12, "italic"), activebackground="lightgray", activeforeground="Lime")
        Widget_menu.add_separator()
        Widget_menu.add_command(label="Freehand Drawing", command=self._open_freehand_drawing)
        Widget_menu.add_separator()
        Widget_menu.add_command(label="Calculator", command=self._add_calculator)
        Widget_menu.add_separator()
        Widget_menu.add_command(label="Speech to Text", command=self._speech_to_text, foreground="black", font=("Arial", 12, "italic"), activebackground="lightgray", activeforeground="Lime")
        Widget_menu.add_separator()
        Widget_menu.add_command(label="Spell Check", command=self._spell_check, foreground="black", font=("Arial", 12, "italic"), activebackground="lightgray", activeforeground="Lime")
        menu_bar.add_cascade(label="Widgets", menu=Widget_menu)
      
        help_menu = tk.Menu(menu_bar, tearoff=0, bg="gray", fg="black", font=("Arial", 12))
        help_menu.add_command(label="Key Binds", command=self._show_keybinds_panel, foreground="black", font=("Arial", 12, "italic"),activebackground="lightgray", activeforeground="Lime")
        help_menu.add_command(label="About", command=self._show_about, foreground="black", font=("Arial", 12, "italic"),activebackground="lightgray", activeforeground="Lime")
        menu_bar.add_cascade(label="About/Help", menu=help_menu) 

        
        root.config(menu=menu_bar)
    

    def _show_keybinds_panel(self):
        keybind_window = tk.Toplevel()
        keybind_window.title("Key Binds")
        keybind_window.geometry("450x800")
        keybind_window.resizable(False, False)
        keybind_window.configure(bg="#2b2b2b")

        title_label = tk.Label(
            keybind_window, 
            text="KeyBind-ShortCuts", 
            font=("Comic Sans MS", 19, "bold"), 
            bg="Black",
            width=15, height=1, 
            fg="Lime", 
            relief="raised", 
            borderwidth=10,
            cursor="hand2"
        )
        
        def on_enter(event):
            title_label.config(bg="lightgray", fg="Lime")  

        def on_leave(event):
            title_label.config(bg="Black", fg="Lime")
        
        title_label.bind("<Enter>", on_enter)
        title_label.bind("<Leave>", on_leave)
        title_label.pack(pady=10)

        # Add a frame to hold the keybinds
        frame = tk.Frame(keybind_window , relief="sunken" , borderwidth=15 ,bg='gray',cursor="hand2")
        frame.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)
        keybinds = [
            ("Ctrl+Z", "New Tab"),
            ("Ctrl+C", "Rename Tab"),
            ("Ctrl+X", "Close Tab"),
            ("Ctrl+S", "Save"),
            ("Ctrl+A", "Load"),
            ("Ctrl+E", "Undo"),
            ("Ctrl+R", "Redo"),
            ("Ctrl+W", "Find and Replace"),
            ("Ctrl+B", "Bold"),
            ("Ctrl+V", "Italic"),
            ("Ctrl+N", "Underline"),
            ("Ctrl+F", "Left Align"),
            ("Ctrl+G", "Center Align"),
            ("Ctrl+H", "Right Align"),
        ]

        for key, action in keybinds:
            parts = key.split('+')
            
            key_label_part1 = tk.Label(
                frame, text=parts[0], font=("Comic Sans MS", 10), anchor="center",
                width=8, relief="raised", borderwidth=10, bg="black", fg="lime"
            )
            plus_label = tk.Label(
                frame, text='+', font=("Comic Sans MS", 10), anchor="center",
                width=3, relief="raised", borderwidth=10, bg="black", fg="red"
            )
            key_label_part2 = tk.Label(
                frame, text=parts[1], font=("Comic Sans MS", 10), anchor="center",
                width=8, relief="raised", borderwidth=10, bg="black", fg="yellow"
            )
            action_label = tk.Label(
                frame, text=action, font=("Comic Sans MS", 10), anchor="w",
                relief="ridge", borderwidth=10, padx=10, bg="black", fg="white"
            )

            row_index = keybinds.index((key, action)) 
            key_label_part1.grid(row=row_index, column=0, padx=5, pady=2, sticky="w")  
            plus_label.grid(row=row_index, column=1, padx=0, pady=2, sticky="w")      
            key_label_part2.grid(row=row_index, column=2, padx=5, pady=2, sticky="w")  
            action_label.grid(row=row_index, column=3, padx=5, pady=2, sticky="w")     

        close_button = ttk.Button(keybind_window, text="Close", command=keybind_window.destroy)
        close_button.pack(pady=10)


   
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

        datetime_button = ttk.Button(toolbar, text="Insert Date & Time", command=self._insert_datetime)
        datetime_button.pack(side=tk.LEFT, padx=5)
    
        spell_check_button = ttk.Button(toolbar, text="Spell Check", command=self._spell_check)
        spell_check_button.pack(side=tk.LEFT, padx=5)
        
        self.status_label = ttk.Label(root, text="Words Type → 0", anchor="w", background="#444444" , foreground="lime" )
        self.status_label.pack(side=tk.BOTTOM, fill=tk.X)
            
        run_code_button = ttk.Button(toolbar, text="Run Code", command=self._run_code , style='TButton')
        run_code_button.pack(side=tk.LEFT, padx=5)

        terminal_button = ttk.Button(toolbar, text="Open Terminal", command=self._open_terminal)
        terminal_button.pack(side=tk.LEFT, padx=5)
        

        self.mousePos_label = tk.Label(root, text="Mouse Position: (0, 0)", bg="#444444", fg="lime", anchor="w")
        self.mousePos_label.pack(side=tk.BOTTOM, fill=tk.X)
        root.bind('<Motion>', self.update_mouse_position)
    def update_mouse_position(self, event):
        x, y = event.x, event.y
        self.mousePos_label.config(text=f"Mouse Position: ({x}, {y})")

        # speech_button = ttk.Button(toolbar, text="Speech to Text", command=self._speech_to_text)
        # speech_button.pack(side=tk.LEFT, padx=5) 
        
        # clock_button = tk.Button(root, text="Show Clock", command=self._add_clock)
        # clock_button.pack(pady=10)
        
        # bullet_button = ttk.Button(toolbar, text="Bullet Points", command=self._insert_bullets)
        # bullet_button.pack(side=tk.LEFT, padx=5)

        # numbered_button = ttk.Button(toolbar, text="Numbered List", command=self._insert_numbered_list)
        # numbered_button.pack(side=tk.LEFT, padx=5) 

        # color_button = ttk.Button(toolbar, text="Text Color", command=self._choose_color)
        # color_button.pack(side=tk.LEFT, padx=5)

        # bg_button = ttk.Button(toolbar, text="Tab Color", command=lambda: self._update_bg_fg('bg'))
        # bg_button.pack(side=tk.LEFT, padx=5) 

        # calculator_button = ttk.Button(toolbar, text="Open Calculator", command=self._add_calculator)
        # calculator_button.pack(side=tk.LEFT, padx=5) 

        # add_frame = ttk.Button(toolbar, text="Add Frame", command=self._toggle_border)
        # add_frame.pack(side=tk.LEFT, padx=5)
