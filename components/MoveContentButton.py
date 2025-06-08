import customtkinter as ctk
from PIL import Image
from components.common.CommonButton import CommonButton


class MoveContentButton(CommonButton):
    def __init__(self, master):
        self.right_arrow = ctk.CTkImage(
            Image.open("./icons/right-arrow.png"), size=(48, 48)
        )
        super().__init__(
            master,
            text="",
            command=None,
            image=self.right_arrow,
            fg_color="transparent",
            width=48,
            height=48,
        )
