from Registration.login_window_UI import Ui_Login_window
from Registration.authorization_window_UI import Ui_authorization_window
from AppUi.menuUI.main_menu_window_UI import Ui_main_menu_window
from Account.change_account_window_UI import Ui_change_account_window
from Registration.main_window import Ui_main_window
from Account.account import Ui_account_window
from PyQt6.QtWidgets import QWidget, QCommandLinkButton, QPushButton, QLabel, QLineEdit
import sqlite3
import re


class RegisterWindow(QWidget, Ui_main_window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.user = (0, 0, 0, 0)

        self.stacked.removeWidget(self.stacked.widget(0))
        self.stacked.removeWidget(self.stacked.widget(0))

        self.ui_login_window = Ui_Login_window()
        self.ui_authorization_window = Ui_authorization_window()
        self.ui_main_menu_window = Ui_main_menu_window()
        self.ui_account_window = Ui_account_window()
        self.ui_change_account_window = Ui_change_account_window()

        self.login_window = QWidget()
        self.authorization_window = QWidget()
        self.main_menu_window = QWidget()
        self.account_window = QWidget()
        self.change_account_window = QWidget()

        self.ui_login_window.setupUi(self.login_window)
        self.ui_authorization_window.setupUi(self.authorization_window)
        self.ui_main_menu_window.setupUi(self.main_menu_window)
        self.ui_account_window.setupUi(self.account_window)
        self.ui_change_account_window.setupUi(self.change_account_window)

        self.stacked.addWidget(self.login_window)           # 0
        self.stacked.addWidget(self.authorization_window)   # 1
        self.stacked.addWidget(self.main_menu_window)       # 2
        self.stacked.addWidget(self.account_window)         # 3
        self.stacked.addWidget(self.change_account_window)  # 4

        self.init_login_window_UI()

    def init_login_window_UI(self):
        self.stacked.setCurrentIndex(0)

        linked_button = self.stacked.widget(0).findChild(QCommandLinkButton, "commoand_link_to_authorization_window")
        linked_button.clicked.connect(self.init_authorization_window_UI)

        login_button = self.stacked.widget(0).findChild(QPushButton, "login_button")
        login_button.clicked.connect(self.checking_user)

    def checking_user(self):
        login_lineEdit = self.stacked.widget(0).findChild(QLineEdit, "login_lineEdit")
        password_lineEdit = self.stacked.widget(0).findChild(QLineEdit, "password_lineEdit")

        result = self.search_user(login_lineEdit.text())
        worning_label = self.stacked.widget(0).findChild(QLabel, "worning_label")
        if result:
            if result[2] == password_lineEdit.text():
                worning_label.setText("")
                self.go_to_main_menu_window(result[1])
            else:
                worning_label.setText("Неверный логин или пароль")
        else:
            worning_label.setText("Неверный логин или пароль")

    def search_user(self, user_login):
        con = sqlite3.connect("Data_bases/Users.bd")
        cur = con.cursor()

        result = cur.execute(f"""SELECT UserID, Login, Password from users_data
                                 WHERE Login = '{user_login}'""").fetchone()
        con.close()
        return result

    def init_authorization_window_UI(self):
        self.stacked.setCurrentIndex(1)

        back_button = self.stacked.widget(1).findChild(QPushButton, "back_button")
        back_button.clicked.connect(self.init_login_window_UI)

        create_accaunt_button = self.stacked.widget(1).findChild(QPushButton, "create_accaunt_button")
        create_accaunt_button.clicked.connect(self.checking_for_correctness)

    def checking_for_correctness(self):
        flag = True

        login_lineEdit = self.stacked.widget(1).findChild(QLineEdit, "login_lineEdit")
        worning_of_login_label = self.stacked.widget(1).findChild(QLabel, "worning_of_login_label")

        user_data = self.search_user(login_lineEdit.text())

        if not user_data:
            if not self.exam_of_login(login_lineEdit.text()):
                flag = False
                worning_of_login_label.setText("Некорректный логин")
            else:
                worning_of_login_label.setText("")

            password_lineEdit = self.stacked.widget(1).findChild(QLineEdit, "password_lineEdit")
            worning_of_password_label = self.stacked.widget(1).findChild(QLabel, "worning_of_password_label")
            if not self.exam_of_password(password_lineEdit.text()):
                flag = False
                worning_of_password_label.setText("Некорректный пароль")
            else:
                worning_of_password_label.setText("")

            repeat_password_lineEdit = self.stacked.widget(1).findChild(QLineEdit, "repeat_password_lineEdit")
            worning_of_repeat_password_label = self.stacked.widget(1).findChild(QLabel, "worning_of_repeat_password_label")
            if repeat_password_lineEdit.text() != password_lineEdit.text():
                flag = False
                worning_of_repeat_password_label.setText("Неверный пароль")
            else:
                worning_of_repeat_password_label.setText("")

            if flag:
                self.creating_new_account(login_lineEdit.text(), password_lineEdit.text())
                self.go_to_main_menu_window(login_lineEdit.text())
        else:
            worning_of_login_label.setText("Пользователь с таким логином уже существует")

    def creating_new_account(self, login, password):
        con = sqlite3.connect("Data_bases/Users.bd")
        cur = con.cursor()
        result = cur.execute(f"""INSERT INTO users_data(Login, Password)
                                 VALUES('{login}', '{password}') """).fetchall()

        user_id = cur.execute(f"""SELECT UserID from users_data
                                  WHERE login = '{login}'""").fetchone()
        result = cur.execute(f"""CREATE TABLE [{user_id[0]}] (
                                 GameID INTEGER PRIMARY KEY
                                 );""")
        con.commit()
        con.close()

    def exam_of_login(self, login):
        if 3 <= len(login) <= 20:
            res = re.findall(r"[a-zA-Z0-9_]", login)
            if len(login) == len(res):
                return True
        return False

    def exam_of_password(self, password):
        if 6 <= len(password) <= 60:
            res = re.findall(r"[a-zA-Z0-9_,#%^!$&*()?;:<>=~]", password)
            if len(password) == len(res):
                return True
        return False

    def go_to_main_menu_window(self, login):
        con = sqlite3.connect("Data_bases/Users.bd")
        cur = con.cursor()
        user = cur.execute(f"""SELECT * from users_data
                               WHERE login = '{login}'""").fetchone()
        con.close()

        self.user = user
        self.init_main_menu_window_UI()
