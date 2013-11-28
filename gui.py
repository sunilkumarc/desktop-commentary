# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'score.ui'
#
# Created: Thu Nov 28 12:08:13 2013
#      by: PyQt4 UI code generator 4.10
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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(667, 101)
        Form.setMouseTracking(True)
        Form.setAcceptDrops(True)
        Form.setAutoFillBackground(True)
        self.start = QtGui.QPushButton(Form)
        self.start.setGeometry(QtCore.QRect(240, 60, 161, 31))
        self.start.setObjectName(_fromUtf8("start"))
        self.scoreurl = QtGui.QTextEdit(Form)
        self.scoreurl.setGeometry(QtCore.QRect(20, 10, 631, 41))
        self.scoreurl.setObjectName(_fromUtf8("scoreurl"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Cricinfo Score App", None))
        self.start.setText(_translate("Form", "Start", None))

