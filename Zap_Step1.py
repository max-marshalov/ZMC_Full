# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Zap_Step1.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Zap_Step1(object):
    def setupUi(self, Zap_Step1):
        Zap_Step1.setObjectName("Zap_Step1")
        Zap_Step1.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(Zap_Step1)
        self.centralwidget.setObjectName("centralwidget")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(170, 210, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.edit_mail = QtWidgets.QLineEdit(self.centralwidget)
        self.edit_mail.setGeometry(QtCore.QRect(340, 300, 341, 20))
        self.edit_mail.setInputMask("")
        self.edit_mail.setMaxLength(32767)
        self.edit_mail.setObjectName("edit_mail")
        self.edit_dad = QtWidgets.QLineEdit(self.centralwidget)
        self.edit_dad.setGeometry(QtCore.QRect(340, 220, 341, 20))
        self.edit_dad.setObjectName("edit_dad")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(170, 170, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.edit_surname = QtWidgets.QLineEdit(self.centralwidget)
        self.edit_surname.setGeometry(QtCore.QRect(340, 140, 341, 20))
        self.edit_surname.setObjectName("edit_surname")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(170, 290, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.radioButton_female = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_female.setGeometry(QtCore.QRect(450, 260, 82, 17))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.radioButton_female.setFont(font)
        self.radioButton_female.setObjectName("radioButton_female")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(170, 250, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.edit_name = QtWidgets.QLineEdit(self.centralwidget)
        self.edit_name.setGeometry(QtCore.QRect(340, 180, 341, 20))
        self.edit_name.setObjectName("edit_name")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(170, 130, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.radioButton_male = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_male.setGeometry(QtCore.QRect(340, 260, 82, 17))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radioButton_male.sizePolicy().hasHeightForWidth())
        self.radioButton_male.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.radioButton_male.setFont(font)
        self.radioButton_male.setIconSize(QtCore.QSize(16, 16))
        self.radioButton_male.setObjectName("radioButton_male")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(160, 10, 461, 31))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(170, 330, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.edit_date = QtWidgets.QLineEdit(self.centralwidget)
        self.edit_date.setGeometry(QtCore.QRect(340, 340, 341, 20))
        self.edit_date.setInputMask("")
        self.edit_date.setMaxLength(32767)
        self.edit_date.setObjectName("edit_date")
        self.edit_phone = QtWidgets.QLineEdit(self.centralwidget)
        self.edit_phone.setGeometry(QtCore.QRect(340, 380, 341, 20))
        self.edit_phone.setInputMask("")
        self.edit_phone.setMaxLength(32767)
        self.edit_phone.setObjectName("edit_phone")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(170, 370, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(170, 400, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.edit_birth_place = QtWidgets.QLineEdit(self.centralwidget)
        self.edit_birth_place.setGeometry(QtCore.QRect(340, 420, 341, 20))
        self.edit_birth_place.setInputMask("")
        self.edit_birth_place.setMaxLength(32767)
        self.edit_birth_place.setObjectName("edit_birth_place")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(170, 440, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.radioButton_yes = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_yes.setGeometry(QtCore.QRect(340, 460, 82, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radioButton_yes.sizePolicy().hasHeightForWidth())
        self.radioButton_yes.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.radioButton_yes.setFont(font)
        self.radioButton_yes.setIconSize(QtCore.QSize(16, 16))
        self.radioButton_yes.setObjectName("radioButton_yes")
        self.radioButton_no = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_no.setGeometry(QtCore.QRect(450, 460, 82, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.radioButton_no.setFont(font)
        self.radioButton_no.setObjectName("radioButton_no")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(170, 490, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.btn_load_photo = QtWidgets.QPushButton(self.centralwidget)
        self.btn_load_photo.setGeometry(QtCore.QRect(340, 510, 75, 23))
        self.btn_load_photo.setObjectName("btn_load_photo")
        self.btn_next = QtWidgets.QPushButton(self.centralwidget)
        self.btn_next.setGeometry(QtCore.QRect(684, 552, 101, 31))
        self.btn_next.setObjectName("btn_next")
        Zap_Step1.setCentralWidget(self.centralwidget)

        self.retranslateUi(Zap_Step1)
        QtCore.QMetaObject.connectSlotsByName(Zap_Step1)

    def retranslateUi(self, Zap_Step1):
        _translate = QtCore.QCoreApplication.translate
        Zap_Step1.setWindowTitle(_translate("Zap_Step1", "MainWindow"))
        self.label_4.setText(_translate("Zap_Step1", "Отчество"))
        self.label_3.setText(_translate("Zap_Step1", "Имя"))
        self.label_6.setText(_translate("Zap_Step1", "Email"))
        self.radioButton_female.setText(_translate("Zap_Step1", "Ж"))
        self.label_5.setText(_translate("Zap_Step1", "Пол"))
        self.label_2.setText(_translate("Zap_Step1", "Фамилия"))
        self.radioButton_male.setText(_translate("Zap_Step1", "М"))
        self.label.setText(_translate("Zap_Step1", "Заполните анкету"))
        self.label_7.setText(_translate("Zap_Step1", "Дата рождения"))
        self.label_8.setText(_translate("Zap_Step1", "Телефон"))
        self.label_9.setText(_translate("Zap_Step1", "Место рождения"))
        self.label_10.setText(_translate("Zap_Step1", "Общежитие"))
        self.radioButton_yes.setText(_translate("Zap_Step1", "Да"))
        self.radioButton_no.setText(_translate("Zap_Step1", "Нет"))
        self.label_11.setText(_translate("Zap_Step1", "Фотография"))
        self.btn_load_photo.setText(_translate("Zap_Step1", "Загрузить"))
        self.btn_next.setText(_translate("Zap_Step1", "Далее"))
