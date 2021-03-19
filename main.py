from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5 import QtWidgets, QtGui, QtCore
import sqlite3
from reg import *
from join import *
from Results_Table import *
from startwindow import *
from check import *
import sys
import os
from student_room import *
from contacts import *
from menu import *
from Zap_Step1 import *
from Zap_Step2 import *
from Zap_Step3 import *
from Zap_Step4 import *
import smtplib

yandex_mail = 'info40.sgu@mail.ru'
yandex_pass = 'Team40SGU'


def send_emails(mail, msg):
    server = smtplib.SMTP_SSL('smtp.mail.ru', 465)
    server.ehlo(yandex_mail)
    server.login('info40.sgu@mail.ru', 'Team40SGU')
    server.auth_plain()
    send_to_email = mail
    server.login(yandex_mail, yandex_pass)
    server.sendmail(yandex_mail, send_to_email, msg)
    server.quit()
    print('E-mails successfully sent!')


class CheckWindow(QMainWindow, Ui_Check):
    def __init__(self, path, user):
        self.user = user
        self.path = path
        super().__init__()
        self.setupUi(self)
        self.con = sqlite3.connect(self.path)
        self.curs = self.con.cursor()
        try:
            self.data = self.curs.execute(
                f"""SELECT photo_path, agree_path, agree_join_path from Anket WHERE id = {self.user}""").fetchall()[0]
        except Exception as ex:
            self.data = ('', '', '')
        print(self.data)
        self.personal_photo.clicked.connect(self.shw_pers_photo)
        self.paper_photo.clicked.connect(self.shw_paper_photo)
        self.agree_photo.clicked.connect(self.shw_ag_photo)
        self.tabel_photo.clicked.connect(self.shw_tb_photo)
        self.achives_photo.clicked.connect(self.shw_ach_photo)
        self.join_agree_photo.clicked.connect(self.shw_join_photo)

        self.radioButton_bad.clicked.connect(self.unblocking)
        self.radioButton_good.clicked.connect(self.unblocking)

        self.checkbox_base = [self.checkBox, self.checkBox_2, self.checkBox_3, self.checkBox_4, self.checkBox_5,
                              self.checkBox_6]

        self.btn_back.clicked.connect(self.go_to_main)
        self.btn_send.clicked.connect(self.sending)

        self.fio = self.curs.execute(
            f"""SELECT FIO from UserForm WHERE id = {self.user}""").fetchone()[0]
        self.label_FIO.setText(self.fio)
        self.mail = self.curs.execute(
            f"""SELECT email from UserForm WHERE id = {self.user}""").fetchall()[0]

    def sending(self):
        self.wrongs = []
        if self.radioButton_bad.isChecked():
            for box in self.checkbox_base:
                if box.isChecked():
                    self.wrongs.append(box.text())
            self.curs.execute(
                f"""UPDATE UserForm set level = 'Отправлено на доработку' WHERE id = {self.user}"""
            )
            self.con.commit()
            # отправка письма с ошибками

            message = f"""Добрый день, {self.fio}!
Уведомляем вас, что при подаче документов в Сызранский государственный университет имени Филиппа Лимонадова вы допустили ошибки в:
            {', '.join(self.wrongs)} 
Просим исправить ошибки в ближайшее время.
С уважением,
приемная комиссия СГУ им. Ф.Лимонадова"""

            message = message.encode("utf-8")

            mail = self.mail

            send_emails(mail, message)

        else:
            # отправка письма об участии

            message = f"""Добрый день, {self.fio}!
Уведомляем вас, что вы успешно подали документы в Сызранский государственный университет имени Филиппа Лимонадова. С этого момента вы участвуете в конкурсе на зачисление.
С уважением,
приемная комиссия СГУ им. Ф.Лимонадова"""
            message = message.encode("utf-8")

            mail = self.mail

            send_emails(mail, message)

            self.curs.execute(
                f"""UPDATE UserForm set level = 'Принято' WHERE id = {self.user}"""
            )
            self.con.commit()

    def go_to_main(self):
        try:
            self.win = UI_Komissia("DATABASE.db")
            self.close()
            self.win.show()

        except Exception as er:
            print(er)

    def unblocking(self):
        if self.radioButton_bad.isChecked():
            for box in self.checkbox_base:
                box.setEnabled(1)
        else:
            for box in self.checkbox_base:
                box.setDisabled(1)

    def shw_pers_photo(self):
        if self.data[0]:
            self.ex = Example(self.data[0])
            self.ex.show()
        else:
            info = QMessageBox.information(self, "Message", "Пользователь не загрузил эти данные")

    def shw_ag_photo(self):
        if self.data[1]:
            self.ex = Example(self.data[1])
            self.ex.show()
        else:
            info = QMessageBox.information(self, "Message", "Пользователь не загрузил эти данные")

    def shw_join_photo(self):
        if self.data[2]:
            self.ex = Example(self.data[2])
            self.ex.show()
        else:
            info = QMessageBox.information(self, "Message", "Пользователь не загрузил эти данные")

    def shw_paper_photo(self):
        dt = self.curs.execute("""Select photo_path from paper where id = 1""").fetchall()[0][0]
        if dt:
            self.ex = Example(dt)
            self.ex.show()

        else:
            info = QMessageBox.information(self, "Message", "Пользователь не загрузил эти данные")

    def shw_tb_photo(self):
        try:
            dt = self.curs.execute("""Select photo_path from Education where id = 1""").fetchall()[0][0]
            if dt:
                self.ex = Example(dt)
                self.ex.show()
            else:
                info = QMessageBox.information(self, "Message", "Пользователь не загрузил эти данные")
        except Exception as er:
            print(er)

    def shw_ach_photo(self):
        try:
            dt = self.curs.execute("""Select photo_path from Achives where id = 1""").fetchall()[0][0]
            if dt:
                self.ex = Example(dt)
                self.ex.show()
            else:
                info = QMessageBox.information(self, "Message", "Пользователь не загрузил эти данные")

        except Exception as er:
            print(er)


