import customtkinter as ctk
from components.common.CommonButton import CommonButton


class SaveButton(CommonButton):
    def __init__(self, master):
        super().__init__(master, text="Save Text", command=self._save_dialogue)

    def _save_dialogue(self):
        file_path = ctk.filedialog.asksaveasfilename(
            defaultextension=".txt",
            title="Save File",
            filetypes=[("All files", "*.*")],
        )
        if file_path:
            with open(file_path, "w") as file:
                file.write("Text to save")  # TODO - save actual text from text box
