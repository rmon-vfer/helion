# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DialogResumenMensual.ui'
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
        Dialog.setWindowModality(QtCore.Qt.NonModal)
        Dialog.resize(866, 468)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(866, 468))
        Dialog.setMaximumSize(QtCore.QSize(866, 468))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("graphics/icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setModal(False)
        self.groupBox = QtGui.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(300, 50, 551, 411))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.resultsTable = QtGui.QTableWidget(self.groupBox)
        self.resultsTable.setEnabled(True)
        self.resultsTable.setGeometry(QtCore.QRect(10, 20, 531, 381))
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
        self.resultsTable.setColumnCount(5)
        self.resultsTable.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.resultsTable.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.resultsTable.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.resultsTable.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.resultsTable.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.resultsTable.setHorizontalHeaderItem(4, item)
        self.resultsTable.horizontalHeader().setDefaultSectionSize(104)
        self.resultsTable.horizontalHeader().setStretchLastSection(True)
        self.resultsTable.verticalHeader().setVisible(True)
        self.resultsTable.verticalHeader().setDefaultSectionSize(22)
        self.resultsTable.verticalHeader().setMinimumSectionSize(15)
        self.resultsTable.verticalHeader().setStretchLastSection(False)
        self.line = QtGui.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(10, 30, 841, 16))
        self.line.setFrameShadow(QtGui.QFrame.Plain)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setObjectName(_fromUtf8("line"))
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(10, 10, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.groupBox_2 = QtGui.QGroupBox(Dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 50, 281, 411))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.periodosTable = QtGui.QTableWidget(self.groupBox_2)
        self.periodosTable.setGeometry(QtCore.QRect(10, 20, 261, 381))
        self.periodosTable.setAlternatingRowColors(True)
        self.periodosTable.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.periodosTable.setObjectName(_fromUtf8("periodosTable"))
        self.periodosTable.setColumnCount(3)
        self.periodosTable.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.periodosTable.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.periodosTable.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.periodosTable.setHorizontalHeaderItem(2, item)
        self.periodosTable.horizontalHeader().setDefaultSectionSize(80)
        self.periodosTable.verticalHeader().setVisible(True)
        self.periodosTable.verticalHeader().setStretchLastSection(False)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Resumen mensual", None))
        self.groupBox.setTitle(_translate("Dialog", "Seleccionado", None))
        self.resultsTable.setSortingEnabled(True)
        item = self.resultsTable.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Nombre", None))
        item = self.resultsTable.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Apellidos", None))
        item = self.resultsTable.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Lectivas", None))
        item = self.resultsTable.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "F/S o Festivos", None))
        item = self.resultsTable.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "Horas totales", None))
        self.label_5.setText(_translate("Dialog", "Resumen mensual", None))
        self.groupBox_2.setTitle(_translate("Dialog", "Disponibles", None))
        item = self.periodosTable.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Inicio", None))
        item = self.periodosTable.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Fin", None))
        item = self.periodosTable.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Tipo", None))
