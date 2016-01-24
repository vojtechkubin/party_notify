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
        self.initElements()
        self.initform()

        self.resize(500, 500)
        self.center()
        self.setWindowTitle('WishBot')

        self.show()

    def initElements(self):
        self.btn = QtGui.QPushButton('Submit', self)
        self.btn.resize(self.btn.sizeHint())
        self.btn.clicked.connect(self.btn_on_clicked)

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

    def initform(self):
        self.form_layout = QtGui.QFormLayout(self)
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
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return:
            #if the pressed key == ENTER -> button has been clicked
            self.btn_on_clicked()

    @pyqtSlot()
    def btn_on_clicked(self):

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
            print("naplnění dtb")
            print(first_name, second_name, mail, tel_number, facebook, birthday_date, nameday_date)
            new_person = Person(first_name, second_name, birthday_date, nameday_date, mail, tel_number, facebook)
            self.db.append(new_person)
            print("actual data", self.db)
