from GamePage.table_row_UI import Ui_table_row
from PyQt6.QtWidgets import QWidget


class TableRow(QWidget, Ui_table_row):
    def __init__(self, header, value):
        super().__init__()
        self.header = header
        self.value = value
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.header_label.setText(self.header)
        self.value_label.setText(self.value)
