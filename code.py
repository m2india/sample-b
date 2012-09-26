#! /usr/bin/env python

import sys
from PyQt4 import QtCore, QtGui
from identicard import Ui_Dialog

class NaMe(QtGui.QDialog):
  def __init__(self, parent=None):
    QtGui.QWidget.__init__(self, parent)
    self.ui = Ui_Dialog()
    self.ui.setupUi(self)
    
    self.ui.pushButton.clicked.connect(self.poc)
    
  def poc(self):
		
	lineEdit = ''
	lineEdit_2 = ''
	lineEdit_3 = ''
	lineEdit_4 = ''
	lineEdit_5 = ''
	lineEdit  = self.ui.lineEdit.text()
	lineEdit_2 = self.ui.lineEdit_2.text()
	lineEdit_3 = self.ui.lineEdit_3.text()
	lineEdit_4 = self.ui.lineEdit_4.text()
	lineEdit_5 = self.ui.lineEdit_5.text()
	
	self.ui.textEdit.setText('Name :' +lineEdit+ '\n\nE-Mail: ' +lineEdit_2+ '\n\nAddress : ' +lineEdit_3 + '\n\n Gender :' +lineEdit_4+ '\n\nPhonenumber :' +lineEdit_5)
	
		
		
    
    
if __name__ == '__main__':
  app = QtGui.QApplication(sys.argv)
  main = NaMe()
  main.show()
  sys.exit(app.exec_())   
    
