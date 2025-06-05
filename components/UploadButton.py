import customtkinter as ctk
import tkinter as tk
from AppContext import AppContext
from TextParser import TextParser
from components.common.CommonButton import CommonButton


class UploadButton(CommonButton):
    def __init__(self, master):
        super().__init__(master, text="Upload Text", command=self._upload_dialogue)

    def _upload_dialogue(self):
        file_path = ctk.filedialog.askopenfilename(
            title="Select a file",
            filetypes=(("All files", ("*.txt", "*.docx", "*.pdf")),),
        )
        if file_path:
            try:
                text_parser = TextParser(file_path)
                text_parser.parse_text(start_page=3, end_page=10)
                AppContext.var("text_parser").set_value(text_parser)

                AppContext.var("text_var").set_value(
                    "\n".join(text_parser.get_next_lines(10))
                )
                # TODO create new window to show text read loading
                # possibly need to do this in another thread
                # alsooo definitely do not set the text here
            except IOError as e:
                tk.messagebox.showerror("Error", f"Failed to read the file: {e}")