class Results_Table(QMainWindow, Ui_Results_Table):
    def __init__(self, path):
        self.path = path
        super().__init__()
        self.setupUi(self)
        self.con = sqlite3.connect(self.path)
        self.cur = self.con.cursor()

        self.btn_go_to_main.clicked.connect(self.go_to_main)
        self.comboBox.activated.connect(self.get_data)
        # self.user_id = self.cur.execute("""Select PersonalData from Anket""").fetchall()[0]
        # self.exam = self.cur.execute("""Select Exams from Anket""").fetchall()[0]
        # self.ach = self.cur.execute("Select Achives from Anket").fetchall()[0]
        # self.cp = self.cur.execute("Select copy from Anket").fetchall()[0]

    def get_data(self):
        try:
            self.brch = self.cur.execute(
                """Select id from Branches where name = "{}"  """.format(self.comboBox.currentText())).fetchall()[0][0]
            self.need = self.cur.execute(
                """Select need from Branches where name = "{}" """.format(self.comboBox.currentText())).fetchall()[0][0]

            self.data = self.cur.execute(
                """Select PersonalData, Exams, Achives, copy from Anket WHERE Branch = {}""".format(
                    self.brch)).fetchall()
            self.items = []
            for i in self.data:
                self.FIO = \
                    self.cur.execute("""Select FIO from UserForm WHERE id = {}""".format(i[0])).fetchall()[0][0]
                self.ach = \
                    self.cur.execute("""Select price from Achives where id = {}""".format(i[2])).fetchall()[0][0]
                if i[3]:
                    self.cp = "Да"
                else:
                    self.cp = "Нет"
                self.ex = self.cur.execute(
                    """Select rus, math, "{}" from Exams where id = {} """.format(self.need, i[1])).fetchall()[0]
                self.summ = sum(self.ex)
                self.items.append((self.FIO, self.summ, self.ach, self.cp))
                self.tableWidget.setRowCount(0)
                n = len(self.items)
                self.tableWidget.setRowCount(n)
                for j in range(n):
                    self.tableWidget.setItem(j, 0, QTableWidgetItem())
                    self.tableWidget.setItem(j, 1, QTableWidgetItem())
                    self.tableWidget.setItem(j, 2, QTableWidgetItem())
                    self.tableWidget.setItem(j, 3, QTableWidgetItem())

                    self.tableWidget.item(j, 0).setText(self.items[j][0])
                    self.tableWidget.item(j, 1).setText(str(self.items[j][1]))
                    self.tableWidget.item(j, 2).setText(str(self.items[j][2]))
                    self.tableWidget.item(j, 3).setText(self.items[j][3])

        except Exception as er:
            print(er)

    def go_to_main(self):
        try:
            self.win = UI_Komissia("DATABASE.db")
            self.close()
            self.win.show()

        except Exception as er:
            print(er)


