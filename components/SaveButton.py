import customtkinter as ctk
from PIL import Image
from AppContext import AppContext
from components.common.CommonButton import CommonButton


class SaveButton(CommonButton):
    def __init__(self, master):
        self.save_image = ctk.CTkImage(Image.open("./icons/save.png"), size=(64, 64))
        super().__init__(
            master,
            text="",
            command=self._save_dialogue,
            image=self.save_image,
            fg_color="transparent",
            width=64,
            height=64,
        )

    def _save_dialogue(self):
        file_path = ctk.filedialog.asksaveasfilename(
            defaultextension=".txt",
            title="Save File",  # TODO - support pdf and docx
        )
        if file_path:
            print(file_path)
            try:
                with open(file_path, "w") as save_file:
                    save_file.write(AppContext.var("result_var").get_value())
            except Exception as e:
                print(f"Failed to save file: {file_path}")
            AppContext.var("save_file").set_value(file_path)
