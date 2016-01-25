from PyQt4 import QtGui
from PyQt4.QtCore import pyqtSlot, Qt, QDate
from datetime import date
from person import Person
import fake_db

class Main_window(QtGui.QWidget):
    def __init__(self):
        super(Main_window, self).__init__()
        self.initUI()
        self.db = fake_db.load("data.json")

    def initUI(self):
        self.stackedLayout = QtGui.QStackedLayout(self)

        self.widget1 = QtGui.QWidget()
        self.widget2 = QtGui.QWidget()

        self.initElements_person_add()
        self.initform_person_add()
        self.initElements_menu()

        self.stackedLayout.addWidget(self.widget1)
        self.stackedLayout.addWidget(self.widget2)
        self.stackedLayout.widget(0).show()

        self.resize(500, 500)
        self.center()
        self.setWindowTitle('WishBot')

        self.show()

    def initElements_menu(self):
        self.menu_layout = QtGui.QVBoxLayout(self.widget1)
        self.buttons_layout = QtGui.QHBoxLayout()
        self.label_layout = QtGui.QHBoxLayout()
        self.left_layout = QtGui.QVBoxLayout()
        self.right_layout = QtGui.QVBoxLayout()
        self.menu_lbl = QtGui.QLabel('Main menu')

#--------------------left-------------------------------------------
        self.new_p_btn = QtGui.QPushButton('&New person', self)
        self.new_p_btn.resize(self.new_p_btn.sizeHint())
        self.new_p_btn.clicked.connect(self.new_p_btn_click)

        self.change_p_btn = QtGui.QPushButton('&Change person', self)
        self.change_p_btn.resize(self.change_p_btn.sizeHint())

        self.delete_p_btn = QtGui.QPushButton('&Delete person', self)
        self.delete_p_btn.resize(self.delete_p_btn.sizeHint())

#-------------------right--------------------------------------------
        self.new_db_btn = QtGui.QPushButton('&New database', self)
        self.new_db_btn.resize(self.new_db_btn.sizeHint())

        self.change_db_btn = QtGui.QPushButton('&Change database', self)
        self.change_db_btn.resize(self.change_db_btn.sizeHint())

        self.delete_db_btn = QtGui.QPushButton('&Delete database', self)
        self.delete_db_btn.resize(self.delete_db_btn.sizeHint())

        self.menu_layout.addLayout(self.label_layout)
        self.menu_layout.addLayout(self.buttons_layout)
        self.menu_layout.addStretch(1)

        self.label_layout.addStretch(1)
        self.label_layout.addWidget(self.menu_lbl)
        self.label_layout.addStretch(1)

        self.left_layout.addWidget(self.new_p_btn)
        self.left_layout.addWidget(self.change_p_btn)
        self.left_layout.addWidget(self.delete_p_btn)
        self.buttons_layout.addLayout(self.left_layout)

        self.right_layout.addWidget(self.new_db_btn)
        self.right_layout.addWidget(self.change_db_btn)
        self.right_layout.addWidget(self.delete_db_btn)
        self.buttons_layout.addLayout(self.right_layout)

    def initElements_person_add(self):
        self.btn = QtGui.QPushButton('Submit', self)
        self.btn.resize(self.btn.sizeHint())
        self.btn.clicked.connect(self.form_on_clicked)

        self.first_name_line_edit = QtGui.QLineEdit()

        self.second_name_line_edit = QtGui.QLineEdit()

        self.birthday_date_line_edit = QtGui.QDateEdit()
        self.birthday_date_line_edit.setDisplayFormat("dd.MM.yyyy")
        self.birthday_date_line_edit.setCalendarPopup(True)
        self.birthday_date_line_edit.setDate(QDate.currentDate())

        self.nameday_date_line_edit = QtGui.QDateEdit()
        self.nameday_date_line_edit.setDisplayFormat("dd.MM")
        self.nameday_date_line_edit.setCalendarPopup(True)
        self.nameday_date_line_edit.setDate(QDate.currentDate())

        self.mail_line_edit = QtGui.QLineEdit()

        self.tel_number_line_edit = QtGui.QLineEdit()

        self.facebook_line_edit = QtGui.QLineEdit()

    def initform_person_add(self):
        self.form_layout = QtGui.QFormLayout(self.widget2)
        self.form_layout.addRow("*&First name:", self.first_name_line_edit)
        self.form_layout.addRow("*&Second name:", self.second_name_line_edit)
        self.form_layout.addRow("*&Birthday date (DD.MM.YYYY):", self.birthday_date_line_edit)
        self.form_layout.addRow("*&Nameday date (DD.MM):", self.nameday_date_line_edit)
        self.form_layout.addRow("&Mail address:", self.mail_line_edit)
        self.form_layout.addRow("&Tel. number:", self.tel_number_line_edit)
        self.form_layout.addRow("&Facebook address:", self.facebook_line_edit)
        self.form_layout.addRow("", self.btn)

    def center(self):
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    @pyqtSlot()
    def new_p_btn_click(self):
        self.stackedLayout.widget(0).hide()
        self.stackedLayout.widget(1).show()

    @pyqtSlot()
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return:
            #if the pressed key == ENTER -> button has been clicked
            self.btn_on_clicked()

    @pyqtSlot()
    def form_on_clicked(self):

        first_name = self.first_name_line_edit.text()
        second_name = self.second_name_line_edit.text()
        mail = self.mail_line_edit.text()
        tel_number = self.tel_number_line_edit.text()
        facebook = self.facebook_line_edit.text()
        birthday_date = self.birthday_date_line_edit.text()
        nameday_date = self.nameday_date_line_edit.text()

        error = []
        if not first_name:
            error.append('first name is empty')
        if not second_name:
            error.append('second name is empty')
        if not mail and not tel_number and not facebook:
            error.append('at least one of: "mail, tel. number, facebook address" has to be filled')
        if error != []:
            print(error)
        else:
            #naplnění db
            new_person = Person(first_name, second_name, birthday_date, nameday_date, mail, tel_number, facebook)
            self.db.append(new_person)