class UI_Komissia(QMainWindow, Ui_Komissia):
    def __init__(self, path):
        self.path = path
        super().__init__()
        self.setupUi(self)

        self.conn = sqlite3.connect(self.path)
        self.curs = self.conn.cursor()
        # self.tableWidget.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        # self.tableWidget.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        # self.tableWidget.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        # self.tableWidget.horizontalHeader().setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)
        # self.tableWidget.horizontalHeader().setSectionResizeMode(4, QtWidgets.QHeaderView.Stretch)
        # self.tableWidget.horizontalHeader().setSectionResizeMode(5, QtWidgets.QHeaderView.Stretch)
        self.update_data()
        self.tableWidget.cellClicked.connect(self.student)

        self.btn_go_to_tables.clicked.connect(self.go_to_tables)
        self.btn_go_to_zach.clicked.connect(self.go_to_zach)

        self.student_status = 'Новый'

    def go_to_tables(self):
        try:
            self.win = Results_Table("DATABASE.db")
            self.close()
            self.win.show()
        except Exception as er:
            print(er)

    def go_to_zach(self):
        pass

    def update_data(self):
        self.data = self.curs.execute(
            """Select id, FIO, sex, email, phone_number from UserForm""").fetchall()
        self.update_table()

    def update_table(self):
        self.tableWidget.setRowCount(0)

        n = len(self.data)
        self.tableWidget.setRowCount(n)
        for i in range(n):
            self.tableWidget.setItem(i, 0, QTableWidgetItem())
            self.tableWidget.setItem(i, 1, QTableWidgetItem())
            self.tableWidget.setItem(i, 2, QTableWidgetItem())
            self.tableWidget.setItem(i, 3, QTableWidgetItem())
            self.tableWidget.setItem(i, 4, QTableWidgetItem())

            self.tableWidget.item(i, 0).setText(str(self.data[i][0]))
            self.tableWidget.item(i, 1).setText(self.data[i][1])
            self.tableWidget.item(i, 2).setText(str(self.data[i][2]))
            self.tableWidget.item(i, 3).setText(self.data[i][3])
            self.tableWidget.item(i, 4).setText(str(self.data[i][4]))

        for i in range(n):
            self.anketa = self.curs.execute(
                f"""Select Address, Paper, PersonalData, Education, agree_path, edu_form, branch, Exams, Achives, birthday, place_of_birth, phone_number, photo_path, campus, copy, agree_join_path from Anket where id='{i + 1}'""").fetchone()

            kol = 0
            self.level = self.curs.execute(
                f"""Select level from UserForm WHERE id = {i + 1}""").fetchone()[0]

            if self.level == None:
                self.level = 'Новый'

            if self.anketa:
                for j in self.anketa:
                    if j:
                        kol += 1

                if kol == len(self.anketa):
                    self.student_status = 'Полный комплект'
                    if self.level == 'Новый':
                        self.level = 'На рассмотрении'
                elif ((kol == len(self.anketa) - 1) or (kol == len(self.anketa) - 1)) and (
                        (not self.anketa[-1]) or (not self.anketa[-2])):
                    self.student_status = 'Комплект без оригинала'
                elif kol > 0:
                    self.student_status = 'В работе'
                else:
                    self.student_status = 'Новый'
            else:
                self.student_status = 'Новый'

            self.curs.execute(
                f"""UPDATE UserForm set level = '{self.level}' WHERE id = {i + 1}"""
            )
            self.conn.commit()

            self.tableWidget.setItem(i, 5, QTableWidgetItem())
            self.tableWidget.item(i, 5).setText(self.student_status)

            self.tableWidget.setItem(i, 6, QTableWidgetItem())
            self.tableWidget.item(i, 6).setText(self.level)

    def student(self):
        try:
            self.win = CheckWindow("DATABASE.db", int(self.tableWidget.item(self.tableWidget.currentRow(), 0).text()))
            self.close()
            self.win.show()
        except Exception as error:
            print(error)


