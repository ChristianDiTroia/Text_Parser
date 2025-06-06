import threading
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
            except (ValueError, FileNotFoundError, IOError) as e:
                tk.messagebox.showwarning("Cannot read file", str(e))
                return

            AppContext.var("text_parser").set_value(text_parser)
            async_parse_text(text_parser, start_page=3)

        # TODO popup another window here asking for start page and end page,
        # maybe display progress bar and the PDF preview


def async_parse_text(text_parser, start_page=None, end_page=None):
    def job():
        try:
            text_parser.parse_text(start_page, end_page)
        except Exception:
            AppContext.var("text_parser").set_value(None)
            tk.messagebox.showwarning("Error", f"Unable to parse the selected file")

    thread = threading.Thread(target=job, daemon=True)
    thread.start()
