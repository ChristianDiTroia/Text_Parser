import customtkinter as ctk


class CommonFrame(ctk.CTkFrame):

    def __init__(
        self,
        master,
        width=0,
        height=0,
        corner_radius=16,
        border_width=None,
        bg_color="transparent",
        fg_color=None,
        border_color=None,
        background_corner_colors=None,
        overwrite_preferred_drawing_method=None,
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
            background_corner_colors,
            overwrite_preferred_drawing_method,
        )
