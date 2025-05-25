from components.common.CommonComboBox import CommonComboBox
import tkinter as tk


class TokenNumberComboBox(CommonComboBox):
    def __init__(self, master):
        super().__init__(
            master,
            values=["10", "20", "50", "100"],
            width=125,
            command=self._select_value,
        )
        self._value = self.get()
        self.bind("<Key>", self._validate_input)
        self.bind("<FocusOut>", self._default_input)

    def _select_value(self, event):
        self._value = event

    def _validate_input(self, event: tk.Event):
        if event.char.isdigit():
            self._value += event.char
        elif event.keysym in ("BackSpace", "Delete"):
            self._value = self._value[:-1]
        self.set(self._value)
        return "break"

    def _default_input(self, _):
        if self.get() == "" or self.get() == "0":
            self.set(self.cget("values")[0])
