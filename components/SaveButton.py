import customtkinter as ctk
import tkinter as tk
import docx as wd
from PIL import Image
from AppContext import AppContext
from components.common.CommonButton import CommonButton


class SaveButton(CommonButton):
    def __init__(self, master):
        self.save_image = ctk.CTkImage(Image.open("./icons/save.png"), size=(48, 48))
        super().__init__(
            master,
            text="",
            command=_save_dialogue,
            image=self.save_image,
            fg_color="transparent",
            width=48,
            height=48,
        )


def _save_dialogue():
    file_path = ctk.filedialog.asksaveasfilename(
        defaultextension=".txt",
        title="Save File",
        filetypes=(
            ("Text File", "*.txt"),
            ("Word Documents", "*.docx"),
        ),
        # TODO - support saving as pdf
    )
    if file_path:
        try:
            save_file(file_path)
        except Exception as e:
            print(f"Failed to save file: {file_path}\nException: {e}")
            tk.messagebox.showwarning(
                "Save failed", f"Failed to save file: {file_path}"
            )


def save_file(file_path: str):
    file_extension = file_path.split(r".")[-1].lower()
    content_to_save = AppContext.var("result_var").get_value()
    if file_extension == "txt":
        with open(file_path, "w", encoding="utf-8") as save_file:
            save_file.write(content_to_save)
    elif file_extension == "docx":
        docx = wd.Document()
        docx.add_paragraph(content_to_save)
        docx.save(file_path)
    else:
        raise ValueError(f"Unable to save file type: {file_extension}")
    AppContext.var("save_file").set_value(file_path)
