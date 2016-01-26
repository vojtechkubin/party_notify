import sys
from main_window import Main_window
from PyQt4 import QtGui


def main():
    """Skusam sa to rozbit"""

    app = QtGui.QApplication(sys.argv)
    app.setStyle(QtGui.QStyleFactory.create("plastique"))
    window = Main_window()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
