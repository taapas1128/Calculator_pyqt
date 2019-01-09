# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'linequ.ui'
#
# Created by: PyQt4 UI code generator 4.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import numpy as np

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

class Ui_LinEquation(object):
    def solve(self):
    	a11 = float(self.a1.text())
    	b11 = float(self.b1.text())
    	c11 = float(self.c1.text())
    	a22 = float(self.a2.text())
    	b22 = float(self.b2.text())
    	c22 = float(self.c2.text())
        a = np.array([[a11, b11],[a22,b22]])
        b = np.array([c11, c22])
        [x,y]=np.linalg.solve(a,b)
        print(x)
        print(y)
        x=str(x)
        y=str(y)
        self.ansx.setText(x)
        self.ansy.setText(y)
    def setupUi(self, LinEquation):
        LinEquation.setObjectName(_fromUtf8("LinEquation"))
        LinEquation.resize(381, 347)
        LinEquation.setStyleSheet(_fromUtf8("\n"
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
        self.a1 = QtGui.QLineEdit(LinEquation)
        self.a1.setGeometry(QtCore.QRect(180, 90, 51, 41))
        self.a1.setText(_fromUtf8(""))
        self.a1.setObjectName(_fromUtf8("a1"))
        self.ansx = QtGui.QLineEdit(LinEquation)
        self.ansx.setEnabled(True)
        self.ansx.setGeometry(QtCore.QRect(90, 240, 271, 41))
        self.ansx.setText(_fromUtf8(""))
        self.ansx.setReadOnly(True)
        self.ansx.setObjectName(_fromUtf8("ansx"))
        self.pushButton = QtGui.QPushButton(LinEquation)
        self.pushButton.setGeometry(QtCore.QRect(160, 200, 97, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton.clicked.connect(self.solve)
        self.c1 = QtGui.QLineEdit(LinEquation)
        self.c1.setGeometry(QtCore.QRect(310, 90, 51, 41))
        self.c1.setText(_fromUtf8(""))
        self.c1.setObjectName(_fromUtf8("c1"))
        self.label1 = QtGui.QLabel(LinEquation)
        self.label1.setGeometry(QtCore.QRect(10, 90, 161, 31))
        self.label1.setObjectName(_fromUtf8("label1"))
        self.b1 = QtGui.QLineEdit(LinEquation)
        self.b1.setGeometry(QtCore.QRect(240, 90, 61, 41))
        self.b1.setText(_fromUtf8(""))
        self.b1.setObjectName(_fromUtf8("b1"))
        self.label4 = QtGui.QLabel(LinEquation)
        self.label4.setGeometry(QtCore.QRect(20, 290, 61, 31))
        self.label4.setObjectName(_fromUtf8("label4"))
        self.label3 = QtGui.QLabel(LinEquation)
        self.label3.setGeometry(QtCore.QRect(20, 250, 51, 31))
        self.label3.setObjectName(_fromUtf8("label3"))
        self.label = QtGui.QLabel(LinEquation)
        self.label.setGeometry(QtCore.QRect(60, 40, 271, 31))
        self.label.setObjectName(_fromUtf8("label"))
        self.ansy = QtGui.QLineEdit(LinEquation)
        self.ansy.setGeometry(QtCore.QRect(90, 290, 271, 41))
        self.ansy.setText(_fromUtf8(""))
        self.ansy.setReadOnly(True)
        self.ansy.setObjectName(_fromUtf8("ansy"))
        self.label_2 = QtGui.QLabel(LinEquation)
        self.label_2.setGeometry(QtCore.QRect(10, 0, 371, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century Schoolbook L"))
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.a2 = QtGui.QLineEdit(LinEquation)
        self.a2.setGeometry(QtCore.QRect(180, 140, 51, 41))
        self.a2.setText(_fromUtf8(""))
        self.a2.setObjectName(_fromUtf8("a2"))
        self.label1_2 = QtGui.QLabel(LinEquation)
        self.label1_2.setGeometry(QtCore.QRect(10, 140, 161, 31))
        self.label1_2.setObjectName(_fromUtf8("label1_2"))
        self.b2 = QtGui.QLineEdit(LinEquation)
        self.b2.setGeometry(QtCore.QRect(240, 140, 61, 41))
        self.b2.setText(_fromUtf8(""))
        self.b2.setObjectName(_fromUtf8("b2"))
        self.c2 = QtGui.QLineEdit(LinEquation)
        self.c2.setGeometry(QtCore.QRect(310, 140, 51, 41))
        self.c2.setText(_fromUtf8(""))
        self.c2.setObjectName(_fromUtf8("c2"))

        self.retranslateUi(LinEquation)
        QtCore.QMetaObject.connectSlotsByName(LinEquation)

    def retranslateUi(self, LinEquation):
        LinEquation.setWindowTitle(_translate("LinEquation", "Form", None))
        self.pushButton.setText(_translate("LinEquation", "Calculate", None))
        self.label1.setText(_translate("LinEquation", "Enter a1 , b1 and c1 \n"
" respectively", None))
        self.label4.setText(_translate("LinEquation", "y=", None))
        self.label3.setText(_translate("LinEquation", "x=", None))
        self.label.setText(_translate("LinEquation", "Equations are of the form a1x+b1y=c1 & \n"
" a2x+b2y=c2", None))
        self.label_2.setText(_translate("LinEquation", "Solving Linear Equation in two Variable", None))
        self.label1_2.setText(_translate("LinEquation", "Enter a2 , b2 and c2 \n"
" respectively", None))
