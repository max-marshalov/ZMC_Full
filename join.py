# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'join.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Join(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(525, 250)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.edit_login = QtWidgets.QLineEdit(self.centralwidget)
        self.edit_login.setGeometry(QtCore.QRect(100, 70, 331, 31))
        self.edit_login.setObjectName("edit_login")
        self.edit_password = QtWidgets.QLineEdit(self.centralwidget)
        self.edit_password.setGeometry(QtCore.QRect(100, 120, 331, 31))
        self.edit_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.edit_password.setObjectName("edit_password")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(210, 10, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.btn_join = QtWidgets.QPushButton(self.centralwidget)
        self.btn_join.setGeometry(QtCore.QRect(100, 160, 131, 31))
        self.btn_join.setObjectName("btn_join")
        self.btn_reg = QtWidgets.QPushButton(self.centralwidget)
        self.btn_reg.setGeometry(QtCore.QRect(300, 160, 131, 31))
        self.btn_reg.setObjectName("btn_reg")
        self.label_error = QtWidgets.QLabel(self.centralwidget)
        self.label_error.setGeometry(QtCore.QRect(100, 210, 331, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_error.setFont(font)
        self.label_error.setStyleSheet("QLabel{\n"
"color: rgb(255, 0, 0);\n"
"}")
        self.label_error.setAlignment(QtCore.Qt.AlignCenter)
        self.label_error.setObjectName("label_error")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Вход"))
        self.btn_join.setText(_translate("MainWindow", "Войти"))
        self.btn_reg.setText(_translate("MainWindow", "Регистрация"))
        self.label_error.setText(_translate("MainWindow", "Введите логин и пароль"))
