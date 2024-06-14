from AppUi.ImageButton.image_button import Ui_game_button
from PyQt6.QtWidgets import QWidget


class GameButton(QWidget, Ui_game_button):
    def __init__(self, game_id, title, price, image, link):
        super().__init__()
        self.title = title
        self.price = price
        self.image = image
        self.link = link
        self.game_id = game_id

        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.title_plainTextEdit.setPlainText(self.title)
        self.price_plainTextEdit.setPlainText(self.price)
        self.image_button.setStyleSheet(f"""
            QPushButton {{
                border-image: url({self.image}) 3 10 3 10;
                border-top: 3px transparent;
                border-bottom: 3px transparent;
                border-right: 10px transparent;
                border-left: 10px transparent;
            }}
        """)
