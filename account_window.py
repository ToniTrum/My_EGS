from main_menu_window import MainMenuWindow
from PyQt6.QtWidgets import QLabel, QPushButton
from PyQt6.QtGui import QPixmap
import sqlite3


class AccountWindow(MainMenuWindow):
    def __init__(self):
        super().__init__()

        self.login_label_for_account = self.stacked.widget(3).findChild(QLabel, "login_label")
        self.balance_label = self.stacked.widget(3).findChild(QLabel, "balance_label")
        self.id_label = self.stacked.widget(3).findChild(QLabel, "id_label")
        self.icon_label = self.stacked.widget(3).findChild(QLabel, "icon_label")

        self.back_button_in_account = self.stacked.widget(3).findChild(QPushButton, "back_button")
        self.back_button_in_account.clicked.connect(self.init_main_menu_window_UI)

        self.change_button = self.stacked.widget(3).findChild(QPushButton, "change_button")
        self.change_button.clicked.connect(self.go_to_change_account_window)

        self.exit_account_button = self.stacked.widget(3).findChild(QPushButton, "exit_account_button")
        self.exit_account_button.clicked.connect(self.init_login_window_UI)

        self.delete_account_button = self.stacked.widget(3).findChild(QPushButton, "del_button")
        self.delete_account_button.clicked.connect(self.delete_account)

    def init_account_window_UI(self):
        self.login_label_for_account.setText(self.user[1])
        self.balance_label.setText(str(self.user[3]))
        self.id_label.setText(str(self.user[0]))
        self.icon_label.setPixmap(QPixmap(self.user[4]))

    def go_to_change_account_window(self):
        self.stacked.setCurrentIndex(4)
        self.init_change_account_window_UI()

    def delete_account(self):
        if self.open_dialog("Вы уверены, что хотите удалить аккаунт?"):
            con = sqlite3.connect("Data_bases/Users.bd")
            cur = con.cursor()
            result = cur.execute(f"""DELETE from users_data 
                                     WHERE UserID = {self.user[0]}""").fetchall()
            result = cur.execute(f"DROP TABLE [{self.user[0]}]").fetchall()

            con.commit()
            con.close()
            self.init_login_window_UI()