class Example(QWidget):

    def __init__(self, path):
        self.path = path
        super().__init__()

        self.initUI()

    def initUI(self):
        hbox = QHBoxLayout(self)
        pixmap = QtGui.QPixmap(self.path)

        lbl = QLabel(self)
        lbl.setPixmap(pixmap)

        hbox.addWidget(lbl)
        self.setLayout(hbox)

        self.move(300, 200)
        self.setWindowTitle('Photo')
        self.show()


class Contacts(QMainWindow, Ui_Contacts):
    def __init__(self, facultet):
        self.facultet = facultet
        super(Contacts, self).__init__()
        self.setupUi(self)
        if self.facultet == 1:
            self.lbl_decan.setText("""Декан - Пупкин Василий Эдуардович 
(телефон 8 (800) 000-00-01, E-mail - pupkin.v.sgu@yandex.ru) 
Зам. декана - Прекрасная Василиса Ивановна 
(телефон 8 (800) 000-00-02, E-mail - prekrasnaya.v.sgu@yandex.ru) 
Секретарь - Секретарев Дмитрий Борисович 
(телефон 8 (800) 000-00-03, E-mail - sekretarev.d.sgu@yandex.ru) 
Секретарь - Ухов Евгений Олегович 
(телефон 8 (800) 000-00-04, E-mail - uhov.e.sgu@yandex.ru) 
""")
        elif self.facultet == 2:
            self.lbl_decan.setText(""" Декан - Иванов Иван Иванович
                                   (телефон 8 (800) 001-00-01, E-mail - ivanov.i.sgu@yandex.ru)
            Зам. декана - Сидоров Сергей Петрович
            (телефон 8 (800) 001-00-02, E-mail - sidorov.s.sgu@yandex.ru)
            Секретарь - Петрова Ирина Викторовна
            (телефон 8 (800) 001-00-03, E-mail - petrova.i.sgu@yandex.ru)
            """)


