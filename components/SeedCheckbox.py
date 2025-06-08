from AppContext import AppContext
from components.common.CommonCheckbox import CommonCheckbox


class SeedCheckbox(CommonCheckbox):
    def __init__(self, master):
        super().__init__(
            master, text="Use Random Seed", command=self._save_checked_state
        )
        self.select()
        self._save_checked_state()

    def _save_checked_state(self):
        AppContext.var("use_random_seed").set_value(self.get())
