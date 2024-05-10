import sys
from PyQt6.QtWidgets import QApplication



if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    sys.exit(app.exec())