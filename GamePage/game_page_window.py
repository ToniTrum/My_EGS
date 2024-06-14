from PyQt6.QtWidgets import QWidget, QPushButton, QPlainTextEdit, QStackedWidget, QLabel, QVBoxLayout, QHBoxLayout
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt, QSize
from GamePage.game_page_UI import Ui_game_page
import urllib.request
from bs4 import BeautifulSoup
import sqlite3


class GamePageWindow(QWidget):
    def __init__(self, game_id, prev):
        super().__init__()
        self.game_id = game_id
        self.prev = prev
        Ui_game_page().setupUi(self)

        self.back_button = self.findChild(QPushButton, "back_button")
        self.left_photo_button = self.findChild(QPushButton, "left_photo_button")
        self.right_photo_button = self.findChild(QPushButton, "right_photo_button")
        self.buy_button = self.findChild(QPushButton, "buy_button")
        self.add_to_wishlist_pushButton = self.findChild(QPushButton, "add_to_wishlist_pushButton")

        self.game_title_plainTextEdit = self.findChild(QPlainTextEdit, "game_title_plainTextEdit")
        self.annotation_plainTextEdit = self.findChild(QPlainTextEdit, "annotation_plainTextEdit")
        self.genres_plainTextEdit = self.findChild(QPlainTextEdit, "genres_plainTextEdit")
        self.content_plainTextEdit = self.findChild(QPlainTextEdit, "content_plainTextEdit")
        self.other_info_plainTextEdit = self.findChild(QPlainTextEdit, "other_info_plainTextEdit")

        self.picture_stacked = self.findChild(QStackedWidget, "picture_stacked")
        self.picture_label = self.findChild(QLabel, "picture_label")
        self.v_lay_of_table = self.findChild(QVBoxLayout, "v_lay_of_table")

        self.init_game_page_window_UI()

    def init_game_page_window_UI(self):
        self.picture_stacked.removeWidget(self.picture_stacked.widget(0))
        self.picture_stacked.removeWidget(self.picture_stacked.widget(0))

        self.get_information_from_html()
        self.get_information_from_db()

        self.back_button.clicked.connect(self.go_to_back)

    def get_information_from_db(self):
        game_info = self.get_information_from_games_db()
        self.game_title_plainTextEdit.setPlainText(game_info[1])
        self.game_title_plainTextEdit.setMinimumHeight(70)

        in_wishlist = self.get_information_from_wishlist_db()
        if in_wishlist is not None:
            in_wishlist = int(in_wishlist[0])
            if in_wishlist:
                self.buy_button.setText("Приобретено")
                self.add_to_wishlist_pushButton.setText("Приобретено")
            else:
                self.add_to_wishlist_pushButton.setText("Убрать из списка")

    def get_information_from_wishlist_db(self):
        con = sqlite3.connect("Data_bases/Users.bd")
        cur = con.cursor()
        result = cur.execute(f"""SELECT InLib from u{self.prev.user[0]}
                                 WHERE GameID = {self.game_id}""").fetchone()
        con.close()
        return result

    def get_information_from_games_db(self):
        con = sqlite3.connect("Data_bases/GamesList.db")
        cur = con.cursor()
        result = cur.execute(f"""SELECT * from GamesInfo
                                 WHERE GameID = {self.game_id}""").fetchone()
        con.close()
        return result

    def get_information_from_html(self):
        with open(f'Parcers/HTML_pages/{self.game_id}.html', encoding='utf-8') as file:
            src = file.read()

        soup = BeautifulSoup(src, 'lxml')
        self.set_screenshots(soup)
        self.add_text_content(soup)

    def set_screenshots(self, soup):
        screenshots = soup.find_all("div", class_="css-5emn3v")
        for picture in screenshots:
            img_url = picture.find("img").get("src")
            urllib.request.urlretrieve(img_url, "GamePage/buffer_img.png")
            self.set_image("GamePage/buffer_img.png")
        if not screenshots:
            self.set_image("Images/NoImage.png")

    def set_image(self, img_path):
        pixmap = QPixmap(img_path)
        scaling_size = (self.picture_stacked.size().width(),
                        int((self.picture_stacked.size().width() * pixmap.size().height()) / pixmap.size().width()))
        pixmap = pixmap.scaled(QSize(*scaling_size), Qt.AspectRatioMode.KeepAspectRatio)

        label = QLabel()
        label.setPixmap(pixmap)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        widget = QWidget()
        lay = QHBoxLayout()

        lay.addWidget(label)
        widget.setLayout(lay)

        self.picture_stacked.addWidget(widget)

    def add_text_content(self, soup):
        annotation = soup.find("div", class_="css-1myreog").text
        self.annotation_plainTextEdit.setPlainText(annotation)
        self.annotation_plainTextEdit.setMinimumHeight(120)

        content = soup.find("div", class_="css-1lwib6p")
        text = ""
        end_lines = 0
        for elem in content:
            if elem.text:
                text += (elem.text + "\n\n")
                end_lines += 2
        size = (len(text) - end_lines) / self.content_plainTextEdit.size().width()
        self.content_plainTextEdit.setPlainText(text)
        self.content_plainTextEdit.setMinimumHeight(
            int(self.content_plainTextEdit.size().width() * size / 10) + end_lines * 30)

    def go_to_back(self):
        self.prev.init_main_menu_window_UI(True)
