from AppContext import AppContext
from components.common.CommonButton import CommonButton
from components.TokenTypeMenu import TokenType


class RandomizeButton(CommonButton):
    def __init__(self, master):
        super().__init__(master, text="Randomize")
        self.configure(command=self._randomize)

    def _randomize(self):
        seed = AppContext.var("seed").get_value()
        token_type = AppContext.var("token_type").get_value()
        text_parser = AppContext.var("text_parser").get_value()

        match token_type:
            case TokenType.SENTENCE:
                text_parser.shuffle_sentences(seed)
            case TokenType.LINE:
                text_parser.shuffle_lines(seed)
            case _:
                raise ValueError(f"Incorrect token type recieved: {token_type}")
