from PyQt4 import QtGui 
from PyQt4.QtCore import pyqtSlot, Qt
from datetime import date
import re

class Main_window(QtGui.QWidget):
    def __init__(self):
        super(Main_window, self).__init__()
        self.initUI()

    def initUI(self):
        QtGui.QToolTip.setFont(QtGui.QFont('SansSerif', 10))
        self.setToolTip('This is a <b>QWidget</b> widget')
        self.btn = QtGui.QPushButton('Button', self)
        self.btn.setToolTip('This is a <b>QPushButton</b> widget')
        self.btn.resize(self.btn.sizeHint())
        self.first_name_line_edit = QtGui.QLineEdit()
        self.second_name_line_edit = QtGui.QLineEdit()
        self.birthday_date_line_edit = QtGui.QDateEdit()
        self.nameday_date_line_edit = QtGui.QDateEdit()
        self.mail_line_edit = QtGui.QLineEdit()
        self.tel_number_line_edit = QtGui.QLineEdit()
        self.facebook_line_edit = QtGui.QLineEdit()
        self.btn.clicked.connect(self.btn_on_clicked)
        self.resize(500, 500)
        self.center()
        self.setWindowTitle('WishBot')
        self.initform()
        self.show()

    def initform(self):
        self.form_layout = QtGui.QFormLayout(self)
        self.form_layout.addRow("*&First name:", self.first_name_line_edit)
        self.form_layout.addRow("*&Second name:", self.second_name_line_edit)
        self.form_layout.addRow("*&Birthday date (YYYY:MM:DD):", self.birthday_date_line_edit)
        self.form_layout.addRow("*&Nameday date:", self.nameday_date_line_edit)
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
        if not self.first_name_line_edit.text():
            print("first name is empty")
        if not self.second_name_line_edit.text():
            print("second name is empty")
        if not self.birthday_date_line_edit.text():
            print("birthday date is empty")
        else: 
            if correct_date_test(self.birthday_date_line_edit.text()) == False:
                print("incorrect birthday date format")
        if not self.mail_line_edit.text() and not self.tel_number_line_edit.text() and not self.facebook_line_edit.text():
            print('at least one of: "mail, tel. number, facebook address" has to be filled')

def correct_date_test(date_test):
    person_date = re.compile(r'^(\d\d\d\d):(\d\d):(\d\d)$').match(date_test)
    if not person_date:
        return False
    today_date = re.compile(r'^(\d\d\d\d)-\d\d-\d\d$').match(str(date.today())) 
    yyyy = int(person_date.group(1))
    mm = int(person_date.group(2))
    dd = int(person_date.group(3))
    if yyyy > int(today_date.group(1)) or mm > 12: 
        return False
    if ((mm%2 == 0 and mm <= 7 and dd > 30) or (mm%2 == 0 and mm>= 8 and dd > 31) or 
        (mm%2 == 1 and mm <= 7 and dd > 31) or (mm%2 == 1 and mm>= 8 and dd > 30) or 
        (mm == 4 and yyyy%4 == 0 and dd > 29) or (mm == 4 and yyyy%4 != 0 and dd > 28)):
        return False
    return True
