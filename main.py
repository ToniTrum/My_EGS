import sys
from PyQt6.QtWidgets import QApplication
from register_stacked_window import RegisterWindow
from main_menu_window import MainMenuWindow


class Window(MainMenuWindow):
    def __init__(self):
        super().__init__()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    sys.exit(app.exec())
