from PyQt6.QtWidgets import QWidget, QPushButton, QPlainTextEdit, QStackedWidget, QLabel, QVBoxLayout, QHBoxLayout
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtWidgets import QMessageBox
from GamePage.game_page_UI import Ui_game_page
from GamePage.table_row import TableRow
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
        self.left_photo_button.clicked.connect(self.left_page)
        self.right_photo_button.clicked.connect(self.right_page)

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
                self.add_to_wishlist_pushButton.clicked.connect(self.delete_from_wishlist)

                if "RUB" in game_info[2] or "₽" in game_info[2]:
                    self.buy_button.setText(game_info[2])
                    self.buy_button.clicked.connect(self.buy_game)
                elif game_info[2] == "Бесплатно":
                    self.buy_button.setText("0")
                    self.buy_button.clicked.connect(self.buy_game)
        else:
            self.add_to_wishlist_pushButton.setText("Добавить в желаемое")
            self.add_to_wishlist_pushButton.clicked.connect(self.add_to_wishlist)

            if "RUB" in game_info[2] or "₽" in game_info[2]:
                self.buy_button.setText(game_info[2])
                self.buy_button.clicked.connect(self.buy_game)
            elif game_info[2] == "Бесплатно":
                self.buy_button.setText("0")
                self.buy_button.clicked.connect(self.buy_game)
            else:
                self.buy_button.setText("Скоро")

        genres = self.get_information_from_genres_db()
        text = ""
        for genre in genres:
            text += (genre[0] + ",   ")
        self.genres_plainTextEdit.setPlainText(text)

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

    def get_information_from_genres_db(self):
        con = sqlite3.connect("Data_bases/GamesList.db")
        cur = con.cursor()
        result = cur.execute(f"""SELECT
                                 Genres.GenreName
                                 FROM GenresForGame
                                 INNER JOIN Genres ON Genres.GenreID = GenresForGame.GenreID
                                 WHERE GenresForGame.GameID = {self.game_id}""").fetchall()
        con.close()
        return result

    def get_information_from_html(self):
        with open(f'Parcers/HTML_pages/{self.game_id}.html', encoding='utf-8') as file:
            src = file.read()

        soup = BeautifulSoup(src, 'lxml')
        self.set_screenshots(soup)
        self.add_text_content(soup)
        self.add_right_game_card(soup)

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
        if content is None:
            content = soup.find("div", class_="css-1u6j54o")
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

    def add_right_game_card(self, soup):
        card = soup.find("div", class_="css-1gmuxco")
        if card is None:
            card = soup.find("div", class_="css-pfnsbm")

        self.set_game_icon(card)
        self.set_table_info(card)
        self.set_other_information(card)

    def set_game_icon(self, card):
        icon_url = card.find("div", class_="css-uwwqev").find("img").get("src")
        urllib.request.urlretrieve(icon_url, "GamePage/buffer_img.png")
        pixmap = QPixmap("GamePage/buffer_img.png")
        scaling_size = (self.picture_label.size().width(),
                        int((self.picture_label.size().width() * pixmap.size().height()) / pixmap.size().width()))
        pixmap = pixmap.scaled(QSize(*scaling_size), Qt.AspectRatioMode.KeepAspectRatio)
        self.picture_label.setPixmap(pixmap)
        self.picture_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

    def set_table_info(self, card):
        exceptions = ["Вознаграждения Epic", "Тип возврата", "Платформа"]

        rows = card.find_all("div", class_="css-10mlqmn")
        for row in rows:
            table_row = row.find("div", class_="css-1o0y1dn")
            head = table_row.find("span", class_="css-d3i3lr")
            if head.text not in exceptions:
                header = head.text
                value = table_row.find("span", class_="css-119zqif").text
                table_row_widget = TableRow(header, value)
                self.v_lay_of_table.addWidget(table_row_widget)

    def set_other_information(self, card):
        info = card.find("div", class_="css-1mdcw0h")
        if info:
            text = ""
            tags = info.find_all("div", class_="css-u4p24i")
            for tag in tags:
                text += (tag.text + "   ")
        self.other_info_plainTextEdit.setPlainText(text)

    def add_to_wishlist(self):
        con = sqlite3.connect("Data_bases/Users.bd")
        cur = con.cursor()

        result = cur.execute(f"""INSERT INTO u{self.prev.user[0]}(GameID, InLib)
                                 VALUES({self.game_id}, 0)""").fetchall()
        self.add_to_wishlist_pushButton.setText("Убрать из списка")
        self.add_to_wishlist_pushButton.clicked.connect(self.delete_from_wishlist)

        con.commit()
        con.close()

    def delete_from_wishlist(self):
        con = sqlite3.connect("Data_bases/Users.bd")
        cur = con.cursor()

        result = cur.execute(f"""DELETE from u{self.prev.user[0]}
                                 WHERE GameID = {self.game_id}""").fetchall()
        self.add_to_wishlist_pushButton.setText("Добавить в желаемое")
        self.add_to_wishlist_pushButton.clicked.connect(self.add_to_wishlist)

        con.commit()
        con.close()

    def buy_game(self):
        price = float(self.buy_button.text().replace(" ", "").replace("RUB", "").replace("₽", ""))
        if self.prev.user[3] < price:
            self.prev.open_dialog("У Вас недостаточно средств")
        else:
            if self.prev.open_dialog("Вы уверены, что хотите совершить покупку?"):
                self.buy_button.setText("Приобретено")
                self.buy_button.clicked.connect(self.void)

                self.add_to_wishlist_pushButton.setText("Приобретено")
                self.add_to_wishlist_pushButton.clicked.connect(self.void)

                new_data = [self.prev.user[0],
                            self.prev.user[1],
                            self.prev.user[2],
                            self.prev.user[3] - price,
                            self.prev.user[4]]
                self.prev.user = new_data

                con = sqlite3.connect("Data_bases/Users.bd")
                cur = con.cursor()

                result = cur.execute(f"""UPDATE users_data
                                         SET Balance = {self.prev.user[3]}
                                         WHERE UserID = {self.prev.user[0]}""").fetchall()

                result = cur.execute(f"""SELECT GameID from u{self.prev.user[0]}
                                         WHERE GameID = {self.game_id}""").fetchone()
                if result:
                    result = cur.execute(f"""DELETE from u{self.prev.user[0]}
                                             WHERE GameID = {self.game_id}""").fetchall()

                result = cur.execute(f"""INSERT INTO u{self.prev.user[0]}(GameID, InLib)
                                         VALUES({self.game_id}, 1)""").fetchall()

                con.commit()
                con.close()

    def left_page(self):
        if self.picture_stacked.currentIndex() > 0:
            self.picture_stacked.setCurrentIndex(self.picture_stacked.currentIndex() - 1)
        else:
            self.picture_stacked.setCurrentIndex(self.picture_stacked.count() - 1)

    def right_page(self):
        if self.picture_stacked.currentIndex() < self.picture_stacked.count() - 1:
            self.picture_stacked.setCurrentIndex(self.picture_stacked.currentIndex() + 1)
        else:
            self.picture_stacked.setCurrentIndex(0)

    def go_to_back(self):
        self.prev.init_main_menu_window_UI(True)

    def void(self):
        pass