class Student_Room(QMainWindow, Ui_Student_Room):
    def __init__(self, path, user):
        self.path = path
        self.user = user
        super(Student_Room, self).__init__()
        self.setupUi(self)
        self.con = sqlite3.connect(self.path)
        self.curs = self.con.cursor()
        self.branch = self.curs.execute(f"""Select name FROM Branches Where id = {self.user[0]}""").fetchall()[0][0]
        self.facultet = self.curs.execute(f"""Select name FROM Facultets Where id = {self.user[1]}""").fetchall()[0][0]
        self.group = self.curs.execute(f"""Select name FROM Groups Where id = {self.user[2]}""").fetchall()[0][0]
        print(self.group, self.branch, self.facultet)
        self.lbl_branch.setText(self.branch)
        self.lbl_fuck.setText(self.facultet)
        self.lbl_group.setText(str(self.group))
        self.btn_info.clicked.connect(self.inf)
        self.btn_timetable.clicked.connect(self.schedule)

        self.tableWidget.cellClicked.connect(self.show_photo)

        self.update_data()
        # Мы берём БВИ Мы берём БВИ Мы берём БВИ Мы берём БВИ Мы берём БВИ Мы берём БВИ Мы берём БВИ Мы берём БВИ
        # Мы призёры Мы призёры Мы призёры АБП Мы призёры АБП Мы призёры АБП Мы призёры АБП Мы призёры АБП
        # Поле название команды обязательно для заполнения - призёры
        # Поле название команды обязательно для заполнения - призёры
        # Поле название команды обязательно для заполнения - призёры
        # Поле название команды обязательно для заполнения - призёры
        # Поле название команды обязательно для заполнения - призёры
        # Поле название команды обязательно для заполнения - призёры
        # Поле название команды обязательно для заполнения - призёры
        # Поле название команды обязательно для заполнения - призёры
        # Поле название команды обязательно для заполнения - призёры
        # Поле название команды обязательно для заполнения - призёры
        # Поле название команды обязательно для заполнения - призёры
        # Поле название команды обязательно для заполнения - призёры
        # Поле название команды обязательно для заполнения - призёры
        # Поле название команды обязательно для заполнения - призёры
        # Поле название команды обязательно для заполнения - призёры
        # Поле название команды обязательно для заполнения - призёры
        # Поле название команды обязательно для заполнения - призёры
        # Поле название команды обязательно для заполнения - призёры
        # Поле название команды обязательно для заполнения - призёры
        # Поле название команды обязательно для заполнения - призёры
        # Поле название команды обязательно для заполнения - призёры
        # Поле название команды обязательно для заполнения - призёры
        # Поле название команды обязательно для заполнения - призёры
        # Поле название команды обязательно для заполнения - призёры
        # Поле название команды обязательно для заполнения - призёры
        # Поле название команды обязательно для заполнения - призёры
        # Поле название команды обязательно для заполнения - призёры
        # Поле название команды обязательно для заполнения - призёры
        # Поле название команды обязательно для заполнения - призёры
        # Поле название команды обязательно для заполнения - призёры
        # Поле название команды обязательно для заполнения - призёры
        # Поле название команды обязательно для заполнения - призёры
        # Поле название команды обязательно для заполнения - призёры
        # Поле название команды обязательно для заполнения - призёры
        # Поле название команды обязательно для заполнения - призёры
        # Поле название команды обязательно для заполнения - призёры
        # Поле название команды обязательно для заполнения - призёры
        # Поле название команды обязательно для заполнения - призёры
        # Поле название команды обязательно для заполнения - призёры
        # Поле название команды обязательно для заполнения - призёры
        # Поле название команды обязательно для заполнения - призёры
        # Поле название команды обязательно для заполнения - призёры
        # Поле название команды обязательно для заполнения - призёры
        # Поле название команды обязательно для заполнения - призёры
        # Поле название команды обязательно для заполнения - призёры
        # Поле название команды обязательно для заполнения - призёры
        # Поле название команды обязательно для заполнения - призёры
        # Поле название команды обязательно для заполнения - призёры
        # Поле название команды обязательно для заполнения - призёры
        # Поле название команды обязательно для заполнения - призёры
        # Поле название команды обязательно для заполнения - призёры
        # Поле название команды обязательно для заполнения - призёры
        # Поле название команды обязательно для заполнения - призёры
        # Поле название команды обязательно для заполнения - призёры
        # Поле название команды обязательно для заполнения - призёры

    def show_photo(self):
        if self.tableWidget.currentColumn() != 5:
            return
        else:
            self.path = self.tableWidget.item(self.tableWidget.currentRow(), 1).text().split()[0]
            print(self.path)
            self.ex = Example(f"Photos/{self.path}.jpg")
            self.ex.show()

    def update_data(self):
        self.data = self.curs.execute(
            """Select lesson, FIO, rang, profession, email from Teachers""").fetchall()
        self.update_table()

    def update_table(self):
        self.tableWidget.setRowCount(0)

        n = len(self.data)
        self.tableWidget.setRowCount(n)
        for i in range(n):
            self.tableWidget.setItem(i, 0, QTableWidgetItem())
            self.tableWidget.setItem(i, 1, QTableWidgetItem())
            self.tableWidget.setItem(i, 2, QTableWidgetItem())
            self.tableWidget.setItem(i, 3, QTableWidgetItem())
            self.tableWidget.setItem(i, 4, QTableWidgetItem())
            self.tableWidget.setItem(i, 5, QTableWidgetItem())

            self.tableWidget.item(i, 0).setText(str(self.data[i][0]))
            self.tableWidget.item(i, 1).setText(self.data[i][1])
            self.tableWidget.item(i, 2).setText(str(self.data[i][2]))
            self.tableWidget.item(i, 3).setText(self.data[i][3])
            self.tableWidget.item(i, 4).setText(str(self.data[i][4]))
            self.tableWidget.item(i, 5).setText("Открыть")

    def inf(self):
        try:
            self.ex = Contacts(self.facultet)
            self.ex.show()
        except Exception as er:
            print(er)

    def schedule(self):
        try:
            dt = self.curs.execute(f"""Select timetable from Groups where id = {self.user[2]}""").fetchall()[0][0]
            self.shed = Example(f"Photos/{dt}")
            self.shed.show()
        except Exception as er:
            print(er)


