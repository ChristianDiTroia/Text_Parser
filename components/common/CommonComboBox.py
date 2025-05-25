import customtkinter as Ctk
import tkinter as tk


class CommonComboBox(Ctk.CTkComboBox):
    def __init__(
        self,
        master,
        values=["Default"],
        width=200,
        height=28,
        corner_radius=16,
        border_width=None,
        bg_color="transparent",
        fg_color=None,
        border_color=None,
        text_color=None,
        font=("Times New Roman", 16),
        variable=None,
        command=None,
    ):
        super().__init__(
            master=master,
            values=values,
            width=width,
            height=height,
            corner_radius=corner_radius,
            border_width=border_width,
            bg_color=bg_color,
            fg_color=fg_color,
            border_color=border_color,
            text_color=text_color,
            font=font,
            variable=variable,
            command=command,
        )

        self.bind("<Return>", lambda _: master.focus_set())
        self.bind("<Escape>", lambda _: master.focus_set())
