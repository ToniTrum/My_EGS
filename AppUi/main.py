
from interface import *
from PyQt6.QtWidgets import QMainWindow, QApplication
import sys
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.setupUi(self)




if __name__ == "__main__":
    qApp = QApplication(sys.argv)
    app = MainWindow()
    app.show()

    sys.exit(qApp.exec())


