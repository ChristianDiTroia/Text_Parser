import threading
import customtkinter as ctk
import tkinter as tk
from AppContext import AppContext
from TextParser import TextParser
from components.ProgressWindow import ProgressWindow
from components.common.CommonButton import CommonButton


class UploadButton(CommonButton):
    def __init__(self, master):
        super().__init__(master, text="Upload", command=self.__upload_dialogue)

    def __upload_dialogue(self):
        self.configure(state="disabled")

        file_path = ctk.filedialog.askopenfilename(
            title="Select a file",
            filetypes=(
                ("All files", "*.*"),
                ("Text File", "*.txt"),
                ("Word Documents", "*.docx"),
                ("PDF File", "*.pdf"),
            ),
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
                message=f'Parsing "{file_name}"\n\nLarge files may take some time.',
            )
            progress_window.after(  # workaround for bug where CTKTopLevel drops itself in lift order
                500,
                func=lambda: progress_window.lift(AppContext.var("root").get_value()),
            )

            def cleanup():
                self.configure(state="normal")
                progress_window.destroy()

            _async_parse_text(
                text_parser,
                start_page=3,
                callback=cleanup,
            )
        else:
            self.configure(state="normal")

            # TODO popup another window here asking for start page and end page,


def _async_parse_text(text_parser, start_page=None, end_page=None, callback=None):
    def job():
        failed = False
        try:
            text_parser.parse_text(start_page, end_page)
            AppContext.var("text_parser").set_value(text_parser)
        except Exception as e:
            failed = True
            AppContext.var("text_parser").set_value(None)
        finally:
            if callback:
                callback()
            if failed:
                tk.messagebox.showwarning("Error", "Unable to parse the selected file")

    threading.Thread(name="_async_parse_text", target=job, daemon=True).start()
