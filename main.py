import sys
from PyQt6.QtWidgets import QApplication, QWidget

class Window(QApplication, QWidget):
    def __init__(self):
        super().__init__(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    sys.exit(app.exec())
