# Form implementation generated from reading ui file 'account.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(874, 705)
        Form.setStyleSheet("background-color: rgb(35, 38, 39);")
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(parent=Form)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 850, 681))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.scrollArea_2 = QtWidgets.QScrollArea(parent=self.scrollAreaWidgetContents)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 826, 657))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.back_button = QtWidgets.QPushButton(parent=self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.back_button.sizePolicy().hasHeightForWidth())
        self.back_button.setSizePolicy(sizePolicy)
        self.back_button.setMinimumSize(QtCore.QSize(50, 50))
        self.back_button.setMaximumSize(QtCore.QSize(50, 50))
        self.back_button.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.PreventContextMenu)
        self.back_button.setStyleSheet("color:rgb(223, 228, 229);\n"
"font: 63 10pt \"Yu Gothic UI Semibold\";\n"
"background-color: rgb(51, 55, 57);\n"
"border-radius: 25%\n"
"\n"
"")
        self.back_button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("image/icon/angle-left-b.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.back_button.setIcon(icon)
        self.back_button.setIconSize(QtCore.QSize(40, 40))
        self.back_button.setObjectName("back_button")
        self.horizontalLayout_9.addWidget(self.back_button)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem)
        self.verticalLayout_4.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.icon_label = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.icon_label.sizePolicy().hasHeightForWidth())
        self.icon_label.setSizePolicy(sizePolicy)
        self.icon_label.setMinimumSize(QtCore.QSize(300, 300))
        self.icon_label.setMaximumSize(QtCore.QSize(300, 300))
        self.icon_label.setSizeIncrement(QtCore.QSize(1, 1))
        self.icon_label.setStyleSheet("border-radius: 10%;")
        self.icon_label.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.icon_label.setMidLineWidth(1)
        self.icon_label.setText("")
        self.icon_label.setPixmap(QtGui.QPixmap("../../OPD/My_EGS/AppUi/ImageButton/lizard-slayer-1y44v.png"))
        self.icon_label.setScaledContents(True)
        self.icon_label.setWordWrap(False)
        self.icon_label.setIndent(0)
        self.icon_label.setOpenExternalLinks(False)
        self.icon_label.setObjectName("icon_label")
        self.horizontalLayout_4.addWidget(self.icon_label)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_4 = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMinimumSize(QtCore.QSize(0, 40))
        self.label_4.setMaximumSize(QtCore.QSize(140, 100))
        self.label_4.setStyleSheet("color:rgb(223, 228, 229);\n"
"background-color: rgb(51, 55, 57);\n"
"font: 63 15pt \"Yu Gothic UI Semibold\";\n"
"\n"
"border-radius: 25%\n"
"\n"
"\n"
"")
        self.label_4.setScaledContents(False)
        self.label_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_4.setIndent(15)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.login_label = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents_2)
        self.login_label.setStyleSheet("color:rgb(223, 228, 229);\n"
"background-color: rgb(51, 55, 57);\n"
"font: 63 15pt \"Yu Gothic UI Semibold\";\n"
"\n"
"border-radius: 25%\n"
"\n"
"")
        self.login_label.setIndent(15)
        self.login_label.setObjectName("login_label")
        self.horizontalLayout_2.addWidget(self.login_label)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.balance_command_link = QtWidgets.QPushButton(parent=self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.balance_command_link.sizePolicy().hasHeightForWidth())
        self.balance_command_link.setSizePolicy(sizePolicy)
        self.balance_command_link.setMaximumSize(QtCore.QSize(140, 100))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.balance_command_link.setFont(font)
        self.balance_command_link.setStyleSheet("color:rgb(223, 228, 229);\n"
"background-color: rgb(51, 55, 57);\n"
"font: 63 13pt \"Yu Gothic UI Semibold\";\n"
"\n"
"border-radius: 25%\n"
"\n"
"")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("image/icon/wallet.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.balance_command_link.setIcon(icon1)
        self.balance_command_link.setIconSize(QtCore.QSize(50, 50))
        self.balance_command_link.setCheckable(True)
        self.balance_command_link.setChecked(True)
        self.balance_command_link.setAutoRepeat(False)
        self.balance_command_link.setAutoExclusive(False)
        self.balance_command_link.setObjectName("balance_command_link")
        self.horizontalLayout_5.addWidget(self.balance_command_link)
        self.balance_label = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents_2)
        self.balance_label.setStyleSheet("color:rgb(223, 228, 229);\n"
"background-color: rgb(51, 55, 57);\n"
"font: 63 15pt \"Yu Gothic UI Semibold\";\n"
"\n"
"border-radius: 25%\n"
"\n"
"\n"
"")
        self.balance_label.setIndent(15)
        self.balance_label.setObjectName("balance_label")
        self.horizontalLayout_5.addWidget(self.balance_label)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents_2)
        self.label_2.setMaximumSize(QtCore.QSize(140, 100))
        self.label_2.setStyleSheet("color:rgb(223, 228, 229);\n"
"font: 63 15pt \"Yu Gothic UI Semibold\";\n"
"\n"
"background-color: rgb(51, 55, 57);\n"
"border-radius: 25%\n"
"\n"
"")
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_2.setIndent(15)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.id_label = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents_2)
        self.id_label.setStyleSheet("color:rgb(223, 228, 229);\n"
"font: 63 15pt \"Yu Gothic UI Semibold\";\n"
"background-color: rgb(51, 55, 57);\n"
"border-radius: 25%\n"
"\n"
"")
        self.id_label.setIndent(15)
        self.id_label.setObjectName("id_label")
        self.horizontalLayout_3.addWidget(self.id_label)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Maximum)
        self.verticalLayout_2.addItem(spacerItem1)
        self.horizontalLayout_4.addLayout(self.verticalLayout_2)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Maximum)
        self.verticalLayout_4.addItem(spacerItem2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.desired_button = QtWidgets.QPushButton(parent=self.scrollAreaWidgetContents_2)
        self.desired_button.setStyleSheet("color:rgb(223, 228, 229);\n"
"background-color: rgb(27, 30, 31);\n"
"font: 63 10pt \"Yu Gothic UI Semibold\";\n"
"\n"
"")
        self.desired_button.setObjectName("desired_button")
        self.verticalLayout_3.addWidget(self.desired_button)
        self.widget = QtWidgets.QWidget(parent=self.scrollAreaWidgetContents_2)
        self.widget.setObjectName("widget")
        self.verticalLayout_3.addWidget(self.widget)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.library_button = QtWidgets.QPushButton(parent=self.scrollAreaWidgetContents_2)
        self.library_button.setStyleSheet("color:rgb(223, 228, 229);\n"
"font: 63 10pt \"Yu Gothic UI Semibold\";\n"
"\n"
"background-color: rgb(27, 30, 31);")
        self.library_button.setObjectName("library_button")
        self.verticalLayout_5.addWidget(self.library_button)
        self.widget_2 = QtWidgets.QWidget(parent=self.scrollAreaWidgetContents_2)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_5.addWidget(self.widget_2)
        self.verticalLayout_4.addLayout(self.verticalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.change_button = QtWidgets.QPushButton(parent=self.scrollAreaWidgetContents_2)
        self.change_button.setStyleSheet("background-color: rgb(177, 191, 197);\n"
"font: 63 10pt \"Yu Gothic UI Semibold\";\n"
"\n"
"")
        self.change_button.setObjectName("change_button")
        self.horizontalLayout_6.addWidget(self.change_button)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem3)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.del_button = QtWidgets.QPushButton(parent=self.scrollAreaWidgetContents_2)
        self.del_button.setStyleSheet("color:rgb(223, 228, 229);\n"
"font: 63 10pt \"Yu Gothic UI Semibold\";\n"
"background-color: rgb(198, 57, 57)\n"
"\n"
"\n"
"")
        self.del_button.setObjectName("del_button")
        self.horizontalLayout_7.addWidget(self.del_button)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem4)
        self.verticalLayout_4.addLayout(self.horizontalLayout_7)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.horizontalLayout.addWidget(self.scrollArea_2)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_4.setText(_translate("Form", "LOGIN:"))
        self.login_label.setText(_translate("Form", "TextLabel"))
        self.balance_command_link.setText(_translate("Form", "Баланс:"))
        self.balance_label.setText(_translate("Form", "TextLabel"))
        self.label_2.setText(_translate("Form", "ID:"))
        self.id_label.setText(_translate("Form", "TextLabel"))
        self.desired_button.setText(_translate("Form", "СПИСОК ЖЕЛАЙМОГО"))
        self.library_button.setText(_translate("Form", "БИБЛИОТЕКА"))
        self.change_button.setText(_translate("Form", "Изменить данные"))
        self.del_button.setText(_translate("Form", " Удалить аккаунт  "))
