from Filter.filter_check import Ui_filter_check
from PyQt6.QtWidgets import QWidget


class FilterCheck(QWidget, Ui_filter_check):
    def __init__(self, text):
        super().__init__()
        self.text = text

        self.setupUi(self)
        self.checkBox.setText(text)
