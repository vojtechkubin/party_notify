# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created: Mon Jan 25 22:27:41 2016
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_StackedWidget(object):
    def setupUi(self, StackedWidget):
        StackedWidget.setObjectName(_fromUtf8("StackedWidget"))
        StackedWidget.resize(545, 397)
        self.Page0 = QtGui.QWidget()
        self.Page0.setObjectName(_fromUtf8("Page0"))
        self.gridLayout_2 = QtGui.QGridLayout(self.Page0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setMargin(15)
        self.gridLayout.setSpacing(10)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.pushButton_3 = QtGui.QPushButton(self.Page0)
        self.pushButton_3.setText(_fromUtf8(""))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.gridLayout.addWidget(self.pushButton_3, 1, 3, 1, 1)
        self.pushButton = QtGui.QPushButton(self.Page0)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout.addWidget(self.pushButton, 1, 1, 1, 1)
        self.pushButton_2 = QtGui.QPushButton(self.Page0)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.gridLayout.addWidget(self.pushButton_2, 2, 1, 1, 1)
        self.pushButton_4 = QtGui.QPushButton(self.Page0)
        self.pushButton_4.setText(_fromUtf8(""))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.gridLayout.addWidget(self.pushButton_4, 2, 3, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 1, 1, 1)
        StackedWidget.addWidget(self.Page0)
        self.Page1 = QtGui.QWidget()
        self.Page1.setObjectName(_fromUtf8("Page1"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.Page1)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.ExpandingFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.FirstNameLabel = QtGui.QLabel(self.Page1)
        self.FirstNameLabel.setObjectName(_fromUtf8("FirstNameLabel"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.FirstNameLabel)
        self.FirstNameLineEdit = QtGui.QLineEdit(self.Page1)
        self.FirstNameLineEdit.setObjectName(_fromUtf8("FirstNameLineEdit"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.FirstNameLineEdit)
        self.secondNameLabel = QtGui.QLabel(self.Page1)
        self.secondNameLabel.setObjectName(_fromUtf8("secondNameLabel"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.secondNameLabel)
        self.secondNameLineEdit = QtGui.QLineEdit(self.Page1)
        self.secondNameLineEdit.setObjectName(_fromUtf8("secondNameLineEdit"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.secondNameLineEdit)
        self.birthdayDateLabel = QtGui.QLabel(self.Page1)
        self.birthdayDateLabel.setObjectName(_fromUtf8("birthdayDateLabel"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.birthdayDateLabel)
        self.birthdayDateDateEdit = QtGui.QDateEdit(self.Page1)
        self.birthdayDateDateEdit.setCalendarPopup(True)
        self.birthdayDateDateEdit.setObjectName(_fromUtf8("birthdayDateDateEdit"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.birthdayDateDateEdit)
        self.namedayDateLabel = QtGui.QLabel(self.Page1)
        self.namedayDateLabel.setObjectName(_fromUtf8("namedayDateLabel"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.namedayDateLabel)
        self.namedayDateDateEdit = QtGui.QDateEdit(self.Page1)
        self.namedayDateDateEdit.setCalendarPopup(True)
        self.namedayDateDateEdit.setObjectName(_fromUtf8("namedayDateDateEdit"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.namedayDateDateEdit)
        self.mailAddressLabel = QtGui.QLabel(self.Page1)
        self.mailAddressLabel.setObjectName(_fromUtf8("mailAddressLabel"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.LabelRole, self.mailAddressLabel)
        self.mailAddressLineEdit = QtGui.QLineEdit(self.Page1)
        self.mailAddressLineEdit.setObjectName(_fromUtf8("mailAddressLineEdit"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.FieldRole, self.mailAddressLineEdit)
        self.telNumberLabel = QtGui.QLabel(self.Page1)
        self.telNumberLabel.setObjectName(_fromUtf8("telNumberLabel"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.LabelRole, self.telNumberLabel)
        self.telNumberLineEdit = QtGui.QLineEdit(self.Page1)
        self.telNumberLineEdit.setObjectName(_fromUtf8("telNumberLineEdit"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.FieldRole, self.telNumberLineEdit)
        self.facebookAddressLabel = QtGui.QLabel(self.Page1)
        self.facebookAddressLabel.setObjectName(_fromUtf8("facebookAddressLabel"))
        self.formLayout.setWidget(7, QtGui.QFormLayout.LabelRole, self.facebookAddressLabel)
        self.facebookAddressLineEdit = QtGui.QLineEdit(self.Page1)
        self.facebookAddressLineEdit.setObjectName(_fromUtf8("facebookAddressLineEdit"))
        self.formLayout.setWidget(7, QtGui.QFormLayout.FieldRole, self.facebookAddressLineEdit)
        self.newPersonSubmit = QtGui.QPushButton(self.Page1)
        self.newPersonSubmit.setObjectName(_fromUtf8("newPersonSubmit"))
        self.formLayout.setWidget(8, QtGui.QFormLayout.FieldRole, self.newPersonSubmit)
        self.horizontalLayout.addLayout(self.formLayout)
        StackedWidget.addWidget(self.Page1)
        self.actionAdd_new_person = QtGui.QAction(StackedWidget)
        self.actionAdd_new_person.setObjectName(_fromUtf8("actionAdd_new_person"))

        self.retranslateUi(StackedWidget)
        StackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(StackedWidget)
        StackedWidget.setTabOrder(self.pushButton, self.pushButton_3)
        StackedWidget.setTabOrder(self.pushButton_3, self.pushButton_2)
        StackedWidget.setTabOrder(self.pushButton_2, self.pushButton_4)
        StackedWidget.setTabOrder(self.pushButton_4, self.FirstNameLineEdit)
        StackedWidget.setTabOrder(self.FirstNameLineEdit, self.secondNameLineEdit)
        StackedWidget.setTabOrder(self.secondNameLineEdit, self.birthdayDateDateEdit)
        StackedWidget.setTabOrder(self.birthdayDateDateEdit, self.namedayDateDateEdit)
        StackedWidget.setTabOrder(self.namedayDateDateEdit, self.mailAddressLineEdit)
        StackedWidget.setTabOrder(self.mailAddressLineEdit, self.telNumberLineEdit)
        StackedWidget.setTabOrder(self.telNumberLineEdit, self.facebookAddressLineEdit)
        StackedWidget.setTabOrder(self.facebookAddressLineEdit, self.newPersonSubmit)

    def retranslateUi(self, StackedWidget):
        StackedWidget.setWindowTitle(_translate("StackedWidget", "StackedWidget", None))
        self.pushButton.setText(_translate("StackedWidget", "New person", None))
        self.pushButton_2.setText(_translate("StackedWidget", "Edit/Delete person", None))
        self.FirstNameLabel.setText(_translate("StackedWidget", "First name:", None))
        self.secondNameLabel.setText(_translate("StackedWidget", "Second name:", None))
        self.birthdayDateLabel.setText(_translate("StackedWidget", "Birthday date:", None))
        self.namedayDateLabel.setText(_translate("StackedWidget", "Nameday date:", None))
        self.namedayDateDateEdit.setDisplayFormat(_translate("StackedWidget", "d.M", None))
        self.mailAddressLabel.setText(_translate("StackedWidget", "Mail address:", None))
        self.telNumberLabel.setText(_translate("StackedWidget", "Tel. number:", None))
        self.facebookAddressLabel.setText(_translate("StackedWidget", "Facebook address:", None))
        self.newPersonSubmit.setText(_translate("StackedWidget", "Submit", None))
        self.actionAdd_new_person.setText(_translate("StackedWidget", "Add new person", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    StackedWidget = QtGui.QStackedWidget()
    ui = Ui_StackedWidget()
    ui.setupUi(StackedWidget)
    StackedWidget.show()
    sys.exit(app.exec_())