class Reg(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_Reg()
        self.ui.setupUi(self)

        self.ui.label_error.hide()

        self.ui.pushButton.clicked.connect(self.go_back)
        self.ui.btn_reg.clicked.connect(self.register)

    def go_back(self):
        try:
            self.win = Join(self)
            self.close()
            self.win.show()

        except Exception as er:
            print(er)

    def register(self):
        Name = None
        Surname = None
        Otch = None
        Sex = None
        Login = None
        Password = None

        if len(self.ui.edit_name.text()) > 0:
            Name = self.ui.edit_name.text()
        else:
            self.ui.label_error.show()
            return

        if len(self.ui.edit_surname.text()) > 0:
            Surname = self.ui.edit_surname.text()
        else:
            self.ui.label_error.show()
            return

        if len(self.ui.edit_dad.text()) > 0:
            Otch = self.ui.edit_dad.text()
        else:
            self.ui.label_error.show()
            return

        if len(self.ui.edit_mail.text()) > 0:
            Login = self.ui.edit_mail.text()
        else:
            self.ui.label_error.show()
            return

        if len(self.ui.edit_password.text()) > 0:
            Password = self.ui.edit_password.text()
        else:
            self.ui.label_error.show()
            return

        radio_base = [self.ui.radioButton_female, self.ui.radioButton_male]
        for rad in radio_base:
            if rad.isChecked():
                Sex = rad.text()

        if not Sex:
            self.ui.label_error.show()
            return

        try:
            con = sqlite3.connect("DATABASE.db")
            curs = con.cursor()
            curs.execute(
                f"""INSERT INTO UserForm(name, surname, otchestvo, password, email, sex) VALUES("{Name}", "{Surname}", "{Otch}", "{Password}", "{Login}", "{Sex}") """)
            con.commit()
            con.close()
        except sqlite3.IntegrityError:
            print("Этот email уже используется")

        try:
            self.win = Join(self)
            self.close()
            self.win.show()

        except Exception as er:
            print(er)


class Join(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_Join()
        self.ui.setupUi(self)

        self.ui.label_error.hide()

        self.ui.btn_join.clicked.connect(self.go_join)
        self.ui.btn_reg.clicked.connect(self.go_reg)

    def go_join(self):
        Login = None
        Password = None

        if len(self.ui.edit_login.text()) > 0:
            Login = self.ui.edit_login.text()
        else:
            self.ui.label_error.setText("Введите логин и пароль")
            self.ui.label_error.show()
            return

        if len(self.ui.edit_password.text()) > 0:
            Password = self.ui.edit_password.text()
        else:
            self.ui.label_error.setText("Введите логин и пароль")
            self.ui.label_error.show()
            return

        con = sqlite3.connect("DATABASE.db")
        curs = con.cursor()
        ex = curs.execute(
            """SELECT * FROM UserForm WHERE email = "{}" and password = "{}" """.format(Login, Password)).fetchone()

        if not ex:

            ex = curs.execute(
                """Select * FROM Join_party where name = '{}' and password = '{}'""".format(Login, Password)).fetchone()

            if not ex:
                ex = curs.execute("""Select * FROM Decanat where name = "{}" and password = "{}" """.format(Login,
                                                                                                            Password)).fetchone()
                if not ex:
                    self.ui.label_error.setText("Неверный логин или пароль")
                    self.ui.label_error.show()
                    return
                else:
                    pass  # Деканат
            else:
                try:
                    self.win = UI_Komissia("DATABASE.db")
                    self.close()
                    self.win.show()  # Приемная комиссия
                except Exception as excep:
                    print(excep)
        else:
            ex1 = curs.execute("""Select * FROM Students where FIO = {}""".format(ex[0])).fetchone()
            if not ex1:
                try:
                    self.win = Menu(self, person=ex)
                    self.close()
                    self.win.show()

                except Exception as er:
                    print(er)
            else:
                try:
                    fio = curs.execute(
                        """SELECT id FROM UserForm WHERE email = "{}" and password = "{}" """.format(Login,
                                                                                                     Password)).fetchall()[
                        0][0]

                    ex = \
                        curs.execute(f"""Select Branch, facultet, Groups from Students Where FIO = {fio}""").fetchall()[
                            0]

                    self.win = Student_Room("DATABASE.db", ex)
                    self.close()
                    self.win.show()  # Студенты
                except Exception as excep:
                    print(excep)

    def go_reg(self):
        try:
            self.win = Reg(self)
            self.close()
            self.win.show()

        except Exception as er:
            print(er)


class Zap_Step1(QtWidgets.QMainWindow):
    def __init__(self, parent=None, person=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_Zap_Step1()
        self.ui.setupUi(self)

        self.person = person
        self.file_path = None

        self.ui.btn_next.clicked.connect(self.go_next)

        self.ui.btn_load_photo.clicked.connect(self.load_photo)

    def load_photo(self):
        self.file_path = QtWidgets.QFileDialog.getOpenFileName(self, 'headers', 'filename')

    def go_next(self):

        radio_base_sex = [self.ui.radioButton_female, self.ui.radioButton_male]
        Surname = self.ui.edit_surname.text()
        Name = self.ui.edit_name.text()
        Otch = self.ui.edit_dad.text()
        Sex = None

        for i in radio_base_sex:
            if i.isChecked():
                Sex = i.text()
        Login = self.ui.edit_mail.text()
        Date = self.ui.edit_date.text()
        Phone = self.ui.edit_phone.text()
        Birth_place = self.ui.edit_birth_place.text()
        Life = None

        Photo = None
        Photo = self.file_path
        print('ok')
        radio_base_life = [self.ui.radioButton_yes, self.ui.radioButton_no]
        for i in radio_base_life:
            if i.isChecked():
                Life = i.text()

        id = self.person[0]

        con = sqlite3.connect("DATABASE.db")
        curs = con.cursor()
        try:
            curs.execute(
                f"""UPDATE UserForm SET FIO = "{Name} {Surname} {Otch}", sex = "{Sex}", email = "{Login}", birthday = "{Date}", place_of_birth = "{Birth_place}", phone_number = "{Phone}", photo_path = "{Photo}", campus = "{Life}" WHERE id = "{id}" """)  # если не будет работать, убери кавычки на id
            con.commit()
            con.close()
        except Exception as excep:
            print(excep)

        try:
            self.win = Zap_Step2(self, person=self.person)
            self.close()
            self.win.show()

        except Exception as er:
            print(er)


class Zap_Step3(QtWidgets.QMainWindow):
    def __init__(self, parent=None, person=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_Zap_Step3()
        self.ui.setupUi(self)

        self.person = person

        self.ui.btn_next.clicked.connect(self.go_next)

    def go_next(self):
        try:
            self.win = Zap_Step4(self, person=self.person)
            self.close()
            self.win.show()

        except Exception as er:
            print(er)


class Zap_Step4(QtWidgets.QMainWindow):
    def __init__(self, parent=None, person=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_Zap_Step4()
        self.ui.setupUi(self)

        self.person = person

        self.ui.btn_next.clicked.connect(self.go_next)

    def go_next(self):
        try:
            self.win = Menu(self, person=self.person)
            self.close()
            self.win.show()

        except Exception as er:
            print(er)


class Zap_Step2(QtWidgets.QMainWindow):
    def __init__(self, parent=None, person=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_Zap_Step2()
        self.ui.setupUi(self)

        self.person = person

        self.ui.btn_next.clicked.connect(self.go_next)

    def go_next(self):
        try:
            self.win = Zap_Step3(self, person=self.person)
            self.close()
            self.win.show()

        except Exception as er:
            print(er)


class Menu(QtWidgets.QMainWindow):
    def __init__(self, parent=None, person=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_Menu()
        self.ui.setupUi(self)

        self.con = sqlite3.connect("DATABASE.db")
        self.curs = self.con.cursor()

        self.person = person
        print(self.person)

        self.ui.pushButton.clicked.connect(self.go_zap)
        self.ui.pushButton_2.clicked.connect(self.go_watch)
        self.ui.pushButton_3.clicked.connect(self.go_change)

        self.ui.label.setText(self.person[1])

    def go_zap(self):
        try:
            self.win = Zap_Step1(self, person=self.person)
            self.close()
            self.win.show()

        except Exception as er:
            print(er)

    def go_watch(self):
        pass

    def go_change(self):
        pass


if __name__ == '__main__':
    try:
        app = QtWidgets.QApplication(sys.argv)
        myapp = Join()
        myapp.show()
        sys.exit(app.exec_())
    except Exception as ex:
        print(ex)
