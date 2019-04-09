# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindowMenu.ui'
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(329, 261)
        MainWindow.setMinimumSize(QtCore.QSize(329, 261))
        MainWindow.setMaximumSize(QtCore.QSize(329, 261))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/graphics/icon.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 161, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Shell Dlg 2"))
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.groupBox_2 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 50, 311, 81))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.administrarPersonal = QtGui.QPushButton(self.groupBox_2)
        self.administrarPersonal.setGeometry(QtCore.QRect(10, 20, 291, 23))
        self.administrarPersonal.setObjectName(_fromUtf8("administrarPersonal"))
        self.administrarPeriodos = QtGui.QPushButton(self.groupBox_2)
        self.administrarPeriodos.setGeometry(QtCore.QRect(10, 50, 291, 23))
        self.administrarPeriodos.setObjectName(_fromUtf8("administrarPeriodos"))
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 30, 311, 16))
        self.line.setFrameShadow(QtGui.QFrame.Plain)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setObjectName(_fromUtf8("line"))
        self.groupBox_3 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(170, 140, 151, 111))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.acerca = QtGui.QPushButton(self.groupBox_3)
        self.acerca.setGeometry(QtCore.QRect(10, 50, 129, 23))
        self.acerca.setObjectName(_fromUtf8("acerca"))
        self.groupBox_4 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 140, 151, 111))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.resMensual = QtGui.QPushButton(self.groupBox_4)
        self.resMensual.setGeometry(QtCore.QRect(10, 20, 131, 23))
        self.resMensual.setObjectName(_fromUtf8("resMensual"))
        self.resSemestral = QtGui.QPushButton(self.groupBox_4)
        self.resSemestral.setGeometry(QtCore.QRect(10, 50, 131, 23))
        self.resSemestral.setObjectName(_fromUtf8("resSemestral"))
        self.resAnual = QtGui.QPushButton(self.groupBox_4)
        self.resAnual.setGeometry(QtCore.QRect(10, 80, 131, 23))
        self.resAnual.setObjectName(_fromUtf8("resAnual"))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Menú principal", None))
        self.label.setText(_translate("MainWindow", "Menú Principal", None))
        self.groupBox_2.setTitle(_translate("MainWindow", "Administración", None))
        self.administrarPersonal.setText(_translate("MainWindow", "Personal", None))
        self.administrarPeriodos.setText(_translate("MainWindow", "Periodos", None))
        self.groupBox_3.setTitle(_translate("MainWindow", "Otros", None))
        self.acerca.setText(_translate("MainWindow", "Acerca", None))
        self.groupBox_4.setTitle(_translate("MainWindow", "Resúmenes", None))
        self.resMensual.setText(_translate("MainWindow", "Mensual", None))
        self.resSemestral.setText(_translate("MainWindow", "Semestral", None))
        self.resAnual.setText(_translate("MainWindow", "Anual", None))