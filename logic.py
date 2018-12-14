#Credits and sources :
#https://stackoverflow.com/questions/3972158/how-to-plot-on-my-gui
from __future__ import division
import sys
from PyQt4 import QtGui
import calculator
import math

import numpy as np
import pyqtgraph as pg


class calculator_class(calculator.Ui_Dialog,QtGui.QMainWindow):

	def __init__(self):
		super(calculator_class, self).__init__()
		self.setupUi(self)
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
		self.decimal.clicked.connect(lambda:self.display_screen('.'))
		self.decimal.clicked.connect(lambda:self.storage('.',1))		
		self.add.clicked.connect(lambda:self.display_screen(' + '))
		self.add.clicked.connect(lambda:self.storage(' + ',1))
		self.substract.clicked.connect(lambda:self.display_screen(' - '))
		self.substract.clicked.connect(lambda:self.storage(' - ',1))
		self.plus_minus.clicked.connect(lambda:self.display_screen('-'))
		self.plus_minus.clicked.connect(lambda:self.storage('-',1))
		self.multiply.clicked.connect(lambda:self.display_screen(' * '))
		self.multiply.clicked.connect(lambda:self.storage(' * ',1))
		self.divide.clicked.connect(lambda:self.display_screen(' / '))
		self.divide.clicked.connect(lambda:self.storage(' / ',1))
		self.log.clicked.connect(lambda:self.display_screen(' log( '))
		self.log.clicked.connect(lambda:self.storage(' np.log10(',1))
		self.ln.clicked.connect(lambda:self.display_screen(' ln( '))
		self.ln.clicked.connect(lambda:self.storage(' (np.log10(np.e))**(-1) * np.log10( ',1))
		self.pi.clicked.connect(lambda:self.display_screen('pi'))
		self.pi.clicked.connect(lambda:self.storage('np.pi',1))
		self.e.clicked.connect(lambda:self.display_screen('e'))
		self.e.clicked.connect(lambda:self.storage('np.e',1))
		self.b_open.clicked.connect(lambda:self.display_screen(' ( '))
		self.b_open.clicked.connect(lambda:self.storage(' ( ',1))
		self.sin.clicked.connect(lambda:self.display_screen(' sin( '))
		self.sin.clicked.connect(lambda:self.storage('np.sin( ',1))
		self.cos.clicked.connect(lambda:self.display_screen(' cos( '))
		self.cos.clicked.connect(lambda:self.storage(' np.cos( ',1))
		self.tan.clicked.connect(lambda:self.display_screen(' tan( '))
		self.tan.clicked.connect(lambda:self.storage(' np.tan( ',1))
		self.sq_root.clicked.connect(lambda:self.display_screen(' sqrt( '))
		self.sq_root.clicked.connect(lambda:self.storage(' np.sqrt( ',1))
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
		self.x.clicked.connect(lambda:self.disp_eqn(' x '))
		self.x.clicked.connect(lambda:self.storage(' x ',1))		
		self.comma.clicked.connect(lambda:self.disp_eqn(' , '))
		self.comma.clicked.connect(lambda:self.storage(' , ',1))
		self.range.clicked.connect(lambda:self.disp_eqn(' range( '))
		self.range.clicked.connect(lambda:self.store_range(' np.arange( '))
		self.plot.clicked.connect(self.print_graph)	
		self.display.setReadOnly(True)	

	equation = ""
	store= ""
	prev_disp = ""
	stack = []
	stack_disp = []	

	temp = []	
	res = ""
	#Displays the equation on the console
	def disp_eqn(self,value):
		self.display.insert(value)
	#Receives the range of input and plots y = f(x)
	def print_graph(self):
		
		try:
			x_range = eval(self.store)
			print(x_range)
			x = x_range
			y = eval(self.res)
		except TypeError:
			self.display.setText("Please enter proper input")
		else:
			print(x)
			print("The equation is ----")
			print(self.res)
			print(y)
			pg.setConfigOption('background', 'w')      # sets background white                                                 
    			pg.setConfigOption('foreground', 'k')      # sets axis color to black
			pw = pg.plot(x,y,pen = 'k')
   			pw.setLabel('bottom', 'x -->')           # x-label
    			pw.setLabel('left', 'y = f(x) -->')             # y-label
    	#An aux. function to store the range and later convert it into proper function
	def store_range(self,value):
		self.store = ""
		self.store = self.store + value
		print("The equation is ----")
		print(self.equation)
		self.display.setText("Range format : (start,end,step size) : (")
		self.res = self.equation
		
    	#Intitiates the graphing console
	def graphing(self):
		print("Welcome to graphs")
		print("Enter the equation f(x) : ")
		self.display.setText("Enter the equation f(x) : ")
		self.store = ""
	
	#Aux. storage for implementing 'back'		

	temp = []

	def storage1(self,value):
		try:
			self.stack.pop()
		except IndexError:
			self.store = ""
		else:
			self.temp = self.stack
			self.store = ''.join(self.temp)

			self.equation = self.store
	
	#Primary storage of input fed


	def storage(self,value,k):
		if k is 1 :
			self.store=self.store + value
		elif k is 3:
			self.store=""
		print (self.store)

		self.equation = self.store
		self.stack.append(value)
	
	#Displays running text on screen
	def display_screen(self,value):
		self.display.insert(value)
		self.stack_disp.append(value)

	#Displays result of final computation	
	def display_screen1(self,value):
		self.display.setText(value)
		self.stack_disp.append(value)
	
	#Aux display after pressing back

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
			self.temp = self.stack_disp
			value = ''.join(self.temp)		
			self.display.setText(value)

			
	#Disp' fun' for error messages
	def display_error(self,value):
		self.display.setText(value)
		self.stack_disp.append(value)
	
	#Yet another display function
	def disp_res(self,value):
		self.display.setText(value)
		self.stack_disp.append(value)
	
	#Heart of the basic calculator


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
			print("Math Error : No negatives in sqrt/log")
			self.stack.append('#')
			self.display_error("Math Error : No negatives in sqrt/log")
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
