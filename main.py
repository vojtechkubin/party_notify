import sys
import fake_db
from datetime import date
from person import Person
from main_window import Main_window
from PyQt4 import QtGui


def main():

    app = QtGui.QApplication(sys.argv)
    window = Main_window()
    sys.exit(app.exec_())
    '''
    data = (fake_db.load('data.json'))
    data2 = {}
    persona = Person('first_name', 'second_name', str(date.today()), 'kokos', 'mail@hacking.fg', '777999555', 'facebook')
    data2['persona'] = persona
    data2['personb'] = persona
    fake_db.save(data2, 'data2.json')
    '''

if __name__ == '__main__':
    main()
