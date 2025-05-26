import customtkinter as ctk
import tkinter as tk
from PIL import Image

from components.common.CommonFrame import CommonFrame
from components.common.CommonTextbox import CommonTextbox


class WorkspaceFrame(CommonFrame):

    def __init__(self, master, text_var: tk.StringVar):
        super().__init__(master)

        self.text_var = text_var

        # Configure frame layout
        self.grid_columnconfigure((0, 2), weight=5)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Left text box
        self.document_text = CommonTextbox(self, width=500)
        self.document_text.grid(row=0, column=0, padx=(40, 0), pady=40, sticky="nsew")
        text_var.trace_add("write", self.update_text)

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
        self.result_text.grid(row=0, column=2, padx=(0, 40), pady=40, sticky="nsew")

    def update_text(self, var, index, mode):
        """Update the document text box when the text variable changes."""
        self.document_text.delete("1.0", "end")
        self.document_text.insert("1.0", self.text_var.get())
