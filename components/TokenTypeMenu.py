from components.common.CommonOptionMenu import CommonOptionMenu


class TokenTypeMenu(CommonOptionMenu):
    def __init__(self, master):
        super().__init__(master, values=["Sentences", "Lines"], width=125)
