from PyQt4 import QtGui

class Main_window(QtGui.QWidget):
    def __init__(self):
        super(Main_window, self).__init__()

        self.initUI()

    def initUI(self):
        QtGui.QToolTip.setFont(QtGui.QFont('SansSerif', 10))
        self.setToolTip('This is a <b>QWidget</b> widget')
        btn = QtGui.QPushButton('Button', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        btn.resize(btn.sizeHint())
        btn.move(50, 50)
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Tooltips')
        self.show()
