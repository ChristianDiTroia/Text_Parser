import threading
import customtkinter as ctk
import tkinter as tk
from PIL import Image
from AppContext import AppContext
from TextParser import TextParser
from components.ProgressWindow import ProgressWindow
from components.common.CommonButton import CommonButton


class UploadButton(CommonButton):
    def __init__(self, master):
        working_dir = AppContext.var("working_dir").get_value()
        self.upload_image = ctk.CTkImage(
            Image.open(working_dir / "./icons/upload.png"), size=(48, 48)
        )
        super().__init__(
            master,
            text="",
            command=self.__upload_dialogue,
            image=self.upload_image,
            fg_color="transparent",
            width=48,
            height=48,
        )

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
            AppContext.var("loading").set_value(f'Parsing "{file_name}"...')

            def cleanup():
                self.configure(state="normal")
                AppContext.var("loading").set_value("")

            async_parse_text(
                text_parser,
                callback=cleanup,
            )
        else:
            self.configure(state="normal")

            # TODO popup another window here asking for start page and end page,


def async_parse_text(text_parser, start_page=1, end_page=None, callback=None):
    def job():
        failed = False
        try:
            text_parser.parse_text(start_page, end_page)
            AppContext.var("text_parser").set_value(text_parser)
        except Exception as e:
            failed = True
            AppContext.var("text_parser").set_value(None)
            print(e)
        finally:
            if callback:
                callback()
            if failed:
                tk.messagebox.showwarning("Error", "Unable to parse the selected file")

    threading.Thread(name="_async_parse_text", target=job, daemon=True).start()
