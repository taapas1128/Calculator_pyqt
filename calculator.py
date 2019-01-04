# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calculator.ui'
#
# Created by: PyQt4 UI code generator 4.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from equation import Ui_Form
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

class Ui_Dialog(object):
    def openWindow(self):
        self.window = QtGui.QMainWindow()
        self.ui = Ui_Form()
        self.ui.setupUi(self.window)
        self.window.show()
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(440, 539)
        Dialog.setMinimumSize(QtCore.QSize(440, 539))
        Dialog.setMaximumSize(QtCore.QSize(440, 539))
        Dialog.setStyleSheet(_fromUtf8("\n"
"QToolTip\n"
"{\n"
"     border: 1px solid black;\n"
"     background-color: #D1DBCB;\n"
"     padding: 1px;\n"
"     border-radius: 3px;\n"
"     opacity: 100;\n"
"}\n"
"\n"
"QWidget\n"
"{\n"
"    color: #b1b1b1;\n"
"    background-color: #323232;\n"
"    selection-background-color:#323232;\n"
"    selection-color: black;\n"
"    background-clip: border;\n"
"    border-image: none;\n"
"    border: 0px transparent black;\n"
"    outline: 0;\n"
"}\n"
"\n"
"QWidget:item:hover\n"
"{\n"
"    background-color: #D1DBCB;\n"
"    color: black;\n"
"}\n"
"\n"
"QWidget:item:selected\n"
"{\n"
"    background-color: #D1DBCB;\n"
"    border: 0px\n"
"}\n"
"\n"
"QLineEdit\n"
"{\n"
"    background-color: #1e1e1e;\n"
"    selection-background-color: #D1DBCB;\n"
"    selection-color: black;\n"
"    padding: 5px;\n"
"    border-style: solid;\n"
"    border: 1px solid #76797C;\n"
"    border-radius: 2px;\n"
"    color: #eff0f1;\n"
"}\n"
"QPushButton::menu-indicator  {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: bottom right;\n"
"    left: 8px;\n"
"}\n"
"QPushButton\n"
"{\n"
"    color: #eff0f1;\n"
"    background-color: #323232;\n"
"    border-width: 1px;\n"
"    border-color: #76797C;\n"
"    border-style: solid;\n"
"    padding: 5px;\n"
"    border-radius: 0px;\n"
"    outline: none;\n"
"}\n"
"\n"
"QPushButton:disabled\n"
"{\n"
"    background-color: #323232;\n"
"    border-width: 1px;\n"
"    border-color: #454545;\n"
"    border-style: solid;\n"
"    padding-top: 5px;\n"
"    padding-bottom: 5px;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"    border-radius: 2px;\n"
"    color: #454545;\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    background-color: #D1DBCB;\n"
"    color: black;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    color: black;\n"
"    background-color: #D1DBCB;\n"
"    padding-top: -15px;\n"
"    padding-bottom: -17px;\n"
"}\n"
"\n"
"QComboBox\n"
"{\n"
"    selection-background-color: #D1DBCB;\n"
"    background-color: #31363B;\n"
"    border-style: solid;\n"
"    border: 1px solid #76797C;\n"
"    border-radius: 2px;\n"
"    padding: 5px;\n"
"    min-width: 75px;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"    background-color: #76797C;\n"
"    border-color: #6A6969;\n"
"}\n"
"\n"
"QComboBox:hover,QPushButton:hover,QAbstractSpinBox:hover,QLineEdit:hover,QTextEdit:hover,QPlainTextEdit:hover,QAbstractView:hover,QTreeView:hover\n"
"{\n"
"    border: 1px solid #D1DBCB;\n"
"}\n"
"QTabWidget:focus, QCheckBox:focus, QRadioButton:focus, QSlider:focus\n"
"{\n"
"    border: none;\n"
"}\n"
"\n"
"QHeaderView::section\n"
"{\n"
"    background-color: #76797C;\n"
"    color: #eff0f1;\n"
"    padding: 5px;\n"
"    border: 1px solid #76797C;\n"
"}\n"
"\n"
"QSizeGrip {\n"
"    image: url(:/qss_icons/rc/sizegrip.png);\n"
"    width: 12px;\n"
"    height: 12px;\n"
"}\n"
"\n"
"\n"
"QMainWindow::separator\n"
"{\n"
"    background-color: #323232;\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    spacing: 2px;\n"
"    border: 1px dashed #76797C;\n"
"}\n"
"\n"
"QMainWindow::separator:hover\n"
"{\n"
"\n"
"    background-color: #787876;\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #76797C;\n"
"    spacing: 2px;\n"
"}\n"
"\n"
"\n"
"QMenu::separator\n"
"{\n"
"    height: 1px;\n"
"    background-color: #76797C;\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    margin-left: 10px;\n"
"    margin-right: 5px;\n"
"}\n"
"\n"
"QFrame\n"
"{\n"
"    border-radius: 0px;\n"
"    /*border: 1px solid #76797C;*/\n"
"}\n"
"\n"
"\n"
"QFrame[frameShape=\"0\"]\n"
"{\n"
"    border-radius: 0px;\n"
"    border: 0px transparent #76797C;\n"
"}\n"
"\n"
"QStackedWidget\n"
"{\n"
"    border: 1px transparent black;\n"
"}"))
        self.b1 = QtGui.QPushButton(Dialog)
        self.b1.setGeometry(QtCore.QRect(10, 230, 61, 51))
        self.b1.setObjectName(_fromUtf8("b1"))
        self.b3 = QtGui.QPushButton(Dialog)
        self.b3.setGeometry(QtCore.QRect(150, 230, 61, 51))
        self.b3.setObjectName(_fromUtf8("b3"))
        self.b2 = QtGui.QPushButton(Dialog)
        self.b2.setGeometry(QtCore.QRect(80, 230, 61, 51))
        self.b2.setObjectName(_fromUtf8("b2"))
        self.b6 = QtGui.QPushButton(Dialog)
        self.b6.setGeometry(QtCore.QRect(150, 170, 61, 51))
        self.b6.setObjectName(_fromUtf8("b6"))
        self.b5 = QtGui.QPushButton(Dialog)
        self.b5.setGeometry(QtCore.QRect(80, 170, 61, 51))
        self.b5.setObjectName(_fromUtf8("b5"))
        self.b4 = QtGui.QPushButton(Dialog)
        self.b4.setGeometry(QtCore.QRect(10, 170, 61, 51))
        self.b4.setObjectName(_fromUtf8("b4"))
        self.b9 = QtGui.QPushButton(Dialog)
        self.b9.setGeometry(QtCore.QRect(150, 110, 61, 51))
        self.b9.setObjectName(_fromUtf8("b9"))
        self.b8 = QtGui.QPushButton(Dialog)
        self.b8.setGeometry(QtCore.QRect(80, 110, 61, 51))
        self.b8.setObjectName(_fromUtf8("b8"))
        self.b7 = QtGui.QPushButton(Dialog)
        self.b7.setGeometry(QtCore.QRect(10, 110, 61, 51))
        self.b7.setObjectName(_fromUtf8("b7"))
        self.plus_minus = QtGui.QPushButton(Dialog)
        self.plus_minus.setGeometry(QtCore.QRect(80, 290, 61, 51))
        self.plus_minus.setObjectName(_fromUtf8("plus_minus"))
        self.b0 = QtGui.QPushButton(Dialog)
        self.b0.setGeometry(QtCore.QRect(10, 290, 61, 51))
        self.b0.setObjectName(_fromUtf8("b0"))
        self.decimal = QtGui.QPushButton(Dialog)
        self.decimal.setGeometry(QtCore.QRect(150, 290, 61, 51))
        self.decimal.setObjectName(_fromUtf8("decimal"))
        self.display = QtGui.QLineEdit(Dialog)
        self.display.setGeometry(QtCore.QRect(10, 20, 421, 71))
        self.display.setObjectName(_fromUtf8("display"))
        self.equal = QtGui.QPushButton(Dialog)
        self.equal.setGeometry(QtCore.QRect(220, 290, 61, 51))
        self.equal.setObjectName(_fromUtf8("equal"))
        self.clear = QtGui.QPushButton(Dialog)
        self.clear.setGeometry(QtCore.QRect(290, 230, 81, 51))
        self.clear.setObjectName(_fromUtf8("clear"))
        self.back = QtGui.QPushButton(Dialog)
        self.back.setGeometry(QtCore.QRect(290, 170, 81, 51))
        self.back.setObjectName(_fromUtf8("back"))
        self.add = QtGui.QPushButton(Dialog)
        self.add.setGeometry(QtCore.QRect(220, 170, 61, 51))
        self.add.setObjectName(_fromUtf8("add"))
        self.substract = QtGui.QPushButton(Dialog)
        self.substract.setGeometry(QtCore.QRect(220, 230, 61, 51))
        self.substract.setObjectName(_fromUtf8("substract"))
        self.divide = QtGui.QPushButton(Dialog)
        self.divide.setGeometry(QtCore.QRect(290, 290, 81, 51))
        self.divide.setObjectName(_fromUtf8("divide"))
        self.multiply = QtGui.QPushButton(Dialog)
        self.multiply.setGeometry(QtCore.QRect(220, 110, 61, 51))
        self.multiply.setObjectName(_fromUtf8("multiply"))
        self.sq_root = QtGui.QPushButton(Dialog)
        self.sq_root.setGeometry(QtCore.QRect(320, 350, 51, 51))
        self.sq_root.setObjectName(_fromUtf8("sq_root"))
        self.sin = QtGui.QPushButton(Dialog)
        self.sin.setGeometry(QtCore.QRect(10, 350, 51, 51))
        self.sin.setObjectName(_fromUtf8("sin"))
        self.cos = QtGui.QPushButton(Dialog)
        self.cos.setGeometry(QtCore.QRect(70, 350, 51, 51))
        self.cos.setObjectName(_fromUtf8("cos"))
        self.tan = QtGui.QPushButton(Dialog)
        self.tan.setGeometry(QtCore.QRect(130, 350, 51, 51))
        self.tan.setObjectName(_fromUtf8("tan"))
        self.power = QtGui.QPushButton(Dialog)
        self.power.setGeometry(QtCore.QRect(150, 410, 71, 51))
        self.power.setObjectName(_fromUtf8("power"))
        self.log = QtGui.QPushButton(Dialog)
        self.log.setGeometry(QtCore.QRect(250, 350, 61, 51))
        self.log.setObjectName(_fromUtf8("log"))
        self.b_open = QtGui.QPushButton(Dialog)
        self.b_open.setGeometry(QtCore.QRect(10, 410, 61, 51))
        self.b_open.setObjectName(_fromUtf8("b_open"))
        self.b_close = QtGui.QPushButton(Dialog)
        self.b_close.setGeometry(QtCore.QRect(80, 410, 61, 51))
        self.b_close.setObjectName(_fromUtf8("b_close"))
        self.ln = QtGui.QPushButton(Dialog)
        self.ln.setGeometry(QtCore.QRect(190, 350, 51, 51))
        self.ln.setObjectName(_fromUtf8("ln"))
        self.e = QtGui.QPushButton(Dialog)
        self.e.setGeometry(QtCore.QRect(230, 410, 71, 51))
        self.e.setObjectName(_fromUtf8("e"))
        self.pi = QtGui.QPushButton(Dialog)
        self.pi.setGeometry(QtCore.QRect(310, 410, 61, 51))
        self.pi.setObjectName(_fromUtf8("pi"))
        self.bco = QtGui.QPushButton(Dialog)
        self.bco.setGeometry(QtCore.QRect(190, 350, 181, 51))
        self.bco.setObjectName(_fromUtf8("bco"))
        self.arg = QtGui.QPushButton(Dialog)
        self.arg.setGeometry(QtCore.QRect(10, 350, 171, 51))
        self.arg.setObjectName(_fromUtf8("arg"))
        self.r1 = QtGui.QRadioButton(Dialog)
        self.r1.setGeometry(QtCore.QRect(290, 110, 91, 51))
        self.r1.setObjectName(_fromUtf8("r1"))
        self.graph = QtGui.QPushButton(Dialog)
        self.graph.setGeometry(QtCore.QRect(10, 470, 61, 51))
        self.graph.setObjectName(_fromUtf8("graph"))
        self.plot = QtGui.QPushButton(Dialog)
        self.plot.setGeometry(QtCore.QRect(80, 470, 81, 51))
        self.plot.setObjectName(_fromUtf8("plot"))
        self.x = QtGui.QPushButton(Dialog)
        self.x.setGeometry(QtCore.QRect(170, 470, 61, 51))
        self.x.setObjectName(_fromUtf8("x"))
        self.cos1 = QtGui.QPushButton(Dialog)
        self.cos1.setGeometry(QtCore.QRect(380, 170, 51, 51))
        self.cos1.setObjectName(_fromUtf8("cos1"))
        self.sin1 = QtGui.QPushButton(Dialog)
        self.sin1.setGeometry(QtCore.QRect(380, 110, 51, 51))
        self.sin1.setObjectName(_fromUtf8("sin1"))
        self.tan1 = QtGui.QPushButton(Dialog)
        self.tan1.setGeometry(QtCore.QRect(380, 230, 51, 51))
        self.tan1.setObjectName(_fromUtf8("tan1"))
        self.fact = QtGui.QPushButton(Dialog)
        self.fact.setGeometry(QtCore.QRect(380, 290, 51, 51))
        self.fact.setObjectName(_fromUtf8("fact"))
        self.comb = QtGui.QPushButton(Dialog)
        self.comb.setGeometry(QtCore.QRect(380, 350, 51, 51))
        self.comb.setObjectName(_fromUtf8("comb"))
        self.perm = QtGui.QPushButton(Dialog)
        self.perm.setGeometry(QtCore.QRect(380, 410, 51, 51))
        self.perm.setObjectName(_fromUtf8("perm"))
        self.com = QtGui.QPushButton(Dialog)
        self.com.setGeometry(QtCore.QRect(380, 470, 51, 51))
        self.com.setObjectName(_fromUtf8("com"))
        self.equ = QtGui.QPushButton(Dialog)
        self.equ.setGeometry(QtCore.QRect(240, 470, 131, 51))
        self.equ.setObjectName(_fromUtf8("equ"))
        self.equ.clicked.connect(self.openWindow)
        self.graph.raise_()
        self.plot.raise_()
        self.x.raise_()
        self.arg.raise_()
        self.b1.raise_()
        self.b3.raise_()
        self.b2.raise_()
        self.b6.raise_()
        self.b5.raise_()
        self.b4.raise_()
        self.b9.raise_()
        self.b8.raise_()
        self.b7.raise_()
        self.plus_minus.raise_()
        self.b0.raise_()
        self.decimal.raise_()
        self.display.raise_()
        self.equal.raise_()
        self.clear.raise_()
        self.back.raise_()
        self.add.raise_()
        self.substract.raise_()
        self.divide.raise_()
        self.multiply.raise_()
        self.sq_root.raise_()
        self.sin.raise_()
        self.cos.raise_()
        self.tan.raise_()
        self.power.raise_()
        self.log.raise_()
        self.b_open.raise_()
        self.b_close.raise_()
        self.ln.raise_()
        self.e.raise_()
        self.pi.raise_()
        self.r1.raise_()
        self.bco.raise_()
        self.cos1.raise_()
        self.sin1.raise_()
        self.tan1.raise_()
        self.fact.raise_()
        self.comb.raise_()
        self.perm.raise_()
        self.com.raise_()
        self.equ.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Calculator", None))
        self.b1.setText(_translate("Dialog", "1", None))
        self.b3.setText(_translate("Dialog", "3", None))
        self.b2.setText(_translate("Dialog", "2", None))
        self.b6.setText(_translate("Dialog", "6", None))
        self.b5.setText(_translate("Dialog", "5", None))
        self.b4.setText(_translate("Dialog", "4", None))
        self.b9.setText(_translate("Dialog", "9", None))
        self.b8.setText(_translate("Dialog", "8", None))
        self.b7.setText(_translate("Dialog", "7", None))
        self.plus_minus.setText(_translate("Dialog", "+/-", None))
        self.b0.setText(_translate("Dialog", "0", None))
        self.decimal.setText(_translate("Dialog", ".", None))
        self.equal.setText(_translate("Dialog", "=", None))
        self.clear.setText(_translate("Dialog", "AC", None))
        self.back.setText(_translate("Dialog", "Back", None))
        self.add.setText(_translate("Dialog", "+", None))
        self.substract.setText(_translate("Dialog", "-", None))
        self.divide.setText(_translate("Dialog", "/", None))
        self.multiply.setText(_translate("Dialog", "X", None))
        self.sq_root.setText(_translate("Dialog", "Sqrt", None))
        self.sin.setText(_translate("Dialog", "sin", None))
        self.cos.setText(_translate("Dialog", "cos", None))
        self.tan.setText(_translate("Dialog", "tan", None))
        self.power.setText(_translate("Dialog", "^", None))
        self.log.setText(_translate("Dialog", "log", None))
        self.b_open.setText(_translate("Dialog", "(", None))
        self.b_close.setText(_translate("Dialog", ")", None))
        self.ln.setText(_translate("Dialog", "ln", None))
        self.e.setText(_translate("Dialog", "e", None))
        self.pi.setText(_translate("Dialog", "π", None))
        self.bco.setText(_translate("Dialog", "j", None))
        self.arg.setText(_translate("Dialog", "Arg", None))
        self.r1.setText(_translate("Dialog", "Complex", None))
        self.graph.setText(_translate("Dialog", "graph", None))
        self.plot.setText(_translate("Dialog", "plot", None))
        self.x.setText(_translate("Dialog", "x", None))
        self.cos1.setText(_translate("Dialog", "cos-1", None))
        self.sin1.setText(_translate("Dialog", "sin-1", None))
        self.tan1.setText(_translate("Dialog", "tan-1", None))
        self.fact.setText(_translate("Dialog", "x!", None))
        self.comb.setText(_translate("Dialog", "nCr", None))
        self.perm.setText(_translate("Dialog", "nPr", None))
        self.com.setText(_translate("Dialog", ",", None))
        self.equ.setText(_translate("Dialog", "Equation", None))
