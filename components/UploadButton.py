import threading
import customtkinter as ctk
import tkinter as tk
from AppContext import AppContext
from TextParser import TextParser
from components.ProgressWindow import ProgressWindow
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

            file_name = file_path.split(r"/")[-1]
            progress_window = ProgressWindow(
                master=AppContext.var("root").get_value(),
                title="Parsing Text",
                message=f"Parsing {file_name}\n\nLarge files may take some time.",
            )
            self.after(  # workaround for bug where CTKTopLevel drops itself in lift order
                500,
                func=lambda: progress_window.lift(AppContext.var("root").get_value()),
            )

            AppContext.var("text_parser").set_value(text_parser)
            _async_parse_text(
                text_parser,
                start_page=3,
                callback=lambda: progress_window.destroy(),
            )

            # TODO popup another window here asking for start page and end page,


def _async_parse_text(text_parser, start_page=None, end_page=None, callback=None):
    def job():
        try:
            text_parser.parse_text(start_page, end_page)
        except Exception:
            AppContext.var("text_parser").set_value(None)
            tk.messagebox.showwarning("Error", f"Unable to parse the selected file")
        finally:
            if callback:
                callback()

    thread = threading.Thread(target=job, daemon=True)
    thread.start()
