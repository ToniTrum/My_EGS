# Form implementation generated from reading ui file '.\table_row_UI.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_table_row(object):
    def setupUi(self, table_row):
        table_row.setObjectName("table_row")
        table_row.resize(235, 50)
        table_row.setMaximumSize(QtCore.QSize(16777215, 50))
        self.horizontalLayout = QtWidgets.QHBoxLayout(table_row)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.header_label = QtWidgets.QLabel(parent=table_row)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.header_label.sizePolicy().hasHeightForWidth())
        self.header_label.setSizePolicy(sizePolicy)
        self.header_label.setMinimumSize(QtCore.QSize(60, 30))
        self.header_label.setMaximumSize(QtCore.QSize(16777215, 50))
        self.header_label.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 8pt \"Calibri\";\n"
"background-color: rgb(81, 81, 81);")
        self.header_label.setIndent(10)
        self.header_label.setObjectName("header_label")
        self.horizontalLayout.addWidget(self.header_label)
        self.value_label = QtWidgets.QLabel(parent=table_row)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.value_label.sizePolicy().hasHeightForWidth())
        self.value_label.setSizePolicy(sizePolicy)
        self.value_label.setMinimumSize(QtCore.QSize(60, 30))
        self.value_label.setMaximumSize(QtCore.QSize(16777215, 50))
        self.value_label.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 8pt \"Calibri\";\n"
"background-color: rgb(81, 81, 81);")
        self.value_label.setIndent(10)
        self.value_label.setObjectName("value_label")
        self.horizontalLayout.addWidget(self.value_label)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 1)

        self.retranslateUi(table_row)
        QtCore.QMetaObject.connectSlotsByName(table_row)

    def retranslateUi(self, table_row):
        _translate = QtCore.QCoreApplication.translate
        table_row.setWindowTitle(_translate("table_row", "Form"))
        self.header_label.setText(_translate("table_row", "TextLabel"))
        self.value_label.setText(_translate("table_row", "TextLabel"))
