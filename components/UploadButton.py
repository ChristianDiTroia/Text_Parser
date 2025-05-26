import customtkinter as ctk
import tkinter as tk

from TextParser import TextParser
from components.common.CommonButton import CommonButton


class UploadButton(CommonButton):
    def __init__(self, master, text_parser: TextParser, text_var: tk.StringVar):
        super().__init__(master, text="Upload Text", command=self._upload_dialogue)
        self.text_parser = text_parser
        self.text_var = text_var

    def _upload_dialogue(self):
        file_path = ctk.filedialog.askopenfilename(
            title="Select a file",
            filetypes=(("All files", ("*.txt", "*.docx", "*.pdf")),),
        )
        if file_path:
            try:
                self.text_parser = TextParser(file_path)
                self.text_parser.parse_text(start_page=3, end_page=10)
                self.text_var.set("\n".join(self.text_parser.get_next_lines(10)))
            except Exception as e:
                tk.messagebox.showerror("Error", f"Failed to read the file: {e}")
