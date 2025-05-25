import tkinter
import customtkinter as Ctk


class CommonEntry(Ctk.CTkEntry):

    def __init__(
        self,
        master,
        width=200,
        height=28,
        corner_radius=16,
        border_width=None,
        bg_color="transparent",
        fg_color=None,
        border_color=None,
        text_color=None,
        placeholder_text_color=None,
        textvariable=None,
        placeholder_text=None,
        font=("Times New Roman", 16),
        state=tkinter.NORMAL,
    ):
        super().__init__(
            master,
            width,
            height,
            corner_radius,
            border_width,
            bg_color,
            fg_color,
            border_color,
            text_color,
            placeholder_text_color,
            textvariable,
            placeholder_text,
            font,
            state,
        )
