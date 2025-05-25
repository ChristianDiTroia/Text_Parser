import customtkinter as ctk
from components.common.CommonButton import CommonButton


class UploadButton(CommonButton):
    def __init__(self, master):
        super().__init__(master, text="Upload Text", command=self._upload_dialogue)

    def _upload_dialogue(self) -> str:
        file_path = ctk.filedialog.askopenfilename(
            title="Select a file",
            filetypes=(("All files", ("*.txt", "*.docx", "*.pdf")),),
        )
        if file_path:
            print(f"File selected: {file_path}")
            # TODO - take the file and process it as a text manipulator object then display it
