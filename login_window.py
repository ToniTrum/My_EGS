from Registration.login_window_UI import Ui_Login_window
from PyQt6.QtWidgets import QWidget


class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui_login_window = Ui_Login_window()
        self.ui_login_window.setupUi(self)

