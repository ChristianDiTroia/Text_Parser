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
        AppContext.var("result_var").add_callback(self.__update_result)

        # Configure frame layout
        self.grid_columnconfigure((0, 1), weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Left text box
        self.document_text = CommonTextbox(self, width=500)
        self.document_text.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        self.document_text.bind("<<Modified>>", command=self.__save_text)

        # Right text box
        self.result_text = CommonTextbox(self, width=500)
        self.result_text.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
        self.result_text.bind("<<Modified>>", command=self.__save_result)

    def __update_text(self, value):
        cursor_pos = self.document_text.index(tk.INSERT)
        self.document_text.delete("1.0", "end")
        self.document_text.insert("1.0", value)

        try:
            self.document_text.mark_set(tk.INSERT, cursor_pos)
        except tk.TclError:
            self.document_text.mark_set(tk.INSERT, "end")

    def __update_result(self, value):
        cursor_pos = self.result_text.index(tk.INSERT)
        self.result_text.delete("1.0", "end")
        self.result_text.insert("1.0", value)

        try:
            self.result_text.mark_set(tk.INSERT, cursor_pos)
        except tk.TclError:
            self.result_text.mark_set(tk.INSERT, "end")

    def __save_text(self, event):
        if self.document_text.edit_modified():
            text = self.document_text.get(1.0, tk.END).removesuffix("\n")
            AppContext.var("text_var").set_value(text)
            self.document_text.edit_modified(False)

    def __save_result(self, event):
        if self.result_text.edit_modified():
            text = self.result_text.get(1.0, tk.END).removesuffix("\n")
            AppContext.var("result_var").set_value(text)
            self.result_text.edit_modified(False)
