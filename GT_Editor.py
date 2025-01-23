from GT_imports import *
from datetime import datetime
from spellchecker import SpellChecker

class Font_Text_Editor:
    def __init__(self, text_area):
        self.text_area = text_area
    
    def _toggle_Highlight_Box(self):
        text_area = self._get_current_text_area()
        selected_text = text_area.tag_ranges("sel")
        
        if selected_text:
            if "Highlight_Box" in text_area.tag_names("sel.first"):
                text_area.tag_remove("Highlight_Box", selected_text[0], selected_text[1])
            else:
                text_area.tag_add("Highlight_Box", selected_text[0], selected_text[1])

            text_area.tag_configure(
                "Highlight_Box",
                background="yellow",  
                relief="solid",      
                borderwidth=2,       
                lmargin1=5,        
                rmargin=5,           
                foreground="black",  
            )
            text_area.focus_set()
    
    def _find_and_replace(self):
        find_replace_win = tk.Toplevel()
        find_replace_win.title("Find and Replace")
        find_replace_win.iconbitmap("Assets/FaceLogo.ico")
       
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
         

        def find_next():
            text_area = self._get_current_text_area()
            text_area.tag_remove("highlight", "1.0", "end")
            find_text = find_entry.get()
            if not find_text:
                return
            start_pos = text_area.index(tk.INSERT)  
            pos = text_area.search(find_text, start_pos, stopindex="end")
            if pos:
                end_pos = f"{pos}+{len(find_text)}c"
                text_area.tag_add("highlight", pos, end_pos)
                text_area.tag_configure("highlight", background="yellow")
                text_area.mark_set(tk.INSERT, end_pos) 
                text_area.see(tk.INSERT)
            else:
                messagebox.showinfo("Find", "No more occurrences found.")

        def highlight_all():
            text_area = self._get_current_text_area()
            text_area.tag_remove("highlight", "1.0", "end")
            find_text = find_entry.get()
            if not find_text:
                return
            start_pos = "1.0"
            while True:
                start_pos = text_area.search(find_text, start_pos, stopindex="end")
                if not start_pos:
                    break
                end_pos = f"{start_pos}+{len(find_text)}c"
                text_area.tag_add("highlight", start_pos, end_pos)
                start_pos = end_pos
            text_area.tag_configure("highlight", background="yellow")

        ttk.Button(find_replace_win, text="Replace All", command=perform_replace).grid(row=2, column=0, padx=5, pady=5)
        ttk.Button(find_replace_win, text="Find Next", command=find_next).grid(row=2, column=1, padx=5, pady=5)
        ttk.Button(find_replace_win, text="Highlight All", command=highlight_all).grid(row=3, column=0, columnspan=2, pady=10)

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
    
    def _insert_datetime(self):
        text_area = self._get_current_text_area() 
        current_datetime = datetime.now().strftime("%Y-%m-%d %I:%M:%S %p")  
        text_area.insert(tk.INSERT, current_datetime)  

    def _insert_bullets(self):
        text_area = self._get_current_text_area()
        selected_text = text_area.tag_ranges("sel")
        if selected_text:
            selected_content = text_area.get(selected_text[0], selected_text[1])
            bulleted_content = '\n'.join(['• ' + line for line in selected_content.split('\n')])
            text_area.delete(selected_text[0], selected_text[1])
            text_area.insert(selected_text[0], bulleted_content)

    def _insert_numbered_list(self):
        text_area = self._get_current_text_area()
        selected_text = text_area.tag_ranges("sel")
        if selected_text:
            selected_content = text_area.get(selected_text[0], selected_text[1])
            numbered_content = '\n'.join([f"{i+1}. {line}" for i, line in enumerate(selected_content.split('\n'))])
            text_area.delete(selected_text[0], selected_text[1])
            text_area.insert(selected_text[0], numbered_content)
    
    def _spell_check(self):
        spell = SpellChecker()

        text_area = self._get_current_text_area()
        content = text_area.get("1.0", "end-1c")
    
        words = content.split()
        misspelled = spell.unknown(words)
        
        text_area.tag_remove("misspelled", "1.0", "end")

        for word in misspelled:
            start_idx = text_area.search(word, "1.0", stopindex="end")
            while start_idx:
                end_idx = f"{start_idx}+{len(word)}c"
                text_area.tag_add("misspelled", start_idx, end_idx)
                text_area.tag_configure("misspelled", foreground="red", underline=True)
                text_area.tag_bind("misspelled", "<Button-3>", lambda event, word=word: self._show_spell_suggestions(event, word))
                start_idx = text_area.search(word, end_idx, stopindex="end")

        if misspelled:
            messagebox.showinfo("Spell Check", f"Misspelled words: {', '.join(misspelled)}")
        else:
            messagebox.showinfo("Spell Check", "No spelling errors found.")
    def _show_spell_suggestions(self, event, word):
        spell = SpellChecker()

        suggestions = spell.candidates(word)

        context_menu = tk.Menu(self._get_current_text_area(), tearoff=0)
        
        for suggestion in suggestions:
            context_menu.add_command(label=suggestion, command=lambda word=word, suggestion=suggestion: self._replace_word(word, suggestion))
        
        context_menu.post(event.x_root, event.y_root)

    def _replace_word(self, word, suggestion):
        text_area = self._get_current_text_area()
        
        start_idx = text_area.search(word, "1.0", stopindex="end")
        
        while start_idx:
            end_idx = f"{start_idx}+{len(word)}c"
            
            text_area.delete(start_idx, end_idx)
            text_area.insert(start_idx, suggestion)
            
            start_idx = text_area.search(word, end_idx, stopindex="end")
