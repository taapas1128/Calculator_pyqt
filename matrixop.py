import matrix
import sys
from PyQt4 import QtGui
import numpy as np
import math


class matrix_class(matrix.Ui_Matwin,QtGui.QMainWindow):
	st=""
	def __init__(self):
		super(matrix_class, self).__init__()
		self.setupUi(self)
		self.solve.clicked.connect(lambda:self.solver())
		self.clear.clicked.connect(lambda:self.clear_scrn())
		self.op.setReadOnly(True)
		self.clr.clicked.connect(self.ds2.clear)



	def solver(self):
		v=str(self.ds2.text())
		n=eval(v)
		self.st=self.st+str(n)+'\n'
		self.op.setText(self.st)
	def clear_scrn(self):
		self.st=""
		self.op.setText(self.st)

if __name__ == '__main__':
	qapp=QtGui.QApplication(sys.argv)
	calc=matrix_class()
	calc.show()
	qapp.exec_()

