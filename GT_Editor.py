from GT_imports import *
import io

class Font_Text_Editor:
    def __init__(self, text_area):
        self.text_area = text_area
    
#! ------------------------------------------------------------------------------------------------    
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
#! ------------------------------------------------------------------------------------------------    
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
#! ------------------------------------------------------------------------------------------------
    def _undo(self):
        self._get_current_text_area().edit_undo()

    def _redo(self):
        self._get_current_text_area().edit_redo()
#! ------------------------------------------------------------------------------------------------
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
#! ------------------------------------------------------------------------------------------------    
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
#! ------------------------------------------------------------------------------------------------    
    def _insert_hyperlink(self):
        """Insert a hyperlink in the current text area."""
        text_area = self._get_current_text_area()
        url = simpledialog.askstring("Insert Hyperlink", "Enter URL:")
        if url:
            selected_text = text_area.tag_ranges("sel")
            if selected_text:
                text_area.tag_add("hyperlink", selected_text[0], selected_text[1])
                text_area.tag_configure("hyperlink", foreground="blue", underline=True)

                def open_url(event, link=url):
                    webbrowser.open(link)

                text_area.tag_bind("hyperlink", "<Button-1>", open_url)
    
#! ------------------------------------------------------------------------------------------------
    
    def _dynamic_word_count(self, event=None):
        text_area = self._get_current_text_area()
        content = text_area.get("1.0", "end-1c")  
        words = content.split()  
        word_count = len(words) 

        self.status_label.config(text=f"Words Type →{word_count}")

#! ------------------------------------------------------------------------------------------------
    
    def _speech_to_text(self):
        recognizer = sr.Recognizer()

        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source)  # Reduce noise
            print("Listening... Speak now.")
            try:
                audio = recognizer.listen(source)
                command = recognizer.recognize_google(audio).lower()
                print(f"You said: {command}")
                text_area = self._get_current_text_area()
                
                if "bold" in command:
                    self._apply_bold_to_highlighted_text()
                elif "italic" in command:
                    self._toggle_italic()
                elif "load file" in command:
                    self._load_file()
                elif "underline" in command:
                    self._toggle_underline()
                elif "strike" in command:
                    self._toggle_strike()
                elif "highlight" in command:
                    keyword = command.replace("highlight", "").strip()
                    if keyword:
                        self._highlight_text(keyword)
                    else:
                        print("No keyword specified for highlighting.")
                elif "clear highlight" in command:
                    self._clear_highlight()  
                elif "align left" in command:
                    self._align_left()
                elif "align center" in command:
                    self._align_center()
                elif "align right" in command:
                    self._align_right()
                else:
                    text_area.insert(tk.INSERT, command)

            except sr.UnknownValueError:
                print("Sorry, I could not understand what you said.")
            except sr.RequestError as e:
                print(f"Could not request results from Google Speech Recognition service; {e}")

    
    def _apply_bold_to_highlighted_text(self):
        text_area = self._get_current_text_area()
        try:
            selected_text = text_area.get(tk.SEL_FIRST, tk.SEL_LAST)
            if selected_text:
                text_area.tag_configure("bold", font=("Helvetica", 12, "bold"))
                text_area.tag_add("bold", tk.SEL_FIRST, tk.SEL_LAST)
                print("Bold applied to selected text.")
            else:
                print("No text selected for bold formatting.")
        except tk.TclError:
            print("No text selected for bold formatting.")
    

    def _load_file(self):
        """Load a file into the text area."""
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file_path:
            with open(file_path, "r") as file:
                content = file.read()
                text_area = self._get_current_text_area()
                text_area.delete("1.0", "end")
                text_area.insert("1.0", content)
            print("File loaded successfully.")

    
    def _save_file(self):
        """Save the current text area content to a file."""
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
        if file_path:
            with open(file_path, "w") as file:
                text_area = self._get_current_text_area()
                content = text_area.get("1.0", "end-1c")
                file.write(content)
            print("File saved successfully.")

    
    def _highlight_text(self, keyword):
        """Highlight all occurrences of a keyword in the text area."""
        text_area = self._get_current_text_area()
        text_area.tag_remove("highlight", "1.0", "end")  
        start_pos = "1.0"
        while True:
            start_pos = text_area.search(keyword, start_pos, stopindex="end")
            if not start_pos:
                break
            end_pos = f"{start_pos}+{len(keyword)}c"
            text_area.tag_add("highlight", start_pos, end_pos)
            text_area.tag_configure("highlight", background="yellow", foreground="black")
            start_pos = end_pos
        print(f"Highlighted all occurrences of '{keyword}'.")
    
