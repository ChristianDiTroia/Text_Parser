from customtkinter import CTkCheckBox, CTkFont, Variable
from typing import Any, Tuple, Callable

import tkinter


class CommonCheckbox(CTkCheckBox):
    def __init__(
        self,
        master: Any,
        width: int = 100,
        height: int = 28,
        checkbox_width: int = 24,
        checkbox_height: int = 24,
        corner_radius: int | None = None,
        border_width: int | None = None,
        bg_color: str | Tuple[str, str] = "transparent",
        fg_color: str | Tuple[str, str] | None = None,
        hover_color: str | Tuple[str, str] | None = None,
        border_color: str | Tuple[str, str] | None = None,
        checkmark_color: str | Tuple[str, str] | None = None,
        text_color: str | Tuple[str, str] | None = None,
        text_color_disabled: str | Tuple[str, str] | None = None,
        text: str = "Common Checkbox",
        font: tuple | CTkFont | None = ("Times New Roman", 16),
        textvariable: Variable | None = None,
        state: str = tkinter.NORMAL,
        hover: bool = True,
        command: Callable[[], Any] | None = None,
        onvalue: int | str = 1,
        offvalue: int | str = 0,
        variable: Variable | None = None,
        **kwargs
    ):
        super().__init__(
            master=master,
            width=width,
            height=height,
            checkbox_width=checkbox_width,
            checkbox_height=checkbox_height,
            corner_radius=corner_radius,
            border_width=border_width,
            bg_color=bg_color,
            fg_color=fg_color,
            hover_color=hover_color,
            border_color=border_color,
            checkmark_color=checkmark_color,
            text_color=text_color,
            text_color_disabled=text_color_disabled,
            text=text,
            font=font,
            textvariable=textvariable,
            state=state,
            hover=hover,
            command=command,
            onvalue=onvalue,
            offvalue=offvalue,
            variable=variable,
            **kwargs
        )
