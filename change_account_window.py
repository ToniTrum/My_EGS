from account_window import AccountWindow
from PyQt6.QtWidgets import QPushButton, QLabel, QLineEdit
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QFileDialog, QMessageBox
import sqlite3
from PIL import Image


class ChangeAccountWindow(AccountWindow):
    def __init__(self):
        super().__init__()
        self.image_path = ""

        self.login_lineEdit_for_change = self.stacked.widget(4).findChild(QLineEdit, "login_lineEdit")
        self.password_lineEdit_for_change = self.stacked.widget(4).findChild(QLineEdit, "password_lineEdit")
        self.repeat_password_lineEdit_for_change = self.stacked.widget(4).findChild(QLineEdit,
                                                                                    "repeat_password_lineEdit")

        self.choose_photo_button = self.stacked.widget(4).findChild(QPushButton, "choose_photo_button")
        self.choose_photo_button.clicked.connect(self.choose_new_profile_icon)

        self.cancel_button_for_change = self.stacked.widget(4).findChild(QPushButton, "cancel_button")
        self.cancel_button_for_change.clicked.connect(self.go_to_account_window)

        self.change_account_button = self.stacked.widget(4).findChild(QPushButton, "change_account_button")
        self.change_account_button.clicked.connect(self.change_account_info)

        self.photo_label = self.stacked.widget(4).findChild(QLabel, "photo_label")
        self.photo_label.setScaledContents(True)

    def init_change_account_window_UI(self):
        self.stacked.setCurrentIndex(4)

        self.login_lineEdit_for_change.setText(self.user[1])
        self.password_lineEdit_for_change.setText(self.user[2])
        self.repeat_password_lineEdit_for_change.setText("")

        self.image_path = self.user[4]
        self.photo_label.setPixmap(QPixmap(self.user[4]))

    def choose_new_profile_icon(self):
        photo_path = self.open_file_dialog()
        self.image_path = photo_path
        self.photo_label.setPixmap(QPixmap(photo_path))

    def open_file_dialog(self):
        dialog = QFileDialog()
        dialog.setNameFilter("Image files (*.png *.jpg *.jpeg *.svg)")
        if dialog.exec():
            return dialog.selectedFiles()[0]

    def open_dialog(self, mess):
        message = QMessageBox(self)
        message.setIcon(QMessageBox.Icon.Information)
        message.setText(mess)
        message.setWindowTitle("Внимание")
        message.setStandardButtons(QMessageBox.StandardButton.No | QMessageBox.StandardButton.Yes)

        value = message.exec()
        if value == QMessageBox.StandardButton.Yes:
            return True
        return False

    def change_account_info(self):
        flag = True

        if self.open_dialog("Вы уверены, что хотитие изменить данные?"):
            warning_of_login_label = self.stacked.widget(4).findChild(QLabel, "worning_of_login_label")
            warning_of_password_label = self.stacked.widget(4).findChild(QLabel, "worning_of_password_label")
            warning_of_repeat_password_label = self.stacked.widget(4).findChild(QLabel, "worning_of_repeat_password_label")

            if not self.exam_of_login(self.login_lineEdit_for_change.text()):
                flag = False
                warning_of_login_label.setText("Некорректный логин")
            else:
                warning_of_login_label.setText("")

            if not self.exam_of_password(self.password_lineEdit_for_change.text()):
                flag = False
                warning_of_password_label.setText("Некорректный пароль")
            else:
                warning_of_password_label.setText("")

            if self.repeat_password_lineEdit_for_change.text() != self.password_lineEdit_for_change.text():
                flag = False
                warning_of_repeat_password_label.setText("Неверный пароль")
            else:
                warning_of_repeat_password_label.setText("")

            if flag:
                image = Image.open(self.image_path)
                extension = self.image_path.split(".")[-1]
                self.image_path = f"Images/{self.user[0]}.{extension}"
                image.save(self.image_path)

                new_user_data = (self.user[0],
                                 self.login_lineEdit_for_change.text(),
                                 self.password_lineEdit_for_change.text(),
                                 self.user[3],
                                 self.image_path)
                self.user = new_user_data
                self.change_db_info()
                self.go_to_account_window()

    def change_db_info(self):
        con = sqlite3.connect("Data_bases/Users.bd")
        cur = con.cursor()
        result = cur.execute("""UPDATE users_data
                                SET
                                Login = ?,
                                Password = ?,
                                Image = ?
                                WHERE UserID = ?""",
                             (self.user[1], self.user[2],
                              self.user[4], self.user[0])).fetchall()
        con.commit()
        con.close()
