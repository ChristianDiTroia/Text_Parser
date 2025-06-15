import customtkinter as ctk
from components.common.CommonFrame import CommonFrame


class ProgressWindow(CommonFrame):
    def __init__(self, master, message="Processing..."):
        super().__init__(master=master, corner_radius=2, fg_color="transparent")

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure((0, 1), weight=1)

        # Message label
        self.message = ctk.CTkLabel(self, text=message, font=("Times New Roman", 12))
        self.message.grid(row=0, column=0)

        # Progress bar
        self.progress_bar = ctk.CTkProgressBar(self, mode="indeterminate")
        self.progress_bar.grid(row=0, column=1, padx=20, sticky="ew")
        self.progress_bar.start()

    def set_message(self, message: str):
        self.message.configure(text=message)
