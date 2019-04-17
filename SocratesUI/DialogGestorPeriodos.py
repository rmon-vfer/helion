# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DialogGestorPeriodos.ui'
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
        Dialog.setEnabled(True)
        Dialog.resize(567, 389)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(567, 389))
        Dialog.setMaximumSize(QtCore.QSize(567, 389))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("graphics/icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setAutoFillBackground(False)
        Dialog.setSizeGripEnabled(False)
        Dialog.setModal(False)
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(10, 10, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.groupBox_3 = QtGui.QGroupBox(Dialog)
        self.groupBox_3.setGeometry(QtCore.QRect(300, 170, 261, 51))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.botonEliminar = QtGui.QPushButton(self.groupBox_3)
        self.botonEliminar.setGeometry(QtCore.QRect(10, 20, 241, 23))
        self.botonEliminar.setObjectName(_fromUtf8("botonEliminar"))
        self.line = QtGui.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(10, 30, 551, 20))
        self.line.setFrameShadow(QtGui.QFrame.Plain)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setObjectName(_fromUtf8("line"))
        self.groupBox_2 = QtGui.QGroupBox(Dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(300, 50, 261, 111))
        self.groupBox_2.setMinimumSize(QtCore.QSize(0, 0))
        self.groupBox_2.setMaximumSize(QtCore.QSize(100000, 100000))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.botonAnadir = QtGui.QPushButton(self.groupBox_2)
        self.botonAnadir.setGeometry(QtCore.QRect(171, 78, 75, 23))
        self.botonAnadir.setObjectName(_fromUtf8("botonAnadir"))
        self.label_4 = QtGui.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(9, 50, 25, 20))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.comboTipoPeriodo = QtGui.QComboBox(self.groupBox_2)
        self.comboTipoPeriodo.setGeometry(QtCore.QRect(40, 24, 211, 20))
        self.comboTipoPeriodo.setObjectName(_fromUtf8("comboTipoPeriodo"))
        self.comboTipoPeriodo.addItem(_fromUtf8(""))
        self.comboTipoPeriodo.addItem(_fromUtf8(""))
        self.comboTipoPeriodo.addItem(_fromUtf8(""))
        self.label_3 = QtGui.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(9, 24, 20, 20))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.selectInicio = QtGui.QDateEdit(self.groupBox_2)
        self.selectInicio.setGeometry(QtCore.QRect(40, 50, 211, 20))
        self.selectInicio.setStyleSheet(_fromUtf8("    /* navigation bar */\n"
"    QCalendarWidget QWidget#qt_calendar_navigationbar { \n"
"            background-color: grey;\n"
"    }"))
        self.selectInicio.setCalendarPopup(True)
        self.selectInicio.setObjectName(_fromUtf8("selectInicio"))
        self.botonAceptar = QtGui.QPushButton(Dialog)
        self.botonAceptar.setGeometry(QtCore.QRect(392, 360, 82, 23))
        self.botonAceptar.setObjectName(_fromUtf8("botonAceptar"))
        self.groupBox = QtGui.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(10, 50, 281, 301))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.tablaPeriodos = QtGui.QTableWidget(self.groupBox)
        self.tablaPeriodos.setGeometry(QtCore.QRect(10, 20, 261, 271))
        self.tablaPeriodos.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tablaPeriodos.setObjectName(_fromUtf8("tablaPeriodos"))
        self.tablaPeriodos.setColumnCount(3)
        self.tablaPeriodos.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tablaPeriodos.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tablaPeriodos.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tablaPeriodos.setHorizontalHeaderItem(2, item)
        self.tablaPeriodos.horizontalHeader().setDefaultSectionSize(80)
        self.tablaPeriodos.verticalHeader().setVisible(False)
        self.tablaPeriodos.verticalHeader().setStretchLastSection(False)
        self.botonAplicar = QtGui.QPushButton(Dialog)
        self.botonAplicar.setGeometry(QtCore.QRect(480, 360, 81, 23))
        self.botonAplicar.setObjectName(_fromUtf8("botonAplicar"))

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.botonAceptar, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Periodos", None))
        self.label_5.setText(_translate("Dialog", "Periodos", None))
        self.groupBox_3.setTitle(_translate("Dialog", "Seleccionado", None))
        self.botonEliminar.setText(_translate("Dialog", "Eliminar", None))
        self.groupBox_2.setTitle(_translate("Dialog", "Nuevo", None))
        self.botonAnadir.setText(_translate("Dialog", "Añadir", None))
        self.label_4.setText(_translate("Dialog", "Inicio", None))
        self.comboTipoPeriodo.setItemText(0, _translate("Dialog", "Mes", None))
        self.comboTipoPeriodo.setItemText(1, _translate("Dialog", "Semestre", None))
        self.comboTipoPeriodo.setItemText(2, _translate("Dialog", "Año", None))
        self.label_3.setText(_translate("Dialog", "Tipo", None))
        self.botonAceptar.setText(_translate("Dialog", "Aceptar", None))
        self.groupBox.setTitle(_translate("Dialog", "Periodos activos", None))
        item = self.tablaPeriodos.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Inicio", None))
        item = self.tablaPeriodos.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Fin", None))
        item = self.tablaPeriodos.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Tipo", None))
        self.botonAplicar.setText(_translate("Dialog", "Aplicar", None))
