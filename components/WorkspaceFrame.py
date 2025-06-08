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
        AppContext.var("text_var").add_callback(self.__update_text)

        # Configure frame layout
        self.grid_columnconfigure((0, 1), weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Left text box
        self.document_text = CommonTextbox(self, width=500)
        self.document_text.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        # # Arrow image
        # self.right_arrow = ctk.CTkImage(
        #     Image.open("./icons/right-arrow.png"), size=(64, 64)
        # )
        # self.right_arrow_label = ctk.CTkLabel(
        #     self, image=self.right_arrow, width=128, height=128, text=""
        # )
        # self.right_arrow_label.grid(row=0, column=1, sticky="nsew")

        # Right text box
        self.result_text = CommonTextbox(self, width=500)
        self.result_text.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
        self.result_text.bind("<KeyRelease>", command=self.__save_result)

    def __update_text(self, value):
        self.document_text.delete("1.0", "end")
        self.document_text.insert("1.0", value)

    def __save_result(self, event):
        if self.result_text.edit_modified():
            AppContext.var("result_var").set_value(self.result_text.get(1.0, tk.END))
            self.result_text.edit_modified(False)
