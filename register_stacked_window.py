from UI.login_window_UI import Ui_Login_window
from UI.authorization_window_UI import Ui_Authorization_window
from PyQt6.QtWidgets import QWidget, QStackedWidget


class RegisterWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.stacked = QStackedWidget()
        self.stacked.addWidget(Ui_Login_window)
        self.stacked.addWidget(Ui_Authorization_window)
        self.stacked.setCurrentIndex(0)
