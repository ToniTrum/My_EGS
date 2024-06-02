import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton , QLineEdit
from account_UI import Ui_Form
from PyQt6 import QtGui

class Account(QWidget, Ui_Form):
    def __init__(self):
        super().__init__() # - мы проводим инециализацию из qwiget кв swap
        self.setupUi(self)
        self.change_button.clicked.connect(self.setIcon)

    def setIcon(self):
        a = "image\profile\profile.png"
        self.icon_label.setPixmap(QtGui.QPixmap(a))
    
    def setDialog(self):
        self.dialog = QFileDialog.getOpenFileName(self, "Icon", os.path.realpath("src/app"), "Comma-Separated Values (*.png)")


if __name__=='__main__':
    app = QApplication(sys.argv)
    ac = Account()
    ac.show() # демонтстрирует окно
    sys.exit(app.exec())

