from PyQt6.QtWidgets import QWidget
from UI.authorization_window_UI import Ui_Authorization_window


class AuthorizationWindow(QWidget, Ui_Authorization_window):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.setupUi(parent)