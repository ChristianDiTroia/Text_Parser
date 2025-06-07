from enum import StrEnum
from AppContext import AppContext
from components.common.CommonOptionMenu import CommonOptionMenu


class TokenTypeMenu(CommonOptionMenu):
    def __init__(self, master):
        super().__init__(
            master,
            values=[TokenType.SENTENCE, TokenType.LINE],
            width=125,
            command=self.__set_token_type,
        )
        self.__set_token_type(None)

    def __set_token_type(self, event):
        AppContext.var("token_type").set_value(self.get())


class TokenType(StrEnum):
    SENTENCE = "Sentences"
    LINE = "Lines"
