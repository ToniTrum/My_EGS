from imageButton import *
from PyQt6.QtWidgets import QWidget, QApplication
import sys
import pillow_avif
from PyQt6.QtWidgets import QLabel, QVBoxLayout
from PyQt6.QtGui import QPixmap
from PIL import Image

from PyQt6.QtNetwork import QNetworkRequest, QNetworkReply


class MainWindow(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        title = input("Введите название ")
        price = input("Введите цену ")
        image = input("Введите путь к изображению ")

        #image_avif = Image.open("lizard-slayer-1y44v.avif")
        #image_avif.save("lizard-slayer-1y44v.png", "PNG")
       

        # Создание кнопки с использованием сохраненного изображения в качестве фона
       
        
        self.title_listWidget.addItem(title)
        self.prise_listWidget.addItem(price)

        self.image_button.setStyleSheet(f"""
            QPushButton {{
                border-image: url({image}) 3 10 3 10;
                border-top: 3px transparent;
                border-bottom: 3px transparent;
                border-right: 10px transparent;
                border-left: 10px transparent;
            }}
        """)


        

if __name__ == "__main__":
    qApp = QApplication(sys.argv)
    app = MainWindow()
    app.show()

    sys.exit(qApp.exec())


