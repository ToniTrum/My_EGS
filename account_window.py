from main_menu_window import MainMenuWindow
from PyQt6.QtWidgets import QLabel, QPushButton
from PyQt6.QtGui import QPixmap, QIcon


class AccountWindow(MainMenuWindow):
    def __init__(self):
        super().__init__()

    def init_account_window_UI(self):
        login_label = self.stacked.widget(3).findChild(QLabel, "login_label")
        login_label.setText(self.user[1])

        balance_label = self.stacked.widget(3).findChild(QLabel, "balance_label")
        balance_label.setText(str(self.user[3]))

        id_label = self.stacked.widget(3).findChild(QLabel, "id_label")
        id_label.setText(str(self.user[0]))

        icon_label = self.stacked.widget(3).findChild(QLabel, "icon_label")
        icon_label.setPixmap(QPixmap(self.user[4]))

        back_button = self.stacked.widget(3).findChild(QPushButton, "back_button")
        back_button.clicked.connect(lambda: self.go_to_main_menu_window(self.user))

        desired_button = self.stacked.widget(3).findChild(QPushButton, "desired_button")

        library_button = self.stacked.widget(3).findChild(QPushButton, "library_button")

        change_button = self.stacked.widget(3).findChild(QPushButton, "change_button")

        del_button = self.stacked.widget(3).findChild(QPushButton, "del_button")