#! ------------------------------------------------------------------------------------------------    
    def _add_clock(self):
        """Create a popup window with an enhanced analog clock."""
        clock_popup = tk.Toplevel()
        clock_popup.title("Clocky")
        clock_popup.geometry("250x250")  
        clock_popup.resizable(False, False)

        self.analog_clock_canvas = tk.Canvas(clock_popup, width=200, height=200, bg="black", highlightthickness=0)
        self.analog_clock_canvas.pack(padx=10, pady=10)

        self._draw_clock_face()

        self._update_clock()

    def _draw_clock_face(self):
        """Draw the static elements of the clock face with enhanced design."""
        radius = 90
        center = 100, 100  
        self.analog_clock_canvas.create_oval(10, 10, 190, 190, outline="#333", width=3)  

        self.analog_clock_canvas.create_oval(15, 15, 185, 185, fill="#eea284", outline="#c0d6e4", width=1)

        for hour in range(1, 13):
            angle = math.radians(hour * 30)
            x = center[0] + radius * 0.75 * math.cos(angle - math.pi / 2)
            y = center[1] + radius * 0.75 * math.sin(angle - math.pi / 2)
            self.analog_clock_canvas.create_text(x, y, text=str(hour), font=("Arial", 14, "bold"), fill="#333")

        for tick in range(60):
            angle = math.radians(tick * 6) 
            outer_x = center[0] + radius * math.cos(angle - math.pi / 2)
            outer_y = center[1] + radius * math.sin(angle - math.pi / 2)
            inner_x = center[0] + (radius - 5 if tick % 5 == 0 else radius - 2) * math.cos(angle - math.pi / 2)
            inner_y = center[1] + (radius - 5 if tick % 5 == 0 else radius - 2) * math.sin(angle - math.pi / 2)
            color = "#555" if tick % 5 == 0 else "#aaa"
            self.analog_clock_canvas.create_line(outer_x, outer_y, inner_x, inner_y, fill=color, width=1)

        self.analog_clock_canvas.create_oval(95, 95, 105, 105, fill="#333", outline="#111")

        self.left_eye = self.analog_clock_canvas.create_oval(70, 70, 90, 90, fill="white", outline="#333")  # Left eye
        self.right_eye = self.analog_clock_canvas.create_oval(110, 70, 130, 90, fill="white", outline="#333")  # Right eye

        self.left_pupil = self.analog_clock_canvas.create_oval(78, 78, 82, 82, fill="black")  # Left pupil
        self.right_pupil = self.analog_clock_canvas.create_oval(118, 78, 122, 82, fill="black")  # Right pupil
        self.analog_clock_canvas.create_arc(65, 90, 135, 140, start=200, extent=140, style="arc", outline="#333", width=2)

        self._update_googly_eyes()

    def _update_googly_eyes(self):
        """Update the position of the googly eyes dynamically."""

        def move_pupil(eye_center, pupil_radius, eye_radius):
            max_offset = eye_radius - pupil_radius
            offset_x = random.randint(-max_offset, max_offset)
            offset_y = random.randint(-max_offset, max_offset)
            return eye_center[0] + offset_x, eye_center[1] + offset_y

        left_eye_center = (80, 80)  
        right_eye_center = (120, 80) 
        pupil_radius = 4
        eye_radius = 10
        left_pupil_pos = move_pupil(left_eye_center, pupil_radius, eye_radius)
        right_pupil_pos = move_pupil(right_eye_center, pupil_radius, eye_radius)

        self.analog_clock_canvas.coords(
            self.left_pupil,
            left_pupil_pos[0] - pupil_radius,
            left_pupil_pos[1] - pupil_radius,
            left_pupil_pos[0] + pupil_radius,
            left_pupil_pos[1] + pupil_radius,
        )

        self.analog_clock_canvas.coords(
            self.right_pupil,
            right_pupil_pos[0] - pupil_radius,
            right_pupil_pos[1] - pupil_radius,
            right_pupil_pos[0] + pupil_radius,
            right_pupil_pos[1] + pupil_radius,
        )

        self.analog_clock_canvas.after(200, self._update_googly_eyes)


    def _update_clock(self):
        """Update the analog clock hands with cooler visuals."""
        self.analog_clock_canvas.delete("hands")
        self.analog_clock_canvas.delete("hands_shadow")

        center = 100, 100
        radius = 90
        current_time = datetime.now()
        hour, minute, second = current_time.hour % 12, current_time.minute, current_time.second

        hour_angle = math.radians((hour + minute / 60) * 30)
        hour_x = center[0] + radius * 0.5 * math.cos(hour_angle - math.pi / 2)
        hour_y = center[1] + radius * 0.5 * math.sin(hour_angle - math.pi / 2)
        self.analog_clock_canvas.create_line(center[0], center[1], hour_x, hour_y, fill="#333", width=6, tags="hands")

        minute_angle = math.radians((minute + second / 60) * 6)
        minute_x = center[0] + radius * 0.7 * math.cos(minute_angle - math.pi / 2)
        minute_y = center[1] + radius * 0.7 * math.sin(minute_angle - math.pi / 2)
        self.analog_clock_canvas.create_line(center[0], center[1], minute_x, minute_y, fill="#5555ff", width=4, tags="hands")

        second_angle = math.radians(second * 6)
        second_x = center[0] + radius * 0.85 * math.cos(second_angle - math.pi / 2)
        second_y = center[1] + radius * 0.85 * math.sin(second_angle - math.pi / 2)
        self.analog_clock_canvas.create_line(center[0], center[1], second_x, second_y, fill="#ff5555", width=2, tags="hands")

        shadow_offset = 1
        self.analog_clock_canvas.create_line(center[0] + shadow_offset, center[1] + shadow_offset, hour_x, hour_y,
                                            fill="#888", width=6, tags="hands_shadow")
        self.analog_clock_canvas.create_line(center[0] + shadow_offset, center[1] + shadow_offset, minute_x, minute_y,
                                            fill="#aaa", width=4, tags="hands_shadow")
        self.analog_clock_canvas.create_line(center[0] + shadow_offset, center[1] + shadow_offset, second_x, second_y,
                                            fill="#faa", width=2, tags="hands_shadow")

        self.analog_clock_canvas.after(1000, self._update_clock)
