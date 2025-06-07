from AppContext import AppContext
from components.TokenTypeMenu import TokenType
from components.common.CommonButton import CommonButton


class GetTextButton(CommonButton):
    def __init__(self, master):
        super().__init__(master, text="Get text")
        self.configure(command=self._display_text)

    def _display_text(self):
        text_parser = AppContext.var("text_parser").get_value()
        token_type = AppContext.var("token_type").get_value()
        num_tokens = AppContext.var("token_number").get_value()
        to_display = ""

        match token_type:
            case TokenType.SENTENCE:
                to_display = text_parser.get_next_sentences(num_tokens)
            case TokenType.LINE:
                to_display = text_parser.get_next_lines(num_tokens)
            case _:
                raise ValueError(f"Incorrect token type recieved: {token_type}")

        AppContext.var("text_var").set_value("\n\n".join(to_display))
