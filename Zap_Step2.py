# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Zap_Step2.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Zap_Step2(object):
    def setupUi(self, Zap_Step2):
        Zap_Step2.setObjectName("Zap_Step2")
        Zap_Step2.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(Zap_Step2)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_next = QtWidgets.QPushButton(self.centralwidget)
        self.btn_next.setGeometry(QtCore.QRect(680, 540, 101, 31))
        self.btn_next.setObjectName("btn_next")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(160, 10, 461, 31))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(160, 50, 461, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(160, 180, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.edit_vidan = QtWidgets.QLineEdit(self.centralwidget)
        self.edit_vidan.setGeometry(QtCore.QRect(370, 190, 341, 20))
        self.edit_vidan.setObjectName("edit_vidan")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(160, 140, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.edit_serial = QtWidgets.QLineEdit(self.centralwidget)
        self.edit_serial.setGeometry(QtCore.QRect(370, 110, 341, 20))
        self.edit_serial.setMaxLength(5)
        self.edit_serial.setObjectName("edit_serial")
        self.edit_number = QtWidgets.QLineEdit(self.centralwidget)
        self.edit_number.setGeometry(QtCore.QRect(370, 150, 341, 20))
        self.edit_number.setMaxLength(6)
        self.edit_number.setObjectName("edit_number")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(160, 100, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.edit_code = QtWidgets.QLineEdit(self.centralwidget)
        self.edit_code.setGeometry(QtCore.QRect(370, 230, 341, 20))
        self.edit_code.setObjectName("edit_code")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(160, 220, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(160, 260, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.edit_date_vi = QtWidgets.QLineEdit(self.centralwidget)
        self.edit_date_vi.setGeometry(QtCore.QRect(370, 270, 341, 20))
        self.edit_date_vi.setObjectName("edit_date_vi")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(160, 300, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.btn_load_photo = QtWidgets.QPushButton(self.centralwidget)
        self.btn_load_photo.setGeometry(QtCore.QRect(370, 310, 75, 23))
        self.btn_load_photo.setObjectName("btn_load_photo")
        Zap_Step2.setCentralWidget(self.centralwidget)

        self.retranslateUi(Zap_Step2)
        QtCore.QMetaObject.connectSlotsByName(Zap_Step2)

    def retranslateUi(self, Zap_Step2):
        _translate = QtCore.QCoreApplication.translate
        Zap_Step2.setWindowTitle(_translate("Zap_Step2", "MainWindow"))
        self.btn_next.setText(_translate("Zap_Step2", "??????????"))
        self.label.setText(_translate("Zap_Step2", "?????????????????? ????????????"))
        self.label_2.setText(_translate("Zap_Step2", "????????????????, ???????????????????????????? ????????????????"))
        self.label_4.setText(_translate("Zap_Step2", "??????????"))
        self.label_3.setText(_translate("Zap_Step2", "??????????"))
        self.edit_serial.setInputMask(_translate("Zap_Step2", "00 00"))
        self.edit_number.setInputMask(_translate("Zap_Step2", "000000"))
        self.label_5.setText(_translate("Zap_Step2", "??????????"))
        self.edit_code.setInputMask(_translate("Zap_Step2", "000-000"))
        self.label_6.setText(_translate("Zap_Step2", "?????? ??????????????????????????"))
        self.label_7.setText(_translate("Zap_Step2", "???????? ????????????"))
        self.edit_date_vi.setInputMask(_translate("Zap_Step2", "00.00.0000"))
        self.label_8.setText(_translate("Zap_Step2", "???????? 1 ????????????????"))
        self.btn_load_photo.setText(_translate("Zap_Step2", "??????????????????"))
