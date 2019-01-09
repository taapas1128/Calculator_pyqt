# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menuu.ui'
#
# Created by: PyQt4 UI code generator 4.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from equation import Ui_Form
from linequ import Ui_LinEquation
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

class Ui_Menu(object):
    def openWindow(self):
        self.window = QtGui.QMainWindow()
        self.ui = Ui_Form()
        self.ui.setupUi(self.window)
        self.window.show()
    def openWindowl(self):
        self.window = QtGui.QMainWindow()
        self.ui = Ui_LinEquation()
        self.ui.setupUi(self.window)
        self.window.show()
    def setupUi(self, Menu):
        Menu.setObjectName(_fromUtf8("Menu"))
        Menu.resize(306, 179)
        Menu.setStyleSheet(_fromUtf8("\n"
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
"}\n"
""))
        self.label = QtGui.QLabel(Menu)
        self.label.setGeometry(QtCore.QRect(80, 0, 151, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century Schoolbook L"))
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.linequ = QtGui.QPushButton(Menu)
        self.linequ.setGeometry(QtCore.QRect(10, 50, 281, 51))
        self.linequ.setObjectName(_fromUtf8("linequ"))
        self.quadequ = QtGui.QPushButton(Menu)
        self.quadequ.setGeometry(QtCore.QRect(10, 110, 281, 51))
        self.quadequ.setObjectName(_fromUtf8("quadequ"))
        self.linequ.clicked.connect(self.openWindowl)
        self.quadequ.clicked.connect(self.openWindow)

        self.retranslateUi(Menu)
        QtCore.QMetaObject.connectSlotsByName(Menu)

    def retranslateUi(self, Menu):
        Menu.setWindowTitle(_translate("Menu", "Form", None))
        self.label.setText(_translate("Menu", "Equation Menu", None))
        self.linequ.setText(_translate("Menu", "Solve Linear Equation in two Variable", None))
        self.quadequ.setText(_translate("Menu", "Solve Quadratic equation", None))
