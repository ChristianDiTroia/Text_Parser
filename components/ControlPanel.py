from components.MoveContentButton import MoveContentButton
from components.GetTextButton import GetTextButton
from components.SeedCheckbox import SeedCheckbox
from components.SeedEntry import SeedEntry
from components.TokenTypeMenu import TokenTypeMenu
from components.RandomizeButton import RandomizeButton
from components.common.CommonFrame import CommonFrame
from components.SaveButton import SaveButton
from components.UploadButton import UploadButton
from components.TokenNumberComboBox import TokenNumberComboBox


class ControlPanel(CommonFrame):

    def __init__(self, master):
        super().__init__(master, corner_radius=0)

        # Configure frame layout
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure((0, 1, 3, 4, 5, 6, 8, 9, 10), weight=0)
        self.grid_columnconfigure((2), weight=3)
        self.grid_columnconfigure((7), weight=2)

        # IO upload and save buttons
        self.upload_button = UploadButton(self)
        self.upload_button.grid(column=0, row=0, sticky="ew")

        self.save_button = SaveButton(self)
        self.save_button.grid(column=1, row=0, sticky="ew")

        # Token count entry
        self.token_count_entry = TokenNumberComboBox(self)
        self.token_count_entry.grid(column=3, row=0, padx=10, sticky="ew")

        # Token type selection
        self.token_type_selection = TokenTypeMenu(self)
        self.token_type_selection.grid(column=4, row=0, padx=10, sticky="ew")

        # Get text button
        self.get_text_button = GetTextButton(self)
        self.get_text_button.grid(column=5, row=0, padx=10, sticky="ew")

        # Move content button
        self.move_content_button = MoveContentButton(self)
        self.move_content_button.grid(column=6, row=0, padx=10, sticky="ew")

        # Seed entry
        self.random_seed_checkbox = SeedCheckbox(self)
        self.random_seed_checkbox.grid(column=8, row=0, padx=10, sticky="ew")

        self.seed_entry = SeedEntry(self)
        self.seed_entry.grid(column=9, row=0, padx=10, sticky="ew")

        # Randomize button
        self.randomize_button = RandomizeButton(self)
        self.randomize_button.grid(column=10, row=0, padx=10, sticky="ew")