#! ------------------------------------------------------------------------------------------------
 
    def _open_freehand_drawing(self):
        """Open a freehand drawing tool."""
        drawing_window = tk.Toplevel()
        drawing_window.title("Freehand Drawing")
        drawing_window.geometry("800x600")
        drawing_window.resizable(True, True)

        drawing_canvas = tk.Canvas(drawing_window, bg="white", width=800, height=600)
        drawing_canvas.pack(fill=tk.BOTH, expand=True)

        canvas_image = Image.new("RGB", (800, 600), color="white")
        img_draw = ImageDraw.Draw(canvas_image)

        self.drawing_tool_active = False
        current_color = "black" 

        def start_drawing(event):
            """Start freehand drawing on the canvas."""
            self.drawing_tool_active = True
            drawing_canvas.old_coords = (event.x, event.y)

        def draw_on_canvas(event):
            """Draw on the canvas as the mouse moves."""
            if self.drawing_tool_active:
                x, y = event.x, event.y
                old_coords = drawing_canvas.old_coords
                drawing_canvas.create_line(old_coords[0], old_coords[1], x, y, fill=current_color, width=2, capstyle=tk.ROUND, smooth=True)
                img_draw.line([old_coords[0], old_coords[1], x, y], fill=current_color, width=2)
                drawing_canvas.old_coords = (x, y)

        def stop_drawing(event):
            """Stop drawing."""
            self.drawing_tool_active = False
            drawing_canvas.old_coords = None

        def save_drawing():
            """Save the current drawing on the canvas to a PNG file."""
            file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("All files", "*.*")])
            if file_path:
                canvas_image.save(file_path)

        def load_drawing():
            """Load a saved drawing from a PNG file."""
            file_path = filedialog.askopenfilename(filetypes=[("PNG files", "*.png"), ("All files", "*.*")])
            if file_path:
                loaded_image = Image.open(file_path)
                canvas_image.paste(loaded_image, (0, 0))
                photo = ImageTk.PhotoImage(loaded_image)
                drawing_canvas.create_image(0, 0, anchor=tk.NW, image=photo)
                drawing_canvas.image = photo  
                img_draw = ImageDraw.Draw(canvas_image)
                img_draw.bitmap((0, 0), loaded_image.convert("1"), fill="black")

        def choose_color():
            """Open a color picker and update the drawing color."""
            nonlocal current_color  
            color_code = colorchooser.askcolor()[1]  
            if color_code:
                current_color = color_code

        def clear_canvas():
            """Clear the canvas and reset the image."""
            drawing_canvas.delete("all")
            canvas_image.paste(Image.new("RGB", (800, 600), color="white"), (0, 0))  

        def show_context_menu(event):
            """Show context menu on right-click."""
            context_menu.post(event.x_root, event.y_root)

        context_menu = tk.Menu(drawing_window, tearoff=0)
        context_menu.add_command(label="Save Drawing", command=save_drawing)
        context_menu.add_command(label="Load Drawing", command=load_drawing)
        context_menu.add_command(label="Choose Color", command=choose_color)
        context_menu.add_command(label="Clear Canvas", command=clear_canvas) 

        drawing_canvas.bind("<Button-3>", show_context_menu)
        drawing_canvas.bind("<ButtonPress-1>", start_drawing)
        drawing_canvas.bind("<B1-Motion>", draw_on_canvas)
        drawing_canvas.bind("<ButtonRelease-1>", stop_drawing)

