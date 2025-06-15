import random
import sys
from AppContext import AppContext
from components.common.CommonButton import CommonButton


class RandomizeButton(CommonButton):
    def __init__(self, master):
        super().__init__(master, text="Randomize")
        self.configure(command=self._randomize)

    def _randomize(self):
        AppContext.var("loading").set_value("Shuffling text...")

        use_random_seed = AppContext.var("use_random_seed").get_value()
        seed = AppContext.var("seed").get_value()
        text_parser = AppContext.var("text_parser").get_value()

        if use_random_seed or not seed:
            seed = str(random.randint(-sys.maxsize - 1, sys.maxsize))
            AppContext.var("seed").set_value(seed)

        try:
            text_parser.shuffle_sentences(seed)
            text_parser.shuffle_lines(seed)
        except Exception:
            print("Text parser not initialized, nothing to randomize")

        self.after(1000, lambda: AppContext.var("loading").set_value(""))
