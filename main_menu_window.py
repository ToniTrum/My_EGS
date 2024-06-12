from register_stacked_window import RegisterWindow
from AppUi.ImageButton.imageMain import GameButton
from PyQt6.QtWidgets import QHBoxLayout, QPushButton, QVBoxLayout
from PyQt6.QtWidgets import QInputDialog
import sqlite3
from math import ceil


class MainMenuWindow(RegisterWindow):
    def __init__(self):
        super().__init__()
        self.pages_count = 0

        self.right_button = self.stacked.widget(2).findChild(QPushButton, "right_button")
        self.right_button.clicked.connect(self.next_page)

        self.left_button = self.stacked.widget(2).findChild(QPushButton, "left_button")
        self.left_button.clicked.connect(self.prev_page)

        self.page_number_button = self.stacked.widget(2).findChild(QPushButton, "page_number_button")
        self.page_number_button.clicked.connect(self.current_page)

        self.profile_button = self.stacked.widget(2).findChild(QPushButton, "profileButton")
        self.profile_button.clicked.connect(self.go_to_account_window)

        self.library_button = self.stacked.widget(2).findChild(QPushButton, "libraryButton")

        self.desired_button = self.stacked.widget(2).findChild(QPushButton, "desiredButton")

        self.wallet_button = self.stacked.widget(2).findChild(QPushButton, "walletButton")

    def init_main_menu_window_UI(self):
        self.stacked.setCurrentIndex(2)
        self.clear_games()
        self.add_games_row()

    def add_games_row(self):
        game_list = self.select_game_list()
        v_lay = self.stacked.widget(2).findChild(QVBoxLayout, "verticalLayout_4")

        for game in range(ceil(len(game_list) / 4)):
            h_lay = QHBoxLayout()
            for i in range(4):
                if len(game_list):
                    info = game_list.pop(0)
                    game_button = GameButton(*info)
                    game_button.image_button.clicked.connect(
                        lambda link=game_button.link: self.init_game_window_UI(link))
                    h_lay.addWidget(game_button)
                else:
                    break
            v_lay.addLayout(h_lay)

    def get_game_list(self):
        con = sqlite3.connect("Data_bases/GamesList.db")
        cur = con.cursor()
        result = cur.execute("""SELECT * from GamesInfo""").fetchall()
        con.close()
        return result

    def select_game_list(self):
        page_num = int(self.page_number_button.text()) - 1
        game_list = self.get_game_list()
        self.pages_count = ceil(len(game_list) / 40)
        start = page_num * 40
        game_list = game_list[start:]
        if len(game_list) > 40:
            game_list = game_list[:40]
        return game_list

    def init_game_window_UI(self, link):
        print(link)

    def current_page(self):
        old_num = self.page_number_button.text()
        self.show_dialog(self.page_number_button)
        try:
            page_num = int(self.page_number_button.text())
            if page_num > self.pages_count:
                page_num = self.pages_count
            elif page_num < 1:
                page_num = 1
            self.create_new_page(page_num)
        except ValueError:
            self.page_number_button.setText(old_num)

    def show_dialog(self, page_number_button):
        text, ok = QInputDialog.getText(self, 'Input Dialog', 'Введите номер страницы:')
        if ok:
            page_number_button.setText(str(text))

    def next_page(self):
        page_num = int(self.page_number_button.text()) + 1
        if page_num > self.pages_count:
            page_num = 1
        self.create_new_page(page_num)

    def prev_page(self):
        page_num = int(self.page_number_button.text()) - 1
        if page_num < 1:
            page_num = self.pages_count
        self.create_new_page(page_num)

    def create_new_page(self, page_num):
        self.page_number_button.setText(str(page_num))
        self.clear_games()
        self.add_games_row()

    def clear_games(self):
        v_lay = self.stacked.widget(2).findChild(QVBoxLayout, "verticalLayout_4")
        for i in range(v_lay.count() - 1):
            row_lay = v_lay.itemAt(1)
            for j in range(row_lay.count()):
                game = row_lay.takeAt(0)
                game.widget().setParent(None)
            v_lay.takeAt(1)
            row_lay.deleteLater()

    def go_to_account_window(self):
        self.stacked.setCurrentIndex(3)
        self.init_account_window_UI()
