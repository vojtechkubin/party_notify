from PyQt4.QtCore import pyqtSlot
from PyQt4 import QtGui

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
        self.form_layout = QtGui.QFormLayout(self)
        self.first_name_line_edit = QtGui.QLineEdit()
        self.form_layout.addRow("&First name:", self.first_name_line_edit)
        self.second_name_line_edit = QtGui.QLineEdit()
        self.form_layout.addRow("&Second name:", self.second_name_line_edit)
        self.birthday_date_line_edit = QtGui.QLineEdit()
        self.form_layout.addRow("&Birthday date:", self.birthday_date_line_edit)
        self.form_layout.addRow("", self.btn)
        self.btn.clicked.connect(self.btn_on_clicked)
        self.resize(500, 500)
        self.center()
        self.setWindowTitle('WishBot')
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    @pyqtSlot()
    def btn_on_clicked(self):
        if not self.first_name_line_edit.text():
            print("first name is empty")
