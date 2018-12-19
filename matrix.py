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
        Matwin.resize(851, 681)
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
        self.edit = QtGui.QPushButton(self.frame)
        self.edit.setGeometry(QtCore.QRect(180, 120, 161, 51))
        self.edit.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.edit.setObjectName(_fromUtf8("edit"))
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
        self.clr.setGeometry(QtCore.QRect(350, 120, 161, 51))
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
        self.new_mat.setText(_translate("Matwin", "New Matrix", None))
        self.edit.setText(_translate("Matwin", "Edit Matrix", None))
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

