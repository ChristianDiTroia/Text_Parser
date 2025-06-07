import customtkinter as Ctk


class CommonOptionMenu(Ctk.CTkOptionMenu):
    def __init__(
        self,
        master,
        values=["Default"],
        width=100,
        height=28,
        corner_radius=16,
        bg_color="transparent",
        fg_color=None,
        text_color=None,
        font=("Times New Roman", 16),
        command=None,
    ):
        super().__init__(
            master=master,
            values=values,
            width=width,
            height=height,
            corner_radius=corner_radius,
            bg_color=bg_color,
            fg_color=fg_color,
            text_color=text_color,
            font=font,
            command=command,
        )
