import tkinter
import customtkinter as ctk


class CommonSwiitch(ctk.CTkSwitch):
    def __init__(
        self,
        master,
        width=100,
        height=28,
        switch_width=75,
        switch_height=28,
        corner_radius=16,
        border_width=None,
        button_length=None,
        bg_color="transparent",
        fg_color=None,
        border_color="transparent",
        progress_color=None,
        button_color=None,
        button_hover_color=None,
        text_color=None,
        text_color_disabled=None,
        text="Common Switch",
        font=("Times New Roman", 16),
        textvariable=None,
        onvalue=1,
        offvalue=0,
        variable=None,
        hover=True,
        command=None,
        state=tkinter.NORMAL,
    ):
        super().__init__(
            master,
            width,
            height,
            switch_width,
            switch_height,
            corner_radius,
            border_width,
            button_length,
            bg_color,
            fg_color,
            border_color,
            progress_color,
            button_color,
            button_hover_color,
            text_color,
            text_color_disabled,
            text,
            font,
            textvariable,
            onvalue,
            offvalue,
            variable,
            hover,
            command,
            state,
        )
