import sys
from PyQt6.QtWidgets import QApplication
from PyQt6.QtGui import QIcon, QPixmap
from wallet_window import WalletWindow


class Window(WalletWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("My EpicGameStore")
        self.setWindowIcon(QIcon(QPixmap("Images/Epic_games_store_logo.png")))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    sys.exit(app.exec())
