import matrix
import sys
from PyQt4 import QtGui
import numpy as np
import math
class matrix_class(matrix.Ui_Matwin,QtGui.QMainWindow):
	st=""
	ar1=[]#for name
	arr2=[]# for matrix valve

	def __init__(self):
		super(matrix_class, self).__init__()
		self.setupUi(self)
		self.solve.clicked.connect(lambda:self.solver())
		self.clear.clicked.connect(lambda:self.clear_scrn())
		self.op.setReadOnly(True)
		self.clr.clicked.connect(self.ds2.clear)
		self.new_mat.clicked.connect(lambda:self.addmat())

	def addmat(self):
		a=[]
		a2=[]

		v = str(self.ds2.text())
		v=v.replace(" ","")
		ar1=v.split("=")
		nm=ar1[0]
		dat1=ar1[1]
		dat=dat1.split(';')
		for i in dat:
			arr=i.split(',')
			for j in arr:
				a.append(int(j))
			a2.append(a)
			a=[]

		try:
			if nm!= 'st' and nm!='d':
				#self.d[nm]=np.array(a2)
				self.ar1.append(nm)
				self.arr2.append(np.array(a2))
			else:
				self.st = self.st + 'st and d are keywords and cannot be set as a name of matrix' + '\n'
				self.op.setText(self.st)




		except:
			self.st=self.st+"\n"+"Error Please Try Again!!!"+"\n\n"
			self.op.setText(self.st)
	def solver(self):
		v = self.ds2.text()
		c=0
		for i in self.ar1:
			v=v.replace(i,'self.arr2['+str(c)+']')
			c=c+1
		p=eval(v)
		self.st = self.st + str(p) + '\n'
		self.op.setText(self.st)





	def clear_scrn(self):
		self.st=""
		self.op.setText(self.st)

if __name__ == '__main__':
	qapp=QtGui.QApplication(sys.argv)
	calc=matrix_class()
	calc.show()
	qapp.exec_()