#! ------------------------------------------------------------------------------------------------
 
    def _open_terminal(self):
        terminal_window = tk.Toplevel()
        terminal_window.title("Terminal")
        terminal_window.geometry("800x600")
        terminal_window.resizable(True, True)

        text_color = "green"
        bg_color = "black"

        terminal_output = tk.Text(
            terminal_window, wrap=tk.WORD, state=tk.DISABLED, fg=text_color, bg=bg_color
        )
        terminal_output.pack(expand=True, fill=tk.BOTH)

        terminal_input = ttk.Entry(terminal_window, width=80)
        terminal_input.pack(fill=tk.X, padx=5, pady=5)

        def set_color(target, color):
            """Set the terminal's text or background color."""
            nonlocal text_color, bg_color
            if target == "text":
                text_color = color
                terminal_output.config(fg=color)
            elif target == "bg":
                bg_color = color
                terminal_output.config(bg=color)

        def execute_command(event=None):
            """Execute the entered command."""
            command = terminal_input.get()
            if command.strip(): 
                terminal_output.config(state=tk.NORMAL)
                terminal_output.insert(tk.END, f"$Terminal >> {command}\n", "user_input")
                terminal_output.config(state=tk.DISABLED)
                terminal_input.delete(0, tk.END)

                if command.startswith("set textcolor"):
                    _, _, color = command.split(maxsplit=2)
                    set_color("text", color)
                    return
                elif command.startswith("set bgcolor"):
                    _, _, color = command.split(maxsplit=2)
                    set_color("bg", color)
                    return

                shell_command = ["cmd.exe", "/c", command]
                process = subprocess.Popen(
                    shell_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
                )
                stdout, stderr = process.communicate()

                if stdout:
                    terminal_output.config(state=tk.NORMAL)
                    terminal_output.insert(tk.END, stdout)
                    terminal_output.config(state=tk.DISABLED)

                if stderr:
                    terminal_output.config(state=tk.NORMAL)
                    terminal_output.insert(tk.END, f"Error: {stderr}")
                    terminal_output.config(state=tk.DISABLED)

        terminal_input.bind("<Return>", execute_command)
        terminal_input.focus_set()
