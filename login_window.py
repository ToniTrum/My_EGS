from PyQt6.QtWidgets import QWidget
from UI.login_window_UI import Ui_Login_window


class LoginWindow(QWidget, Ui_Login_window):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.setupUi(parent)
