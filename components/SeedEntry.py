import tkinter as tk
from AppContext import AppContext
from components.common.CommonEntry import CommonEntry


class SeedEntry(CommonEntry):
    def __init__(self, master):
        super().__init__(
            master,
            placeholder_text="Seed",
            width=100,
            height=28,
        )

        # State management
        self.bind("<KeyRelease>", command=self._save_entry_state)
        AppContext.var("seed").add_callback(self.__display_seed)

    def _save_entry_state(self, event):
        AppContext.var("seed").set_value(self.get())

    def __display_seed(self, value):
        if self.get() != value:  # check this to prevent redundant re-render
            self.delete("0", tk.END)
            self.insert("0", str(value))
