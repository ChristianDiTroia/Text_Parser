from components.SeedCheckbox import SeedCheckbox
from components.SeedEntry import SeedEntry
from components.TokenTypeMenu import TokenTypeMenu
from components.RandomizeButton import RandomizeButton
from components.ControlSwitch import ControlSwitch
from components.common.CommonFrame import CommonFrame
from components.SaveButton import SaveButton
from components.UploadButton import UploadButton
from components.TokenNumberComboBox import TokenNumberComboBox


class ControlPanel(CommonFrame):

    def __init__(self, master):
        super().__init__(master, corner_radius=16)

        # Configure frame layout
        self.grid_columnconfigure((0, 1), weight=1)
        self.grid_rowconfigure((0, 1, 3, 4, 5, 7), weight=0)
        self.grid_rowconfigure((2), weight=1)
        self.grid_rowconfigure((6), weight=1)

        # Upload button
        self.upload_button = UploadButton(self)
        self.upload_button.grid(
            row=0, column=0, padx=40, pady=(40, 0), sticky="new", columnspan=2
        )

        # Save button
        self.save_button = SaveButton(self)
        self.save_button.grid(
            row=1, column=0, padx=40, pady=(40, 0), sticky="new", columnspan=2
        )

        # Lock text switch
        self.lock_text_switch = ControlSwitch(self)
        self.lock_text_switch.grid(
            row=3, column=0, padx=40, pady=(40, 0), sticky="sew", columnspan=2
        )

        # Token count entry
        self.token_count_entry = TokenNumberComboBox(self)
        self.token_count_entry.grid(
            row=4, column=0, padx=(40, 10), pady=(40, 0), sticky="sew", columnspan=1
        )

        # Token type selection
        self.token_type_selection = TokenTypeMenu(self)
        self.token_type_selection.grid(
            row=4, column=1, padx=(10, 40), pady=(40, 0), sticky="sew", columnspan=1
        )

        # Randomize button
        self.randomize_button = RandomizeButton(self)
        self.randomize_button.grid(
            row=5, column=0, padx=40, pady=40, sticky="sew", columnspan=2
        )

        # Seed entry
        self.seed_entry = SeedEntry(self)
        self.seed_entry.grid(
            row=7, column=0, padx=(40, 10), pady=40, sticky="sew", columnspan=1
        )

        self.random_seed_checkbox = SeedCheckbox(self)
        self.random_seed_checkbox.grid(
            row=7, column=1, padx=(10, 40), pady=40, sticky="sew", columnspan=1
        )
