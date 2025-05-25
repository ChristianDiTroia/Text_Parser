import customtkinter as ctk

from components.ControlPanel import ControlPanel
from components.WorkspaceFrame import WorkspaceFrame


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Take focus of any widget when clicked
        self.bind_all("<Button-1>", lambda event: event.widget.focus_set())

        self.title("Poem Generator Beta")
        self.geometry("1920x1080")
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=10)
        self.grid_rowconfigure(0, weight=1)

        # Control Panel
        self.control_panel = ControlPanel(self)
        self.control_panel.grid(row=0, column=0, padx=(40, 20), pady=40, sticky="nsew")

        # Workspace
        self.workspace = WorkspaceFrame(self)
        self.workspace.grid(row=0, column=1, padx=(20, 40), pady=40, sticky="nsew")


if __name__ == "__main__":
    app = App()
    app.mainloop()
