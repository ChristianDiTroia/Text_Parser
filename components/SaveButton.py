import customtkinter as ctk
import tkinter as tk
from PIL import Image
from AppContext import AppContext
from components.common.CommonButton import CommonButton


class SaveButton(CommonButton):
    def __init__(self, master):
        self.save_image = ctk.CTkImage(Image.open("./icons/save.png"), size=(64, 64))
        super().__init__(
            master,
            text="",
            command=_save_dialogue,
            image=self.save_image,
            fg_color="transparent",
            width=64,
            height=64,
        )


def _save_dialogue():
    file_path = ctk.filedialog.asksaveasfilename(
        defaultextension=".txt",
        title="Save File",  # TODO - support pdf and docx
    )
    if file_path:
        try:
            with open(file_path, "w", encoding="utf-8") as save_file:
                save_file.write(AppContext.var("result_var").get_value())
                AppContext.var("save_file").set_value(file_path)
        except Exception as e:
            print(f"Failed to save file: {file_path}\nException: {e}")
            tk.messagebox.showwarning(
                "Save failed", f"Failed to save file: {file_path}"
            )
