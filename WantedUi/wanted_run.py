
from wanted_ui import *
from PyQt6.QtWidgets import QWidget, QApplication
import sys
class MainWindow(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()

        self.setupUi(self)



if __name__ == "__main__":
    qApp = QApplication(sys.argv)
    app = MainWindow()
    app.show()

    sys.exit(qApp.exec())

