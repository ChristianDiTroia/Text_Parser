import tkinter as tk

from AppContext import AppContext
from components.common.CommonButton import CommonButton


class RandomizeButton(CommonButton):
    def __init__(self, master):
        super().__init__(master, text="Randomize Text")
        self.configure(command=self._randomize)

    def _randomize(self):
        text_parser = AppContext.text_parser
        text_var = tk.StringVar(name="text_var")
        print(text_var.get())

        text_parser.shuffle_lines()
        text_var.set("\n".join(text_parser.get_next_lines(10)))
