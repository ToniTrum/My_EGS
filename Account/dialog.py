import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton , QLineEdit
from dialog_ui import Ui_Dialog

class Dialog(QWidget, Ui_Dialog):
    def __init__(self):
        super().__init__() # - мы проводим инециализацию из qwiget в swap
        self.setupUi(self)
    
    
    


if __name__=='__main__':
    app = QApplication(sys.argv)
    ac = Dialog()
    ac.show() # демонтстрирует окно
    sys.exit(app.exec())