#! ------------------------------------------------------------------------------------------------
 
    def _toggle_border(self):
        text_area = self._get_current_text_area() 
        selected_text = text_area.tag_ranges("sel")

        if selected_text:
            paragraph_start = text_area.index(f"{selected_text [0]} linestart")
            paragraph_end = text_area.index(f"{selected_text [1]} lineend") 

            if "paragraph_border" in  text_area.tag_names(paragraph_start):
                text_area.tag_remove("paragraph_border", paragraph_start, paragraph_end) 
            else: 
                text_area.tag_add("paragraph_border", paragraph_start, paragraph_end)

            text_area.tag_configure("paragraph_border", relief="sunken" , borderwidth=5 , foreground="#00ff00")
            text_area.focus_set()

#! ------------------------------------------------------------------------------------------------
 
    def _add_calculator(self):
        calculator_popup = tk.Toplevel()
        calculator_popup.title("Calculator")
        calculator_popup.geometry("380x510")
        calculator_popup.resizable(False, False)
        calculator_popup.config(bg="#1a1a1a") 
        result = tk.Entry(calculator_popup, width=16, font=("Courier New", 24), bd=5, relief="sunken", justify="right", bg="#111", fg="lime")
        result.grid(row=0, column=0, columnspan=4, pady=10)

        def on_button_click(value):
            current = result.get()
            if value == "=":
                try:
                    result.delete(0, tk.END)
                    result.insert(tk.END, str(eval(current)))
                except Exception:
                    result.delete(0, tk.END)
                    result.insert(tk.END, "Error")
            else:
                result.insert(tk.END, value)

        def clear_input():
            result.delete(0, tk.END)

        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3)
        ]

        for (text, row, col) in buttons:
            button = tk.Button(calculator_popup, text=text, width=5, height=2, font=("Courier New", 18), bg="#222", fg="cyan", relief="flat", 
                            activebackground="#555", activeforeground="yellow", bd=3, highlightthickness=1, 
                            highlightbackground="#00ff00", command=lambda t=text: on_button_click(t))
            button.grid(row=row, column=col, padx=5, pady=5)

        clear_button = tk.Button(calculator_popup, text='C', width=5, height=2, font=("Courier New", 18), bg="#222", fg="cyan", relief="flat", 
                                activebackground="#c0392b", activeforeground="white", bd=3, highlightthickness=1, 
                                highlightbackground="#ff0000", command=clear_input)
        clear_button.grid(row=5, column=0, columnspan=4, pady=10)

        for widget in calculator_popup.winfo_children():
            if isinstance(widget, tk.Button):
                widget.bind("<Enter>", lambda e, b=widget: b.config(bg="#666", fg="lime"))
                widget.bind("<Leave>", lambda e, b=widget: b.config(bg="#222", fg="cyan"))

        def glow_entry():
            current_fg = result.cget("fg")
            new_fg = "lime" if current_fg == "red" else "red"
            result.config(fg=new_fg)
            result.after(500, glow_entry)
        glow_entry()
        calculator_popup.mainloop()

                
