from AppContext import AppContext
from components.common.CommonComboBox import CommonComboBox
import tkinter as tk


class TokenNumberComboBox(CommonComboBox):
    def __init__(self, master):
        super().__init__(
            master,
            values=["10", "20", "50", "100"],
            width=125,
            command=self.__select_value,
        )
        self._value = self.get()
        self.__set_token_number()
        self.bind("<Key>", self.__validate_input)
        self.bind("<FocusOut>", self.__default_input)

    def __set_token_number(self):
        try:
            token_num = int(self._value)
        except:
            token_num = self.cget("values")[0]
        AppContext.var("token_number").set_value(token_num)

    def __select_value(self, event):
        self._value = event
        self.__set_token_number()

    def __validate_input(self, event: tk.Event):
        if event.char.isdigit():
            self._value += event.char
        elif event.keysym in ("BackSpace", "Delete"):
            self._value = self._value[:-1]
        self.set(self._value)
        self.__set_token_number()
        return "break"

    def __default_input(self, _):
        if self.get() == "" or self.get() == "0":
            self.set(self.cget("values")[0])
            self.__set_token_number()
