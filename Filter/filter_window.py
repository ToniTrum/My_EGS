from PyQt6.QtWidgets import QWidget, QApplication
from Filter.filter_window_UI import Ui_filter_window
from Filter.filter_checkBox import FilterCheck
import sqlite3
import sys


class FilterWindow(QWidget, Ui_filter_window):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.check_list = []
        self.mark = []

        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Выберите жанры")
        db = self.get_db()
        for genre in db:
            check = FilterCheck(genre[0])
            self.v_lay.addWidget(check)
            self.check_list.append(check)

        self.yes_button.clicked.connect()
        self.cancel_button.clicked.connect()

    def get_db(self):
        con = sqlite3.connect("../Data_bases/GamesList.db")
        cur = con.cursor()
        result = cur.execute("""SELECT GenreName from Genres""").fetchall()
        con.close()
        return result

    def yes_answer(self):




if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = FilterWindow()
    ex.show()
    sys.exit(app.exec())
