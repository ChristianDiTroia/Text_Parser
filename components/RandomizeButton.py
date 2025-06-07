from TextParser import TextParser
from AppContext import AppContext
from components.common.CommonButton import CommonButton


class RandomizeButton(CommonButton):
    def __init__(self, master):
        super().__init__(master, text="Randomize")
        self.configure(command=self._randomize)

    def _randomize(self):
        text_parser: TextParser = AppContext.var("text_parser").get_value()
        text_var = AppContext.var("text_var")
        text_parser.shuffle_lines()
        text_var.set_value("\n".join(text_parser.get_next_lines(40)))
