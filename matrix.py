# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'matrix.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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

class Ui_Matwin(object):
    def setupUi(self, Matwin):
        Matwin.setObjectName(_fromUtf8("Matwin"))
        Matwin.resize(851, 670)
        Matwin.setMinimumSize(QtCore.QSize(851, 670))
        Matwin.setMaximumSize(QtCore.QSize(851, 670))
        Matwin.setStyleSheet(_fromUtf8("\n"
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
        self.centralwidget = QtGui.QWidget(Matwin)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.frame_2 = QtGui.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(10, 10, 831, 601))
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.frame = QtGui.QFrame(self.frame_2)
        self.frame.setGeometry(QtCore.QRect(40, 20, 771, 541))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.ds2 = QtGui.QLineEdit(self.frame)
        self.ds2.setGeometry(QtCore.QRect(10, 10, 611, 91))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Yu Gothic UI Semibold"))
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.ds2.setFont(font)
        self.ds2.setObjectName(_fromUtf8("ds2"))
        self.solve = QtGui.QPushButton(self.frame)
        self.solve.setGeometry(QtCore.QRect(630, 10, 131, 91))
        self.solve.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.solve.setObjectName(_fromUtf8("solve"))
        self.new_mat = QtGui.QPushButton(self.frame)
        self.new_mat.setGeometry(QtCore.QRect(10, 120, 161, 51))
        self.new_mat.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.new_mat.setObjectName(_fromUtf8("new_mat"))
        self.line = QtGui.QFrame(self.frame)
        self.line.setGeometry(QtCore.QRect(0, 180, 771, 31))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.label = QtGui.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(20, 210, 211, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.line_2 = QtGui.QFrame(self.frame)
        self.line_2.setGeometry(QtCore.QRect(0, 260, 771, 16))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.op = QtGui.QTextEdit(self.frame)
        self.op.setGeometry(QtCore.QRect(0, 280, 771, 261))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Trebuchet MS"))
        font.setPointSize(12)
        self.op.setFont(font)
        self.op.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.op.setObjectName(_fromUtf8("op"))
        self.clear = QtGui.QPushButton(self.frame)
        self.clear.setGeometry(QtCore.QRect(670, 210, 81, 51))
        self.clear.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.clear.setObjectName(_fromUtf8("clear"))
        self.clr = QtGui.QPushButton(self.frame)
        self.clr.setGeometry(QtCore.QRect(190, 120, 161, 51))
        self.clr.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.clr.setObjectName(_fromUtf8("clr"))
        Matwin.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(Matwin)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 851, 26))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        Matwin.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(Matwin)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        Matwin.setStatusBar(self.statusbar)

        self.retranslateUi(Matwin)
        QtCore.QMetaObject.connectSlotsByName(Matwin)

    def retranslateUi(self, Matwin):
        Matwin.setWindowTitle(_translate("Matwin", "MainWindow", None))
        self.solve.setText(_translate("Matwin", "Solve", None))
        self.new_mat.setText(_translate("Matwin", "Add Matrix", None))
        self.label.setText(_translate("Matwin", "Output :", None))
        self.clear.setText(_translate("Matwin", "AC", None))
        self.clr.setText(_translate("Matwin", "Clear", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Matwin = QtGui.QMainWindow()
    ui = Ui_Matwin()
    ui.setupUi(Matwin)
    Matwin.show()
    sys.exit(app.exec_())

