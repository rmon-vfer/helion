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
        Dialog.resize(858, 522)
        Dialog.setMinimumSize(QtCore.QSize(858, 522))
        Dialog.setMaximumSize(QtCore.QSize(858, 522))
        Dialog.setAutoFillBackground(False)
        Dialog.setSizeGripEnabled(False)
        Dialog.setModal(False)
        self.line = QtGui.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(10, 30, 841, 16))
        self.line.setFrameShadow(QtGui.QFrame.Plain)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setObjectName(_fromUtf8("line"))
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(10, 10, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.groupBox = QtGui.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(10, 50, 281, 431))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.periodosTable = QtGui.QTableWidget(self.groupBox)
        self.periodosTable.setGeometry(QtCore.QRect(10, 20, 261, 401))
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
        self.periodosTable.verticalHeader().setVisible(False)
        self.periodosTable.verticalHeader().setStretchLastSection(False)
        self.groupBox_2 = QtGui.QGroupBox(Dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(300, 50, 551, 371))
        self.groupBox_2.setMinimumSize(QtCore.QSize(0, 0))
        self.groupBox_2.setMaximumSize(QtCore.QSize(100000, 100000))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.line_2 = QtGui.QFrame(self.groupBox_2)
        self.line_2.setGeometry(QtCore.QRect(10, 40, 531, 20))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.label_6 = QtGui.QLabel(self.groupBox_2)
        self.label_6.setGeometry(QtCore.QRect(10, 60, 61, 16))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_12 = QtGui.QLabel(self.groupBox_2)
        self.label_12.setGeometry(QtCore.QRect(280, 60, 51, 16))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.siguienteButtonFin = QtGui.QPushButton(self.groupBox_2)
        self.siguienteButtonFin.setGeometry(QtCore.QRect(460, 290, 81, 23))
        self.siguienteButtonFin.setObjectName(_fromUtf8("siguienteButtonFin"))
        self.frame_2 = QtGui.QFrame(self.groupBox_2)
        self.frame_2.setGeometry(QtCore.QRect(280, 80, 261, 21))
        self.frame_2.setFrameShape(QtGui.QFrame.Box)
        self.frame_2.setFrameShadow(QtGui.QFrame.Plain)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.labelInicio = QtGui.QLabel(self.frame_2)
        self.labelInicio.setGeometry(QtCore.QRect(0, 0, 261, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labelInicio.setFont(font)
        self.labelInicio.setObjectName(_fromUtf8("labelInicio"))
        self.calendarioFin = QtGui.QCalendarWidget(self.groupBox_2)
        self.calendarioFin.setGeometry(QtCore.QRect(280, 110, 261, 171))
        self.calendarioFin.setLocale(QtCore.QLocale(QtCore.QLocale.Spanish, QtCore.QLocale.Spain))
        self.calendarioFin.setFirstDayOfWeek(QtCore.Qt.Monday)
        self.calendarioFin.setGridVisible(False)
        self.calendarioFin.setHorizontalHeaderFormat(QtGui.QCalendarWidget.SingleLetterDayNames)
        self.calendarioFin.setVerticalHeaderFormat(QtGui.QCalendarWidget.NoVerticalHeader)
        self.calendarioFin.setNavigationBarVisible(False)
        self.calendarioFin.setObjectName(_fromUtf8("calendarioFin"))
        self.frame = QtGui.QFrame(self.groupBox_2)
        self.frame.setGeometry(QtCore.QRect(10, 80, 261, 21))
        self.frame.setFrameShape(QtGui.QFrame.Box)
        self.frame.setFrameShadow(QtGui.QFrame.Plain)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.mesLabel = QtGui.QLabel(self.frame)
        self.mesLabel.setGeometry(QtCore.QRect(0, 0, 261, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.mesLabel.setFont(font)
        self.mesLabel.setObjectName(_fromUtf8("mesLabel"))
        self.hoyButtonInicio = QtGui.QPushButton(self.groupBox_2)
        self.hoyButtonInicio.setGeometry(QtCore.QRect(100, 290, 81, 23))
        self.hoyButtonInicio.setObjectName(_fromUtf8("hoyButtonInicio"))
        self.hoyButtonFin = QtGui.QPushButton(self.groupBox_2)
        self.hoyButtonFin.setGeometry(QtCore.QRect(370, 290, 81, 23))
        self.hoyButtonFin.setObjectName(_fromUtf8("hoyButtonFin"))
        self.calendarioInicio = QtGui.QCalendarWidget(self.groupBox_2)
        self.calendarioInicio.setGeometry(QtCore.QRect(10, 110, 261, 171))
        self.calendarioInicio.setLocale(QtCore.QLocale(QtCore.QLocale.Spanish, QtCore.QLocale.Spain))
        self.calendarioInicio.setFirstDayOfWeek(QtCore.Qt.Monday)
        self.calendarioInicio.setGridVisible(False)
        self.calendarioInicio.setHorizontalHeaderFormat(QtGui.QCalendarWidget.SingleLetterDayNames)
        self.calendarioInicio.setVerticalHeaderFormat(QtGui.QCalendarWidget.NoVerticalHeader)
        self.calendarioInicio.setNavigationBarVisible(False)
        self.calendarioInicio.setObjectName(_fromUtf8("calendarioInicio"))
        self.siguienteButtonInicio = QtGui.QPushButton(self.groupBox_2)
        self.siguienteButtonInicio.setGeometry(QtCore.QRect(190, 290, 81, 23))
        self.siguienteButtonInicio.setObjectName(_fromUtf8("siguienteButtonInicio"))
        self.anteriorButtonFin = QtGui.QPushButton(self.groupBox_2)
        self.anteriorButtonFin.setGeometry(QtCore.QRect(280, 290, 81, 23))
        self.anteriorButtonFin.setObjectName(_fromUtf8("anteriorButtonFin"))
        self.anteriorButtonInicio = QtGui.QPushButton(self.groupBox_2)
        self.anteriorButtonInicio.setGeometry(QtCore.QRect(10, 290, 81, 23))
        self.anteriorButtonInicio.setObjectName(_fromUtf8("anteriorButtonInicio"))
        self.label_4 = QtGui.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(503, 20, 37, 15))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_3 = QtGui.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(323, 19, 50, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.editInicio = QtGui.QLineEdit(self.groupBox_2)
        self.editInicio.setGeometry(QtCore.QRect(50, 19, 117, 17))
        self.editInicio.setReadOnly(True)
        self.editInicio.setObjectName(_fromUtf8("editInicio"))
        self.editFin = QtGui.QLineEdit(self.groupBox_2)
        self.editFin.setGeometry(QtCore.QRect(198, 19, 117, 17))
        self.editFin.setReadOnly(True)
        self.editFin.setObjectName(_fromUtf8("editFin"))
        self.label_2 = QtGui.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(175, 19, 17, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label = QtGui.QLabel(self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(14, 19, 30, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.editDuracion = QtGui.QLineEdit(self.groupBox_2)
        self.editDuracion.setGeometry(QtCore.QRect(380, 20, 117, 17))
        self.editDuracion.setReadOnly(True)
        self.editDuracion.setObjectName(_fromUtf8("editDuracion"))
        self.addButton = QtGui.QPushButton(self.groupBox_2)
        self.addButton.setGeometry(QtCore.QRect(10, 340, 531, 23))
        self.addButton.setObjectName(_fromUtf8("addButton"))
        self.line_3 = QtGui.QFrame(self.groupBox_2)
        self.line_3.setGeometry(QtCore.QRect(10, 320, 531, 20))
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.groupBox_3 = QtGui.QGroupBox(Dialog)
        self.groupBox_3.setGeometry(QtCore.QRect(300, 430, 551, 51))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.buttonEliminar = QtGui.QPushButton(self.groupBox_3)
        self.buttonEliminar.setGeometry(QtCore.QRect(10, 20, 531, 23))
        self.buttonEliminar.setObjectName(_fromUtf8("buttonEliminar"))
        self.botonOk = QtGui.QPushButton(Dialog)
        self.botonOk.setGeometry(QtCore.QRect(682, 490, 82, 23))
        self.botonOk.setObjectName(_fromUtf8("botonOk"))
        self.botonAplicar = QtGui.QPushButton(Dialog)
        self.botonAplicar.setGeometry(QtCore.QRect(770, 490, 81, 23))
        self.botonAplicar.setObjectName(_fromUtf8("botonAplicar"))

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.botonOk, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Periodos", None))
        self.label_5.setText(_translate("Dialog", "Periodos", None))
        self.groupBox.setTitle(_translate("Dialog", "Periodos activos", None))
        item = self.periodosTable.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Inicio", None))
        item = self.periodosTable.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Fin", None))
        item = self.periodosTable.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Duración", None))
        self.groupBox_2.setTitle(_translate("Dialog", "Nuevo", None))
        self.label_6.setText(_translate("Dialog", "Fecha inicio", None))
        self.label_12.setText(_translate("Dialog", "Fecha fin", None))
        self.siguienteButtonFin.setText(_translate("Dialog", "Siguiente", None))
        self.labelInicio.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-weight:400;\">Enero - 2019</span></p></body></html>", None))
        self.mesLabel.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-weight:400;\">Diciembre - 2019</span></p></body></html>", None))
        self.hoyButtonInicio.setText(_translate("Dialog", "Hoy", None))
        self.hoyButtonFin.setText(_translate("Dialog", "Hoy", None))
        self.siguienteButtonInicio.setText(_translate("Dialog", "Siguiente", None))
        self.anteriorButtonFin.setText(_translate("Dialog", "Anterior", None))
        self.anteriorButtonInicio.setText(_translate("Dialog", "Anterior", None))
        self.label_4.setText(_translate("Dialog", "meses", None))
        self.label_3.setText(_translate("Dialog", "Duración", None))
        self.label_2.setText(_translate("Dialog", "Fin", None))
        self.label.setText(_translate("Dialog", "Inicio", None))
        self.addButton.setText(_translate("Dialog", "Añadir", None))
        self.groupBox_3.setTitle(_translate("Dialog", "General", None))
        self.buttonEliminar.setText(_translate("Dialog", "Eliminar periodo seleccionado", None))
        self.botonOk.setText(_translate("Dialog", "Aceptar", None))
        self.botonAplicar.setText(_translate("Dialog", "Aplicar", None))

