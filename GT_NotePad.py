from imports import *

class GTextEditor:
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

    def _build(self, root):
        self._create_menu_bar(root)
        self._create_toolbar(root)
        self._create_tabbed_text_area(root)

    def _create_menu_bar(self, root):
        menu_bar = tk.Menu(root)

        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="New Tab", command=self._new_tab)
        file_menu.add_command(label="Close Tab", command=self._close_tab)
        file_menu.add_command(label="Save", command=self._save_text)
        file_menu.add_command(label="Load", command=self._load_text)
        file_menu.add_command(label="Clear", command=self._clear_text)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=root.quit)
        menu_bar.add_cascade(label="File", menu=file_menu)

        edit_menu = tk.Menu(menu_bar, tearoff=0)
        edit_menu.add_command(label="Undo", command=self._undo)
        edit_menu.add_command(label="Redo", command=self._redo)
        edit_menu.add_separator()
        edit_menu.add_command(label="Find and Replace", command=self._find_and_replace)
        edit_menu.add_separator()
        edit_menu.add_command(label="Bold", command=self._toggle_bold)
        edit_menu.add_command(label="Italic", command=self._toggle_italic)
        edit_menu.add_command(label="Underline", command=self._toggle_underline)
        edit_menu.add_command(label="Strike", command=self._toggle_strike)
        edit_menu.add_separator()
        edit_menu.add_command(label="Left Align", command=self._align_left)
        edit_menu.add_command(label="Center Align", command=self._align_center)
        edit_menu.add_command(label="Right Align", command=self._align_right)

        menu_bar.add_cascade(label="Edit", menu=edit_menu)

        help_menu = tk.Menu(menu_bar, tearoff=0)
        help_menu.add_command(label="About", command=self._show_about)
        menu_bar.add_cascade(label="About", menu=help_menu)

        root.config(menu=menu_bar)

    def _create_toolbar(self, root):
        toolbar = tk.Frame(root)
        toolbar.pack(side=tk.TOP, fill=tk.X)

        font_dropdown = ttk.OptionMenu(toolbar, self.font_var, *families(), command=self._update_font)
        font_dropdown.pack(side=tk.LEFT, padx=5)

        size_dropdown = ttk.OptionMenu(toolbar, self.size_var, *[str(i) for i in range(8, 72)], command=self._update_font)
        size_dropdown.pack(side=tk.LEFT, padx=5)

        color_button = ttk.Button(toolbar, text="Text Color", command=self._choose_color)
        color_button.pack(side=tk.LEFT, padx=5)

        bg_button = ttk.Button(toolbar, text="Background Color", command=lambda: self._update_bg_fg('bg'))
        bg_button.pack(side=tk.LEFT, padx=5)

    def _update_bg_fg(self, mode):
        """Update background or foreground color of the current text area."""
        color = askcolor()[1]
        if color:
            current_text_area = self._get_current_text_area()
            if mode == 'bg':
                current_text_area.configure(bg=color)

    def _create_tabbed_text_area(self, root):
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill=tk.BOTH, expand=True)
        self._new_tab()

    def _new_tab(self):
        frame = tk.Frame(self.notebook, bg=self.bg)
        text_area = tk.Text(frame, font=self.default_font, wrap="word", bg=self.bg, fg=self.fg, undo=True)
        scrollbar = ttk.Scrollbar(frame, command=text_area.yview)
        text_area.configure(yscrollcommand=scrollbar.set)

        text_area.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.notebook.add(frame, text=f"Tab {len(self.tabs) + 1}")
        self.tabs.append(text_area)

    def _close_tab(self):
        current_tab = self.notebook.index(self.notebook.select())
        if len(self.tabs) > 1:
            self.notebook.forget(current_tab)
            del self.tabs[current_tab]
        else:
            messagebox.showwarning("Warning", "Cannot close the last tab!")

    def _get_current_text_area(self):
        current_tab = self.notebook.index(self.notebook.select())
        return self.tabs[current_tab]

    def _find_and_replace(self):
        find_replace_win = tk.Toplevel()
        find_replace_win.title("Find and Replace")

        tk.Label(find_replace_win, text="Find:").grid(row=0, column=0, padx=5, pady=5)
        find_entry = ttk.Entry(find_replace_win, width=30)
        find_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(find_replace_win, text="Replace:").grid(row=1, column=0, padx=5, pady=5)
        replace_entry = ttk.Entry(find_replace_win, width=30)
        replace_entry.grid(row=1, column=1, padx=5, pady=5)

        def perform_replace():
            text_area = self._get_current_text_area()
            find_text = find_entry.get()
            replace_text = replace_entry.get()
            content = text_area.get("1.0", "end")
            new_content = content.replace(find_text, replace_text)
            text_area.delete("1.0", "end")
            text_area.insert("1.0", new_content)

        ttk.Button(find_replace_win, text="Replace All", command=perform_replace).grid(row=2, column=0, columnspan=2, pady=10)

    def _undo(self):
        self._get_current_text_area().edit_undo()

    def _redo(self):
        self._get_current_text_area().edit_redo()

    def _update_font(self, *args):
        current_font = (self.font_var.get(), self.size_var.get())
        selected_text = self._get_current_text_area().tag_ranges("sel")
        if selected_text:
            self._get_current_text_area().tag_add("font", selected_text[0], selected_text[1])
            self._get_current_text_area().tag_configure("font", font=current_font)
        else:
            self._get_current_text_area().configure(font=current_font)

    def _choose_color(self):
        color = askcolor()[1]
        if color:
            selected_text = self._get_current_text_area().tag_ranges("sel")
            if selected_text:
                self._get_current_text_area().tag_add("color", selected_text[0], selected_text[1])
                self._get_current_text_area().tag_configure("color", foreground=color)
            else:
                self._get_current_text_area().configure(fg=color)


    def _toggle_bold(self):
        current_font = Font(font=self._get_current_text_area().cget("font"))
        current_weight = "bold" if current_font.actual("weight") != "bold" else "normal"
        
        new_font = Font(family=current_font.actual("family"), size=current_font.actual("size"), weight=current_weight)
        
        selected_text = self._get_current_text_area().tag_ranges("sel")
        
        if selected_text:
            self._get_current_text_area().tag_add("bold", selected_text[0], selected_text[1])
            self._get_current_text_area().tag_configure("bold", font=new_font)
        else:
            self._get_current_text_area().configure(font=new_font)


    def _toggle_italic(self):
        current_font = Font(font=self._get_current_text_area().cget("font"))
        current_slant = "italic" if current_font.actual("slant") != "italic" else "roman"
        
        new_font = Font(family=current_font.actual("family"), size=current_font.actual("size"), slant=current_slant)
        
        selected_text = self._get_current_text_area().tag_ranges("sel")
        
        if selected_text:
            self._get_current_text_area().tag_add("italic", selected_text[0], selected_text[1])
            self._get_current_text_area().tag_configure("italic", font=new_font)
        else:
            self._get_current_text_area().configure(font=new_font)

    def _toggle_underline(self):
        current_font = Font(font=self._get_current_text_area().cget("font"))
        current_underline = not current_font["underline"]
        selected_text = self._get_current_text_area().tag_ranges("sel")
        if selected_text:
            self._get_current_text_area().tag_add("underline", selected_text[0], selected_text[1])
            self._get_current_text_area().tag_configure("underline", underline=current_underline)
        else:
            current_font["underline"] = current_underline
            self._get_current_text_area().configure(font=current_font)

    def _toggle_strike(self):
        current_font = Font(font=self._get_current_text_area().cget("font"))
        current_overstrike = not current_font["overstrike"]
        selected_text = self._get_current_text_area().tag_ranges("sel")
        if selected_text:
            self._get_current_text_area().tag_add("strike", selected_text[0], selected_text[1])
            self._get_current_text_area().tag_configure("strike", overstrike=current_overstrike)
        else:
            current_font["overstrike"] = current_overstrike
            self._get_current_text_area().configure(font=current_font)

    def _align_left(self):
        self._get_current_text_area().tag_configure("left", justify="left")
        self._get_current_text_area().tag_add("left", "sel.first", "sel.last")

    def _align_center(self):
        self._get_current_text_area().tag_configure("center", justify="center")
        self._get_current_text_area().tag_add("center", "sel.first", "sel.last")

    def _align_right(self):
        self._get_current_text_area().tag_configure("right", justify="right")
        self._get_current_text_area().tag_add("right", "sel.first", "sel.last")

    def _clear_text(self):
        self._get_current_text_area().delete("1.0", "end")

    def _save_text(self):
        file_path = askstring("Save", "Enter file name:", parent=self.notebook)
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
