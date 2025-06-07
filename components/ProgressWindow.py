import customtkinter as ctk


class ProgressWindow(ctk.CTkToplevel):
    def __init__(self, master=None, title="Progress", message="Processing..."):
        super().__init__(master=master, takefocus=True)
        self.title(title)
        self.geometry("500x200")  # TODO - center the window
        self.resizable(False, False)

        self.grid_rowconfigure((0, 1), weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Message label
        self.message = ctk.CTkLabel(self, text=message, font=("Times New Roman", 20))
        self.message.grid(row=0, padx=20, pady=20)

        # Progress bar
        self.progress_bar = ctk.CTkProgressBar(self, mode="indeterminate")
        self.progress_bar.grid(row=1, padx=20, pady=20, sticky="ew")
        self.progress_bar.start()
