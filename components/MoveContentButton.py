import customtkinter as ctk
from PIL import Image
from AppContext import AppContext
from components.common.CommonButton import CommonButton


class MoveContentButton(CommonButton):
    def __init__(self, master):
        working_dir = AppContext.var("working_dir").get_value()
        self.right_arrow = ctk.CTkImage(
            Image.open(working_dir / "./icons/right-arrow.png"), size=(48, 48)
        )
        super().__init__(
            master,
            text="",
            command=self._move_text,
            image=self.right_arrow,
            fg_color="transparent",
            width=48,
            height=48,
        )

    def _move_text(self):
        document_text = AppContext.var("text_var").get_value()
        current_result = AppContext.var("result_var").get_value()
        document_text = str(document_text) if document_text else ""
        current_result = str(current_result) if current_result else ""
        if document_text and current_result:
            document_text = "\n" + document_text
        AppContext.var("result_var").set_value(current_result + document_text)
