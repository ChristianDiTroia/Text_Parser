from components.common.CommonSwitch import CommonSwiitch


class ControlSwitch(CommonSwiitch):
    def __init__(self, master):
        super().__init__(master, text="Lock Controls", progress_color="IndianRed3")
