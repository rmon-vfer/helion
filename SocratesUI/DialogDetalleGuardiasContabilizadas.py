# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DialogDetalleGuardiasContabilizadas.ui'
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
        Dialog.resize(440, 391)
        Dialog.setMinimumSize(QtCore.QSize(440, 391))
        Dialog.setMaximumSize(QtCore.QSize(440, 391))
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(10, 10, 271, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.line = QtGui.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(10, 30, 421, 20))
        self.line.setFrameShadow(QtGui.QFrame.Plain)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setObjectName(_fromUtf8("line"))
        self.groupBox_3 = QtGui.QGroupBox(Dialog)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 50, 421, 61))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.labelApellidos = QtGui.QLabel(self.groupBox_3)
        self.labelApellidos.setGeometry(QtCore.QRect(67, 37, 182, 12))
        self.labelApellidos.setText(_fromUtf8(""))
        self.labelApellidos.setObjectName(_fromUtf8("labelApellidos"))
        self.labelNombre = QtGui.QLabel(self.groupBox_3)
        self.labelNombre.setGeometry(QtCore.QRect(67, 20, 182, 11))
        self.labelNombre.setText(_fromUtf8(""))
        self.labelNombre.setObjectName(_fromUtf8("labelNombre"))
        self.label_2 = QtGui.QLabel(self.groupBox_3)
        self.label_2.setGeometry(QtCore.QRect(10, 37, 51, 12))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label = QtGui.QLabel(self.groupBox_3)
        self.label.setGeometry(QtCore.QRect(10, 20, 44, 11))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.resultsTable = QtGui.QTableWidget(Dialog)
        self.resultsTable.setEnabled(True)
        self.resultsTable.setGeometry(QtCore.QRect(10, 120, 421, 261))
        self.resultsTable.setAutoFillBackground(False)
        self.resultsTable.setFrameShape(QtGui.QFrame.StyledPanel)
        self.resultsTable.setFrameShadow(QtGui.QFrame.Plain)
        self.resultsTable.setAutoScrollMargin(16)
        self.resultsTable.setAlternatingRowColors(True)
        self.resultsTable.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.resultsTable.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.resultsTable.setShowGrid(True)
        self.resultsTable.setGridStyle(QtCore.Qt.SolidLine)
        self.resultsTable.setObjectName(_fromUtf8("resultsTable"))
        self.resultsTable.setColumnCount(3)
        self.resultsTable.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.resultsTable.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.resultsTable.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.resultsTable.setHorizontalHeaderItem(2, item)
        self.resultsTable.horizontalHeader().setDefaultSectionSize(104)
        self.resultsTable.horizontalHeader().setStretchLastSection(False)
        self.resultsTable.verticalHeader().setVisible(True)
        self.resultsTable.verticalHeader().setDefaultSectionSize(22)
        self.resultsTable.verticalHeader().setMinimumSectionSize(15)
        self.resultsTable.verticalHeader().setStretchLastSection(False)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Detalle", None))
        self.label_5.setText(_translate("Dialog", "Guardias contabilizadas", None))
        self.groupBox_3.setTitle(_translate("Dialog", "Trabajador/a", None))
        self.label_2.setText(_translate("Dialog", "Apellidos", None))
        self.label.setText(_translate("Dialog", "Nombre", None))
        self.resultsTable.setSortingEnabled(True)
        item = self.resultsTable.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Fecha", None))
        item = self.resultsTable.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Tipo", None))
        item = self.resultsTable.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Especial", None))

