from __future__ import division
import sys
from PyQt4 import QtGui
import calculator
import math
import cmath
import numpy as np
import pyqtgraph as pg
from PyQt4.QtCore import *
from PyQt4.QtGui import *
prev= ""

class Graph(QtGui.QMainWindow): #Auxiliary class to display pop-up for inputting range
    def __init__(self,parent = None):
        super(Graph, self).__init__(parent)
	page = QWidget()
	page.setMinimumSize(QSize(350, 320))
	page.setWindowTitle("Enter range")
	page.start = QLabel(page)
        page.start.setText('Start:')
        page.end = QLabel(page)
        page.end.setText('End:')
        page.step = QLabel(page)
        page.step.setText('Step size:')
	self.button = QPushButton('Plot', page)
	self.edit1 = QLineEdit()
	self.edit2 = QLineEdit()
	self.edit3 = QLineEdit()
	self.edit1.move(80,20)
	page.start.move(20,15)
	self.edit1.move(80,80)
	page.end.move(20,85)
	self.edit1.move(80,140)
	page.step.move(20,145)
	vbox1 = QVBoxLayout()
	vbox1.addWidget(self.edit1)
	vbox1.addWidget(self.edit2)
	vbox1.addWidget(self.edit3)
	vbox1.addWidget(self.button)
	page.setLayout(vbox1)
	self.setCentralWidget(page)
	self.connect(self.button, SIGNAL("clicked()"), self.clicked)

    def clicked(self):
	l = float(self.edit1.text())
	r = float(self.edit2.text())
	s = float(self.edit3.text())
	x = np.arange(l,r,s)
	print(x)
	s = calculator_class.var
	print("In Second")
	print(s)
	y = eval(s)
	pg.setConfigOption('background', 'w')      # sets background white
    	pg.setConfigOption('foreground', 'k')      # sets axis color to black
	pw = pg.plot(x,y,pen = 'k')
	pw.setTitle('y = f(x)')
   	pw.setLabel('bottom', 'x -->')           	# x-label
    	pw.setLabel('left', 'y = f(x) -->')             # y-label

