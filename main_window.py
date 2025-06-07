import customtkinter as ctk
import threading
import time
from AppContext import AppContext
from components.ControlPanel import ControlPanel
from components.WorkspaceFrame import WorkspaceFrame


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        auto_save_daemon(self)

        # State management
        AppContext.var("root").set_value(self)

        # Take focus of any widget when clicked
        self.bind_all("<Button-1>", lambda event: event.widget.focus_set())

        self.title("Text Parser")
        self.geometry("1920x1080")
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=20)
        self.grid_rowconfigure(0, weight=1)

        # Workspace
        self.workspace = WorkspaceFrame(self)
        self.workspace.grid(row=0, column=1, padx=(20, 40), pady=40, sticky="nsew")

        # Control Panel
        self.control_panel = ControlPanel(self)
        self.control_panel.grid(row=0, column=0, padx=(40, 20), pady=40, sticky="nsew")


def auto_save_daemon(root: App):
    def job():
        while root.winfo_exists():
            file_path = AppContext.var("save_file").get_value()
            if file_path:
                try:
                    with open(file_path, "w") as save_file:
                        save_file.write(AppContext.var("result_var").get_value())
                except Exception as e:
                    print(f"Failed to save to file: {file_path}")
            time.sleep(1)  # auto save every second while the app is alive

    threading.Thread(name="auto_save_daemon", target=job, daemon=True).start()


if __name__ == "__main__":
    app = App()
    app.mainloop()
