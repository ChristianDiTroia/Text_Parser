from components.common.CommonOptionMenu import CommonOptionMenu


class TokenTypeMenu(CommonOptionMenu):
    def __init__(self, master):
        super().__init__(master, values=["Parse sentences", "Parse lines"], width=175)
