from __future__ import division
import sys
from PyQt4 import QtGui
import calculator
import math

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
		self.log.clicked.connect(lambda:self.storage(' math.log10(',1))
		self.ln.clicked.connect(lambda:self.display_screen(' ln( '))
		self.ln.clicked.connect(lambda:self.storage(' (math.log10(math.e))**(-1) * math.log10( ',1))
		self.pi.clicked.connect(lambda:self.display_screen('pi'))
		self.pi.clicked.connect(lambda:self.storage('math.pi',1))
		self.e.clicked.connect(lambda:self.display_screen('e'))
		self.e.clicked.connect(lambda:self.storage('math.e',1))
		self.arg.clicked.connect(lambda:self.display_screen('Arg'))
		self.arg.clicked.connect(lambda:self.storage('cmath.phase',1))
		self.b_open.clicked.connect(lambda:self.display_screen(' ( '))
		self.b_open.clicked.connect(lambda:self.storage(' ( ',1))
		self.sin.clicked.connect(lambda:self.display_screen(' sin( '))
		self.sin.clicked.connect(lambda:self.storage('math.sin( ',1))
		self.cos.clicked.connect(lambda:self.display_screen(' cos( '))
		self.cos.clicked.connect(lambda:self.storage(' math.cos( ',1))
		self.tan.clicked.connect(lambda:self.display_screen(' tan( '))
		self.tan.clicked.connect(lambda:self.storage(' math.tan( ',1))
		self.sq_root.clicked.connect(lambda:self.display_screen(' sqrt( '))
		self.sq_root.clicked.connect(lambda:self.storage(' math.sqrt( ',1))
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
		self.display.setReadOnly(True)

	store= ""

	def storage(self,value,k):
		if k is 1 :
			self.store=self.store + value
		elif k is 3:
			self.store=""
		print (self.store)

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

	def display_error(self,value):
		self.display.setText(value)
		self.stack_disp.append(value)

	def disp_res(self,value):
		self.display.setText(value)
		self.stack_disp.append(value)

	def calculation(self):
		screen_value=self.store
		screen_value=str(screen_value)

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


if __name__== '__main__':
	qapp=QtGui.QApplication(sys.argv)
	calc=calculator_class()
	calc.show()
	qapp.exec_()
