import sys
from pathlib import Path
import multiprocessing
import customtkinter as ctk
import threading
import time
import atexit
from AppContext import AppContext
from components.ProgressWindow import ProgressWindow
from components.ControlPanel import ControlPanel
from components.SaveButton import _save_dialogue, save_file
from components.WorkspaceFrame import WorkspaceFrame


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.auto_save: threading.Thread = create_auto_save_daemon(self)

        # State management
        AppContext.var("root").set_value(self)
        AppContext.var("loading").add_callback(self.set_loading)

        # Take focus of any widget when clicked
        self.bind_all("<Button-1>", lambda event: event.widget.focus_set())

        self.title("Text Parser")
        self.geometry("1920x1080")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=150)

        # Control Panel
        self.control_panel = ControlPanel(self)
        self.control_panel.grid(row=0, column=0, pady=0, sticky="new")

        # Workspace
        self.workspace = WorkspaceFrame(self)
        self.workspace.grid(row=1, column=0, padx=10, pady=5, sticky="nsew")

        # Progress bar
        self.progress_bar = ProgressWindow(self)

    def mainloop(self, *args, **kwargs):
        self.auto_save.start()
        super().mainloop(*args, **kwargs)

    def set_loading(self, value):
        if value:
            if isinstance(value, str):
                self.progress_bar.set_message(value)
            else:
                self.progress_bar.set_message("")
            self.progress_bar.grid(row=2, column=0, padx=10, pady=(0, 5), sticky="nse")
        else:
            self.progress_bar.grid_forget()


def create_auto_save_daemon(root: App):
    def job():
        app_alive = root.winfo_exists()
        while app_alive:
            file_path = AppContext.var("save_file").get_value()
            if file_path:
                try:
                    save_file(file_path)
                except Exception as e:
                    print(f"Failed to save to file: {file_path}")
            time.sleep(1)  # auto save every second while the app is alive
            try:
                app_alive = root.winfo_exists()
            except Exception:  # calling root raises exception if main loop exited
                app_alive = False

    return threading.Thread(name="auto_save_daemon", target=job, daemon=True)


def cleanup():
    file_path = AppContext.var("save_file").get_value()
    result_text = AppContext.var("result_var").get_value()
    if not file_path and result_text and result_text.strip():
        _save_dialogue()  # ask to save any unsaved changes when app closes


if __name__ == "__main__":
    if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
        bundle_dir = Path(sys._MEIPASS)
    else:
        bundle_dir = Path(__file__).parent
    AppContext.var("working_dir").set_value(bundle_dir)

    multiprocessing.freeze_support()  # required for pyinstaller on Windows
    atexit.register(cleanup)

    app = App()
    app.mainloop()
