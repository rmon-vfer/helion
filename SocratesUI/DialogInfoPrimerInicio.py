# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DialogInfoPrimerInicio.ui'
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(500, 273)
        Dialog.setMinimumSize(QtCore.QSize(500, 273))
        Dialog.setMaximumSize(QtCore.QSize(500, 273))
        Dialog.setWindowIcon(QtGui.QIcon("./graphics/icon.ico"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 10, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.line = QtGui.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(10, 30, 481, 31))
        self.line.setFrameShadow(QtGui.QFrame.Plain)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setObjectName(_fromUtf8("line"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 60, 481, 161))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.continuarB = QtGui.QPushButton(Dialog)
        self.continuarB.setGeometry(QtCore.QRect(410, 240, 75, 23))
        self.continuarB.setObjectName(_fromUtf8("continuarB"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Inicio", None))
        self.label.setText(_translate("Dialog", "Configuración inicial", None))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p align=\"justify\">¡Bienvenido/a a Helion!</p><p align=\"justify\">Para poder utilizar todas las características de Helion, antes es necesario que añadas los datos de los trabajadores así como las guardias correspondientes a cada uno a la base de datos del programa. Después tendrás que añadir los periodos (mes, semestre o año) en los que quieres que se contabilicen las distintas guardias, de esa manera, lo único que tendrás que hacer es consultar los resúmenes y modificar las guardias del personal.</p></body></html>", None))
        self.continuarB.setText(_translate("Dialog", "Continuar", None))

