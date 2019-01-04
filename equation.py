# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'equation.ui'
#
# Created by: PyQt4 UI code generator 4.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import cmath

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

class Ui_Form(object):
    def solve(self):
    	a = float(self.edit1.text())
    	b = float(self.edit2.text())
    	c = float(self.edit3.text())
        d = (b**2) - (4*a*c)
        root1 = (-b - cmath.sqrt(d)) / (2 * a)
        root2 = (-b + cmath.sqrt(d)) / (2 * a)
        print(root1)
        print(root2)
        root1=str(root1)
        root2=str(root2)
        self.ansx.setText(root1)
        self.ansy.setText(root2)
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(374, 270)
        Form.setStyleSheet(_fromUtf8("\n"
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
        self.edit1 = QtGui.QLineEdit(Form)
        self.edit1.setGeometry(QtCore.QRect(180, 80, 51, 41))
        self.edit1.setObjectName(_fromUtf8("edit1"))
        self.edit2 = QtGui.QLineEdit(Form)
        self.edit2.setGeometry(QtCore.QRect(240, 80, 61, 41))
        self.edit2.setObjectName(_fromUtf8("edit2"))
        self.edit3 = QtGui.QLineEdit(Form)
        self.edit3.setGeometry(QtCore.QRect(310, 80, 51, 41))
        self.edit3.setObjectName(_fromUtf8("edit3"))
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(80, 10, 241, 31))
        self.label.setObjectName(_fromUtf8("label"))
        self.label1 = QtGui.QLabel(Form)
        self.label1.setGeometry(QtCore.QRect(10, 80, 161, 31))
        self.label1.setObjectName(_fromUtf8("label1"))
        self.label3 = QtGui.QLabel(Form)
        self.label3.setGeometry(QtCore.QRect(30, 170, 51, 31))
        self.label3.setObjectName(_fromUtf8("label3"))
        self.label4 = QtGui.QLabel(Form)
        self.label4.setGeometry(QtCore.QRect(30, 220, 61, 31))
        self.label4.setObjectName(_fromUtf8("label4"))
        self.ansy = QtGui.QLineEdit(Form)
        self.ansy.setGeometry(QtCore.QRect(90, 220, 271, 41))
        self.ansy.setObjectName(_fromUtf8("ansy"))
        self.ansx = QtGui.QLineEdit(Form)
        self.ansx.setGeometry(QtCore.QRect(90, 170, 271, 41))
        self.ansx.setObjectName(_fromUtf8("ansx"))
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(150, 130, 97, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton.clicked.connect(self.solve)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label.setText(_translate("Form", "Equation is of the form ax^2+bx+c", None))
        self.label1.setText(_translate("Form", "Enter a , b and c \n"
" respectively", None))
        self.label3.setText(_translate("Form", "Root1=", None))
        self.label4.setText(_translate("Form", "Root2=", None))
        self.pushButton.setText(_translate("Form", "Calculate", None))
