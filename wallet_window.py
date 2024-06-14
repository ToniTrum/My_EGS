from change_account_window import ChangeAccountWindow
from PyQt6.QtWidgets import QPushButton, QLabel
from PyQt6.QtWidgets import QInputDialog
import sqlite3


class WalletWindow(ChangeAccountWindow):
    def __init__(self):
        super().__init__()
        self.back_button_from_wallet = self.stacked.widget(5).findChild(QPushButton, "back_button")
        self.pay_button = self.stacked.widget(5).findChild(QPushButton, "pay_button")
        self.balance_label = self.stacked.widget(5).findChild(QLabel, "balance_label")

        self.replenish_300 = self.stacked.widget(5).findChild(QPushButton, "replenish_300")
        self.replenish_500 = self.stacked.widget(5).findChild(QPushButton, "replenish_500")
        self.replenish_1000 = self.stacked.widget(5).findChild(QPushButton, "replenish_1000")
        self.replenish = self.stacked.widget(5).findChild(QPushButton, "replenish")

    def init_wallet_window_UI(self):
        self.balance_label.setText(str(self.user[3]))

        self.replenish_300.clicked.connect(lambda: self.pay(300))
        self.replenish_500.clicked.connect(lambda: self.pay(500))
        self.replenish_1000.clicked.connect(lambda: self.pay(1000))

        self.replenish.clicked.connect(self.choose_num)
        self.pay_button.clicked.connect(self.increase_balance)
        self.back_button_from_wallet.clicked.connect(self.init_main_menu_window_UI)

    def pay(self, num):
        balance = float(self.balance_label.text()) + num
        self.balance_label.setText(str(balance))

    def show_balance_dialog(self):
        text, ok = QInputDialog.getText(self, 'Input Dialog', 'Введите сумму:')
        if ok:
            return text

    def choose_num(self):
        num = self.show_balance_dialog()
        try:
            num = float(num)
            self.pay(num)
            if float(self.balance_label.text()) < 0:
                self.balance_label.setText("0")
        except ValueError:
            pass

    def increase_balance(self):
        con = sqlite3.connect("Data_bases/Users.bd")
        cur = con.cursor()
        result = cur.execute(f"""UPDATE users_data
                                 SET Balance = Balance + {self.balance_label.text()}
                                 WHERE UserID = {self.user[0]}""").fetchall()
        con.commit()
        con.close()

        new_data = (self.user[0],
                    self.user[1],
                    self.user[2],
                    float(self.balance_label.text()),
                    self.user[4])
        self.user = new_data
        self.init_main_menu_window_UI()
