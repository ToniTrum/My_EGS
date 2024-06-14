import sys
from PyQt6.QtWidgets import QApplication
from change_account_window import ChangeAccountWindow
from wallet_window import WalletWindow


class Window(WalletWindow):
    def __init__(self):
        super().__init__()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    sys.exit(app.exec())
