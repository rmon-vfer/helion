# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DialogEditorTurnosPorEmpleado.ui'
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
        Dialog.resize(588, 381)
        Dialog.setMinimumSize(QtCore.QSize(588, 381))
        Dialog.setMaximumSize(QtCore.QSize(588, 381))
        Dialog.setAcceptDrops(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("graphics/icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(10, 10, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.line = QtGui.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(10, 30, 571, 16))
        self.line.setFrameShadow(QtGui.QFrame.Plain)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setObjectName(_fromUtf8("line"))
        self.groupBox = QtGui.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(280, 50, 301, 281))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.guardiasTable = QtGui.QTableWidget(self.groupBox)
        self.guardiasTable.setGeometry(QtCore.QRect(10, 20, 281, 251))
        self.guardiasTable.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.guardiasTable.setObjectName(_fromUtf8("guardiasTable"))
        self.guardiasTable.setColumnCount(3)
        self.guardiasTable.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.guardiasTable.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.guardiasTable.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.guardiasTable.setHorizontalHeaderItem(2, item)
        self.guardiasTable.horizontalHeader().setDefaultSectionSize(60)
        self.guardiasTable.horizontalHeader().setStretchLastSection(True)
        self.guardiasTable.verticalHeader().setVisible(False)
        self.guardiasTable.verticalHeader().setStretchLastSection(False)
        self.groupBox_3 = QtGui.QGroupBox(Dialog)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 50, 261, 61))
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
        self.botonAplicar = QtGui.QPushButton(Dialog)
        self.botonAplicar.setGeometry(QtCore.QRect(498, 350, 81, 23))
        self.botonAplicar.setObjectName(_fromUtf8("botonAplicar"))
        self.botonOk = QtGui.QPushButton(Dialog)
        self.botonOk.setGeometry(QtCore.QRect(410, 350, 82, 23))
        self.botonOk.setObjectName(_fromUtf8("botonOk"))
        self.groupBox_2 = QtGui.QGroupBox(Dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 120, 261, 111))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.addButton = QtGui.QPushButton(self.groupBox_2)
        self.addButton.setGeometry(QtCore.QRect(170, 80, 81, 23))
        self.addButton.setObjectName(_fromUtf8("addButton"))
        self.eliminarButton = QtGui.QPushButton(self.groupBox_2)
        self.eliminarButton.setGeometry(QtCore.QRect(90, 80, 75, 23))
        self.eliminarButton.setObjectName(_fromUtf8("eliminarButton"))
        self.comboTurno = QtGui.QComboBox(self.groupBox_2)
        self.comboTurno.setGeometry(QtCore.QRect(40, 20, 211, 20))
        self.comboTurno.setEditable(False)
        self.comboTurno.setObjectName(_fromUtf8("comboTurno"))
        self.comboTurno.addItem(_fromUtf8(""))
        self.comboTurno.addItem(_fromUtf8(""))
        self.label_4 = QtGui.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(14, 46, 15, 20))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.dateEdit = QtGui.QDateEdit(self.groupBox_2)
        self.dateEdit.setGeometry(QtCore.QRect(40, 46, 211, 20))
        self.dateEdit.setStyleSheet(_fromUtf8("    /* navigation bar */\n"
"    QCalendarWidget QWidget#qt_calendar_navigationbar { \n"
"            background-color: grey;\n"
"    }"))
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setObjectName(_fromUtf8("dateEdit"))
        self.label_6 = QtGui.QLabel(self.groupBox_2)
        self.label_6.setGeometry(QtCore.QRect(14, 20, 20, 20))
        self.label_6.setObjectName(_fromUtf8("label_6"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Guardias", None))
        self.label_5.setText(_translate("Dialog", "Guardias", None))
        self.groupBox.setTitle(_translate("Dialog", "Guardias del mes", None))
        item = self.guardiasTable.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Día", None))
        item = self.guardiasTable.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Turno", None))
        item = self.guardiasTable.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Especial", None))
        self.groupBox_3.setTitle(_translate("Dialog", "Trabajador/a", None))
        self.label_2.setText(_translate("Dialog", "Apellidos", None))
        self.label.setText(_translate("Dialog", "Nombre", None))
        self.botonAplicar.setText(_translate("Dialog", "Aplicar", None))
        self.botonOk.setText(_translate("Dialog", "Aceptar", None))
        self.groupBox_2.setTitle(_translate("Dialog", "Añadir guardias", None))
        self.addButton.setText(_translate("Dialog", "Añadir", None))
        self.eliminarButton.setText(_translate("Dialog", "Eliminar", None))
        self.comboTurno.setItemText(0, _translate("Dialog", "A", None))
        self.comboTurno.setItemText(1, _translate("Dialog", "B", None))
        self.label_4.setText(_translate("Dialog", "Día", None))
        self.label_6.setText(_translate("Dialog", "Tipo", None))

