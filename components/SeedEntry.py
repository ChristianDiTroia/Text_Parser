from components.common.CommonEntry import CommonEntry


class SeedEntry(CommonEntry):
    def __init__(self, master):
        super().__init__(master, placeholder_text="Seed", width=100, height=28)
