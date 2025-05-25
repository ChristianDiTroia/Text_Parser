from components.common.CommonCheckbox import CommonCheckbox


class SeedCheckbox(CommonCheckbox):
    def __init__(self, master):
        super().__init__(master, text="Use Random Seed")
        self.select()