class calculator_class(calculator.Ui_Dialog,QtGui.QMainWindow):
	def btnstate(self,r1):
		if r1.isChecked() == True:
			self.bco.show()
			self.arg.show()
			self.sin.hide()
			self.cos.hide()
			self.tan.hide()
			self.log.hide()
			self.ln.hide()
			self.sq_root.hide()
		else:
			self.bco.hide()
			self.arg.hide()
			self.sin.show()
			self.cos.show()
			self.tan.show()
			self.log.show()
			self.ln.show()
			self.sq_root.show()

	def __init__(self):
		super(calculator_class, self).__init__()
		self.setupUi(self)
		self.r1.setChecked(False)
		self.bco.hide()
		self.arg.hide()
		self.r1.toggled.connect(lambda:self.btnstate(self.r1))
		self.b0.clicked.connect(lambda:self.display_screen('0'))
		self.b0.clicked.connect(lambda:self.storage('0',1))
		self.b1.clicked.connect(lambda:self.display_screen('1'))
		self.b1.clicked.connect(lambda:self.storage('1',1))
		self.b2.clicked.connect(lambda:self.display_screen('2'))
		self.b2.clicked.connect(lambda:self.storage('2',1))
		self.b3.clicked.connect(lambda:self.display_screen('3'))
		self.b3.clicked.connect(lambda:self.storage('3',1))
		self.b4.clicked.connect(lambda:self.display_screen('4'))
		self.b4.clicked.connect(lambda:self.storage('4',1))
		self.b5.clicked.connect(lambda:self.display_screen('5'))
		self.b5.clicked.connect(lambda:self.storage('5',1))
		self.b6.clicked.connect(lambda:self.display_screen('6'))
		self.b6.clicked.connect(lambda:self.storage('6',1))
		self.b7.clicked.connect(lambda:self.display_screen('7'))
		self.b7.clicked.connect(lambda:self.storage('7',1))
		self.b8.clicked.connect(lambda:self.display_screen('8'))
		self.b8.clicked.connect(lambda:self.storage('8',1))
		self.b9.clicked.connect(lambda:self.display_screen('9'))
		self.b9.clicked.connect(lambda:self.storage('9',1))
		self.bco.clicked.connect(lambda:self.display_screen('j'))
		self.bco.clicked.connect(lambda:self.storage('j',1))
		self.decimal.clicked.connect(lambda:self.display_screen('.'))
		self.decimal.clicked.connect(lambda:self.storage('.',1))
		self.add.clicked.connect(lambda:self.display_screen(' + '))
		self.add.clicked.connect(lambda:self.storage(' + ',1))
		self.substract.clicked.connect(lambda:self.display_screen(' - '))
		self.substract.clicked.connect(lambda:self.storage(' - ',1))
		self.plus_minus.clicked.connect(lambda:self.display_screen('-'))
		self.plus_minus.clicked.connect(lambda:self.storage('-',1))
		self.multiply.clicked.connect(lambda:self.display_screen(' X '))
		self.multiply.clicked.connect(lambda:self.storage(' * ',1))
		self.divide.clicked.connect(lambda:self.display_screen(' / '))
		self.divide.clicked.connect(lambda:self.storage(' / ',1))
		self.log.clicked.connect(lambda:self.display_screen(' log( '))
		self.log.clicked.connect(lambda:self.storage(' np.log10(',1))
		self.ln.clicked.connect(lambda:self.display_screen(' ln( '))
		self.ln.clicked.connect(lambda:self.storage(' (np.log10(math.e))**(-1) * np.log10( ',1))
		self.pi.clicked.connect(lambda:self.display_screen('pi'))
		self.pi.clicked.connect(lambda:self.storage('np.pi',1))
		self.e.clicked.connect(lambda:self.display_screen('e'))
		self.e.clicked.connect(lambda:self.storage('np.e',1))
		self.arg.clicked.connect(lambda:self.display_screen('Arg('))
		self.arg.clicked.connect(lambda:self.storage('(180/(np.pi))*cmath.phase(',1))
		self.b_open.clicked.connect(lambda:self.display_screen(' ( '))
		self.b_open.clicked.connect(lambda:self.storage(' ( ',1))
		self.sin.clicked.connect(lambda:self.display_screen(' sin( '))
		self.sin.clicked.connect(lambda:self.storage(' np.sin( ',1))
		self.cos.clicked.connect(lambda:self.display_screen(' cos( '))
		self.cos.clicked.connect(lambda:self.storage(' np.cos( ',1))
		self.tan.clicked.connect(lambda:self.display_screen(' tan( '))
		self.tan.clicked.connect(lambda:self.storage(' np.tan( ',1))
		self.sq_root.clicked.connect(lambda:self.display_screen(' sqrt( '))
		self.sq_root.clicked.connect(lambda:self.storage(' math.sqrt( ',1))
		self.sin1.clicked.connect(lambda:self.display_screen(' arcsin( '))
		self.sin1.clicked.connect(lambda:self.storage('math.asin( ',1))
		self.cos1.clicked.connect(lambda:self.display_screen(' arccos( '))
		self.cos1.clicked.connect(lambda:self.storage(' math.acos( ',1))
		self.tan1.clicked.connect(lambda:self.display_screen(' arctan( '))
		self.tan1.clicked.connect(lambda:self.storage(' math.atan( ',1))
		self.power.clicked.connect(lambda:self.display_screen(' ^ '))
		self.power.clicked.connect(lambda:self.storage(' ** ',1))
		self.b_close.clicked.connect(lambda:self.display_screen(' ) '))
		self.b_close.clicked.connect(lambda:self.storage(' ) ',1))
		self.clear.clicked.connect(self.display.clear)
		self.clear.clicked.connect(lambda:self.storage("",3))
		self.back.clicked.connect(self.display.clear)
		self.back.clicked.connect(lambda:self.display_screen2(self.prev_disp))
		self.back.clicked.connect(lambda:self.storage1(self.store))
		self.equal.clicked.connect(self.calculation)
		self.graph.clicked.connect(self.graphing)
		self.x.clicked.connect(lambda:self.display_screen(' x '))
		self.x.clicked.connect(lambda:self.storage(' x ',1))
		self.plot.clicked.connect(self.plott)
		self.display.setReadOnly(True)
	var = ""
	store= ""
	prev_disp = ""
	stack = []
	stack_disp = []
	temp = []
	def graphing(self):
		self.flag = 1
		print("Welcome to graphs")
		print("Enter the equation f(x) : ")
		self.display.setText("Enter the equation f(x) : ")
		self.store = ""
    	def plott(self):
    		print(self.store)
    		x = np.arange(1,2,0.1) #Just to check if equation enter for plotting is syntactically correct or not
    		try:
    			y = eval(self.store)
    		except SyntaxError:
    			print("Improper Equation entered")
    			self.display.setText("Improper Equation entered")
    		else:
    			calculator_class.var = self.store
			self.dialog = Graph(self)	#Calling the Graph class to display a Range requesting pop-up
			self.dialog.setWindowTitle('Please Enter Range of y = f(x)')
			self.dialog.show()

	def storage1(self,value):
		try:
			self.stack.pop()
		except IndexError:
			self.store = ""
		else:
			self.temp = self.stack
			self.store = ''.join(self.temp)

	def storage(self,value,k):
		if k is 1 :
			self.store=self.store + value
		elif k is 3:
			self.stack=[]
			self.stack_disp=[]
			self.store=""
		print (self.store)
		self.stack.append(value)

	def display_screen(self,value):
		self.display.insert(value)
		self.stack_disp.append(value)

	def display_screen1(self,value):
		self.display.setText(value)
		self.stack_disp.append(value)

	def display_screen2(self,value):
		try:
			self.stack_disp.pop()
		except IndexError:
			self.display_screen1("")
		else:
			if(self.flag == 1):
				self.display.setText("Enter the equation f(x) : ")
				self.temp = self.stack_disp
				value = ''.join(self.temp)
				self.display.insert(value)
			else:
				self.temp = self.stack_disp
				value = ''.join(self.temp)
				self.display.setText(value)

	def display_error(self,value):
		self.display.setText(value)
		self.stack_disp.append(value)

	def disp_res(self,value):
		self.display.setText(value)
		self.stack_disp.append(value)

	def calculation(self):
		screen_value=self.store
		screen_value=str(screen_value)
		print(''.join(self.stack))
		try:
			final_value=eval(screen_value)
		except ZeroDivisionError:
			print("Math Error : Division by Zero")
			self.stack.append('#') #Done so as to pop once in order to remove the error message from disp and secondly to pop the wrong input
			self.display_error("Math Error : Division by Zero")
		except ValueError:
			print("Math Error :No negatives in sqrt/log ,cos-1 & sin-1 b/w -1 & 1")
			self.stack.append('#')
			self.display_error("Math Error :No negatives in sqrt/log ,cos-1 & sin-1 b/w -1 & 1 ")
		except SyntaxError:
			print("Improper equation entered")
			self.stack.append('#')
			self.display_error("Improper equation entered")
		except AttributeError:
			print("Input Error : Please enter proper input")
			self.stack.append('#')
			self.display_error("Input Error : Please enter proper input")
		else:
			final_value=str(final_value)
			self.store=final_value
			self.stack.append(final_value)
			print(self.store)
			self.disp_res(" = " + final_value)




if __name__== '__main__':
	qapp=QtGui.QApplication(sys.argv)
	calc=calculator_class()
	calc.show()
	qapp.exec_()
