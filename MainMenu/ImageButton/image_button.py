# Form implementation generated from reading ui file '.\image_button.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_game_button(object):
    def setupUi(self, game_button):
        game_button.setObjectName("game_button")
        game_button.resize(212, 320)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(game_button.sizePolicy().hasHeightForWidth())
        game_button.setSizePolicy(sizePolicy)
        game_button.setMaximumSize(QtCore.QSize(212, 320))
        game_button.setStyleSheet("background-color: rgb(27, 29, 30);")
        self.verticalLayout = QtWidgets.QVBoxLayout(game_button)
        self.verticalLayout.setObjectName("verticalLayout")
        self.image_button = QtWidgets.QPushButton(parent=game_button)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.image_button.sizePolicy().hasHeightForWidth())
        self.image_button.setSizePolicy(sizePolicy)
        self.image_button.setMinimumSize(QtCore.QSize(150, 175))
        self.image_button.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.image_button.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.NoContextMenu)
        self.image_button.setStyleSheet("font: 11pt \"Arial\";\n"
"color: rgb(243, 243, 243);\n"
"border-radius: 10%;")
        self.image_button.setText("")
        self.image_button.setIconSize(QtCore.QSize(50, 50))
        self.image_button.setFlat(True)
        self.image_button.setObjectName("image_button")
        self.verticalLayout.addWidget(self.image_button)
        self.title_plainTextEdit = QtWidgets.QPlainTextEdit(parent=game_button)
        self.title_plainTextEdit.setMaximumSize(QtCore.QSize(1666666, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.title_plainTextEdit.setFont(font)
        self.title_plainTextEdit.setStyleSheet("color: rgb(255, 255, 255);\n"
"border-radius: 10%;\n"
"background-color: rgb(51, 51, 51);")
        self.title_plainTextEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.title_plainTextEdit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.title_plainTextEdit.setReadOnly(True)
        self.title_plainTextEdit.setPlainText("")
        self.title_plainTextEdit.setObjectName("title_plainTextEdit")
        self.verticalLayout.addWidget(self.title_plainTextEdit)
        self.price_plainTextEdit = QtWidgets.QPlainTextEdit(parent=game_button)
        self.price_plainTextEdit.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.price_plainTextEdit.setFont(font)
        self.price_plainTextEdit.setStyleSheet("color: rgb(255, 255, 255);\n"
"border-radius: 10%;\n"
"background-color: rgb(51, 51, 51);")
        self.price_plainTextEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.price_plainTextEdit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.price_plainTextEdit.setReadOnly(True)
        self.price_plainTextEdit.setObjectName("price_plainTextEdit")
        self.verticalLayout.addWidget(self.price_plainTextEdit)

        self.retranslateUi(game_button)
        QtCore.QMetaObject.connectSlotsByName(game_button)

    def retranslateUi(self, game_button):
        _translate = QtCore.QCoreApplication.translate
        game_button.setWindowTitle(_translate("game_button", "Form"))
