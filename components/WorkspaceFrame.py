import customtkinter as ctk
import tkinter as tk
from PIL import Image
from AppContext import AppContext
from components.common.CommonFrame import CommonFrame
from components.common.CommonTextbox import CommonTextbox


class WorkspaceFrame(CommonFrame):

    def __init__(self, master):
        super().__init__(master)

        # State management
        text_var = AppContext.var("text_var")
        text_var.add_callback(self.update_text)

        # Configure frame layout
        self.grid_columnconfigure((0, 2), weight=5)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Left text box
        self.document_text = CommonTextbox(self, width=500)
        self.document_text.grid(row=0, column=0, padx=(20, 0), pady=20, sticky="nsew")

        # Arrow image
        self.right_arrow = ctk.CTkImage(
            Image.open("./icons/right-arrow.png"), size=(64, 64)
        )
        self.right_arrow_label = ctk.CTkLabel(
            self, image=self.right_arrow, width=128, height=128, text=""
        )
        self.right_arrow_label.grid(row=0, column=1, sticky="nsew")

        # Right text box
        self.result_text = CommonTextbox(self, width=500)
        self.result_text.grid(row=0, column=2, padx=(0, 20), pady=20, sticky="nsew")

    def update_text(self, value):
        self.document_text.delete("1.0", "end")
        self.document_text.insert("1.0", value)
