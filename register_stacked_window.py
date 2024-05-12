from UI.login_window_UI import Ui_Login_window
from UI.authorization_window_UI import Ui_Authorization_window
from UI.main_window import Ui_main_window
from PyQt6.QtWidgets import QWidget


class RegisterWindow(QWidget, Ui_main_window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.stacked.removeWidget(self.stacked.widget(0))
        self.stacked.removeWidget(self.stacked.widget(0))

        self.ui_login_window = Ui_Login_window()
        self.ui_authorization_window = Ui_Authorization_window()

        self.login_window = QWidget()
        self.authorization_window = QWidget()

        self.ui_login_window.setupUi(self.login_window)
        self.ui_authorization_window.setupUi(self.authorization_window)

        self.stacked.addWidget(self.login_window)
        self.stacked.addWidget(self.authorization_window)
        self.stacked.setCurrentIndex(0)

    def initUI(self):
        pass
