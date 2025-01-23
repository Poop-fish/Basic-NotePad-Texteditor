from GT_imports import *

class TabManagement:
    def __init__(self , editor):
        self.tabs = []
        self.editor = editor
    
    def _update_bg_fg(self, mode):
        """Update background or foreground color of the current text area."""
        color = askcolor()[1]
        if color:
            current_text_area = self._get_current_text_area()
            if mode == 'bg':
                current_text_area.configure(bg=color)

    def create_tabbed_text_area(self, root):
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill=tk.BOTH, expand=True)
        self._new_tab()

    def _new_tab(self):
        frame = tk.Frame(self.notebook, bg=self.bg)

        line_numbers = tk.Text(frame, width=4, bg="gray", fg="black", state="disabled")
        line_numbers.pack(side=tk.LEFT, fill=tk.Y)

        text_area = tk.Text(frame, font=self.default_font, wrap="word", bg=self.bg, fg=self.fg, undo=True)

        text_area.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = ttk.Scrollbar(frame, command=text_area.yview)
        text_area.configure(yscrollcommand=lambda *args: self._on_scroll(line_numbers, text_area, *args))
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self._update_line_numbers(line_numbers, text_area)
        text_area.bind("<KeyRelease>", lambda event: self._update_line_numbers(line_numbers, text_area))
        text_area.bind("<MouseWheel>", lambda event: self._update_line_numbers(line_numbers, text_area))

        self.notebook.add(frame, text=f"Tab {len(self.tabs) + 1}")
        self.tabs.append(text_area)

    def _on_scroll(self, line_numbers, text_area, *args):
        """Sync scrolling between the text area and line numbers."""
        if args[0] == "moveto":
            text_area.yview_moveto(args[1])
            line_numbers.yview_moveto(args[1])
        elif args[0] == "scroll":
            text_area.yview_scroll(int(args[1]), args[2])
            line_numbers.yview_scroll(int(args[1]), args[2])

    def _update_line_numbers(self, line_numbers, text_area):
        font = text_area.cget("font")
        line_numbers.config(state="normal", font=font)
        line_numbers.delete("1.0", "end")
        current_lines = text_area.get("1.0", "end-1c").split("\n")
        line_numbers_content = "\n".join(str(i + 1) for i in range(len(current_lines)))
        line_numbers.insert("1.0", line_numbers_content)
        line_numbers.config(state="disabled")

    def _rename_tab(self):
        """Creates a new top-level window for renaming the tab pop up """
        def on_rename():
            new_name = entry.get().strip()
            if new_name:
                self.notebook.tab(current_tab, text=new_name)
                rename_window.destroy()
            else:
                messagebox.showwarning("Input Error", "Please enter a valid name.")

        current_tab = self.notebook.index(self.notebook.select())

        rename_window = tk.Toplevel()
        rename_window.title("Rename Tab")
        rename_window.geometry("200x150") 

        label = tk.Label(rename_window, text="Enter new tab name:")
        label.pack(pady=10)

        entry = tk.Entry(rename_window, width=30)
        entry.pack(pady=5)
        entry.insert(0, self.notebook.tab(current_tab, "text"))  #  \\ Set default text as current tab name

        rename_button = tk.Button(rename_window, text="Rename", command=on_rename)
        rename_button.pack(pady=5)

        cancel_button = tk.Button(rename_window, text="Cancel", command=rename_window.destroy)
        cancel_button.pack(pady=5)
        entry.focus()

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


#! ----------------------- END OF TAB MANAGEMENT ---------------------------------------------------  