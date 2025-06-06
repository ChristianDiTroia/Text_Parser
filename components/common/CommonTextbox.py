import customtkinter as ctk
from typing import Any, Tuple
from customtkinter import CTkFont


class CommonTextbox(ctk.CTkTextbox):
    def __init__(
        self,
        master: Any,
        width: int = 200,
        height: int = 200,
        corner_radius: int | None = None,
        border_width: int | None = None,
        border_spacing: int = 3,
        bg_color: str | Tuple[str, str] = "transparent",
        fg_color: str | Tuple[str, str] | None = None,
        border_color: str | Tuple[str, str] | None = None,
        text_color: str | None = None,
        scrollbar_button_color: str | Tuple[str, str] | None = None,
        scrollbar_button_hover_color: str | Tuple[str, str] | None = None,
        font: tuple | CTkFont | None = ("Times New Roman", 20),
        activate_scrollbars: bool = True,
        undo=True,
        autoseparators=True,
        **kwargs: Any
    ):
        super().__init__(
            master,
            width=width,
            height=height,
            corner_radius=corner_radius,
            border_width=border_width,
            border_spacing=border_spacing,
            bg_color=bg_color,
            fg_color=fg_color,
            border_color=border_color,
            text_color=text_color,
            scrollbar_button_color=scrollbar_button_color,
            scrollbar_button_hover_color=scrollbar_button_hover_color,
            font=font,
            activate_scrollbars=activate_scrollbars,
            undo=undo,
            autoseparators=autoseparators,
            wrap="none",
            **kwargs
        )
