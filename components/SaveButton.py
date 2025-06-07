import customtkinter as ctk
from AppContext import AppContext
from components.common.CommonButton import CommonButton


class SaveButton(CommonButton):
    def __init__(self, master):
        super().__init__(master, text="Save", command=self._save_dialogue)

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
