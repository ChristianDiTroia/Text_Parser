from components.common.CommonSwitch import CommonSwiitch


# Unused - may be included in the future to lock text that the user is working with
class ControlSwitch(CommonSwiitch):
    def __init__(self, master):
        super().__init__(master, text="Lock Controls", progress_color="IndianRed3")
