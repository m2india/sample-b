# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'identicard.ui'
#
# Created: Wed Sep 26 14:26:25 2012
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setEnabled(True)
        Dialog.resize(724, 573)
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(200, 20, 301, 61))
        font = QtGui.QFont()
        font.setFamily("URW Palladio L")
        font.setPointSize(28)
        font.setWeight(75)
        font.setItalic(True)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.name = QtGui.QLabel(Dialog)
        self.name.setGeometry(QtCore.QRect(20, 110, 67, 17))
        self.name.setObjectName("name")
        self.Email = QtGui.QLabel(Dialog)
        self.Email.setGeometry(QtCore.QRect(20, 170, 67, 17))
        self.Email.setObjectName("Email")
        self.address = QtGui.QLabel(Dialog)
        self.address.setGeometry(QtCore.QRect(20, 290, 67, 17))
        self.address.setObjectName("address")
        self.phonenumber = QtGui.QLabel(Dialog)
        self.phonenumber.setGeometry(QtCore.QRect(10, 360, 101, 21))
        self.phonenumber.setObjectName("phonenumber")
        self.gender = QtGui.QLabel(Dialog)
        self.gender.setGeometry(QtCore.QRect(20, 230, 67, 17))
        self.gender.setObjectName("gender")
        self.lineEdit = QtGui.QLineEdit(Dialog)
        self.lineEdit.setEnabled(True)
        self.lineEdit.setGeometry(QtCore.QRect(170, 110, 151, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtGui.QLineEdit(Dialog)
        self.lineEdit_2.setEnabled(True)
        self.lineEdit_2.setGeometry(QtCore.QRect(170, 160, 151, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_4 = QtGui.QLineEdit(Dialog)
        self.lineEdit_4.setEnabled(True)
        self.lineEdit_4.setGeometry(QtCore.QRect(170, 280, 151, 31))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtGui.QLineEdit(Dialog)
        self.lineEdit_5.setEnabled(True)
        self.lineEdit_5.setGeometry(QtCore.QRect(170, 350, 161, 31))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(310, 460, 141, 31))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit_3 = QtGui.QLineEdit(Dialog)
        self.lineEdit_3.setEnabled(True)
        self.lineEdit_3.setGeometry(QtCore.QRect(170, 220, 151, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.textEdit = QtGui.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(470, 110, 191, 271))
        self.textEdit.setObjectName("textEdit")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "simple Example", None, QtGui.QApplication.UnicodeUTF8))
        self.name.setText(QtGui.QApplication.translate("Dialog", "Name", None, QtGui.QApplication.UnicodeUTF8))
        self.Email.setText(QtGui.QApplication.translate("Dialog", "E-Mail", None, QtGui.QApplication.UnicodeUTF8))
        self.address.setText(QtGui.QApplication.translate("Dialog", "Address", None, QtGui.QApplication.UnicodeUTF8))
        self.phonenumber.setText(QtGui.QApplication.translate("Dialog", "PhoneNumber", None, QtGui.QApplication.UnicodeUTF8))
        self.gender.setText(QtGui.QApplication.translate("Dialog", "Gender", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("Dialog", "click", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

