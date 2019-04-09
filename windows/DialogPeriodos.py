import datetime
import os
import pickle
import shutil
import sys

import arrow
from PyQt4 import *
from PyQt4 import Qt, QtCore, QtGui

from CommonUtils import CommonUtils
from SocratesUI.DialogGestorPeriodos import Ui_Dialog as Ui_DialogPeriodos
from windows import (DialogEditorTurnos, DialogGestorPersonal,
                     DialogPrimerInicio, DialogResSemestral, MainWindow)


class DialogPeriodos(QtGui.QDialog, Ui_DialogPeriodos, object):

    def __init__(self, parent = None):
        QtGui.QDialog.__init__(self,parent) 
        self.setupUi(self)

        self.userData = ""
        self.periodos = ""

        self.diaSeleccionadoInicio = arrow.now()
        self.diaSeleccionadoFin = self.diaSeleccionadoInicio + datetime.timedelta(days=31)

        self.loadData()
        self.refrescarCalendarios()

        self.anteriorButtonInicio.clicked.connect(self.mesAnteriorInicio)
        self.hoyButtonInicio.clicked.connect(self.mostrarHoyInicio)
        self.siguienteButtonInicio.clicked.connect(self.mesSiguienteInicio)

        self.anteriorButtonFin.clicked.connect(self.mesAnteriorFin)
        self.hoyButtonFin.clicked.connect(self.mostrarHoyFin)
        self.siguienteButtonFin.clicked.connect(self.mesSiguienteFin)
        self.addButton.clicked.connect(self.anadirPeriodo)
        self.calendarioInicio.clicked.connect(self.refrescarEdits)
        self.calendarioFin.clicked.connect(self.refrescarEdits)
        self.buttonEliminar.clicked.connect(self.eliminarPeriodo)
    
    def anadirPeriodo(self):
        mesI  = self.calendarioInicio.selectedDate().month()
        diaI  = self.calendarioInicio.selectedDate().day()
        anyoI = self.calendarioInicio.selectedDate().year()
        inicio = arrow.Arrow(anyoI, mesI, diaI)

        mesF  = self.calendarioFin.selectedDate().month()
        diaF  = self.calendarioFin.selectedDate().day()
        anyoF = self.calendarioFin.selectedDate().year()
        fin = arrow.Arrow(anyoF, mesF, diaF)
        
        CommonUtils.anadirPeriodo(inicio, fin)

        self.recargarTablaPeriodos()

    def mostrarHoyInicio(self):
        self.diaSeleccionadoInicio = arrow.now()
        self.refrescarCalendarios()

    def mostrarHoyFin(self):
        self.diaSeleccionadoFin = arrow.now()
        self.refrescarCalendarios()

    def closeWindow(self):
        self.close()

    def loadData(self):
        self.userData = CommonUtils.getUserData()
        self.recargarTablaPeriodos()
    
    def mesSiguienteInicio(self):
        self.diaSeleccionadoInicio += datetime.timedelta(days=30)
        self.refrescarCalendarios()

    def mesAnteriorInicio(self):
        self.diaSeleccionadoInicio -= datetime.timedelta(days=30)
        self.refrescarCalendarios()

    def mesSiguienteFin(self):
        self.diaSeleccionadoFin += datetime.timedelta(days=30)
        self.refrescarCalendarios()

    def mesAnteriorFin(self):
        self.diaSeleccionadoFin -= datetime.timedelta(days=30)
        self.refrescarCalendarios()

    def recargarTablaPeriodos(self):
        self.userData = CommonUtils.getUserData()
        self.periodos = self.userData["periodos"]
        print(self.periodos)
        self.periodosTable.setRowCount(len(self.periodos))
        
        for periodo_index in range(len(self.periodos)):
            periodo = self.periodos[periodo_index]
            inicio = periodo["inicio"]
            fin = periodo["final"]
            duracion = (CommonUtils.stringToArrow(fin) - CommonUtils.stringToArrow(inicio))
            duracion = duracion.days/31
            duracion = round(duracion, 2)

            # Establecer el inicio y final
            self.periodosTable.setItem(periodo_index, 0, QtGui.QTableWidgetItem(inicio))
            self.periodosTable.setItem(periodo_index, 1, QtGui.QTableWidgetItem(fin))
            self.periodosTable.setItem(periodo_index, 2, QtGui.QTableWidgetItem(str(duracion)))
        
        self.periodosTable.resizeColumnsToContents()

    def eliminarPeriodo(self):
        rowIndex = self.periodosTable.currentRow()
        self.periodosTable.removeRow(rowIndex)
        del self.userData["periodos"][rowIndex]

        CommonUtils.updateUserData(self.userData)
        self.recargarTablaPeriodos()

    def textoCentrado(self, texto):
        return f"""
        <html>
            <head/>
            <body>
                <p align="center"><span style=" font-weight:400;">{texto}</span>
                </p><
            /body>
        </html>
        """
        
    def refrescarEdits(self):
        mesI  = self.calendarioInicio.selectedDate().month()
        diaI  = self.calendarioInicio.selectedDate().day()
        anyoI = self.calendarioInicio.selectedDate().year()
        inicio = arrow.Arrow(anyoI, mesI, diaI)

        mesF  = self.calendarioFin.selectedDate().month()
        diaF  = self.calendarioFin.selectedDate().day()
        anyoF = self.calendarioFin.selectedDate().year()
        fin = arrow.Arrow(anyoF, mesF, diaF)
        
        duracion = fin - inicio
        duracion = duracion.days/31
        duracion = round(duracion, 2)

        self.editInicio.setText(CommonUtils.arrowToString(inicio))
        self.editFin.setText(CommonUtils.arrowToString(fin))
        self.editDuracion.setText(str(duracion))

    def refrescarCalendarios(self):
        print(self.diaSeleccionadoInicio.strftime("%d-%m-%Y"))
        print(self.diaSeleccionadoFin.strftime("%d-%m-%Y"))
        print("\n----------------------\n")


        #TODO: Ver por qué no funciona
        self.calendarioInicio.setSelectedDate(
            Qt.QDateTime(
                self.diaSeleccionadoInicio.day, 
                self.diaSeleccionadoInicio.month, 
                self.diaSeleccionadoInicio.year,0,0,0))

        self.calendarioInicio.showSelectedDate()

        self.calendarioFin.setSelectedDate(
            Qt.QDateTime(
                self.diaSeleccionadoFin.day, 
                self.diaSeleccionadoFin.month, 
                self.diaSeleccionadoFin.year,0,0,0))

        self.calendarioFin.showSelectedDate()
        #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

        self.mesLabel.setText(
            CommonUtils.textoCentrado(
            f"{CommonUtils.getMonthName(self.diaSeleccionadoInicio.month)} - {self.diaSeleccionadoInicio.year}"))

        self.labelInicio.setText(
            CommonUtils.textoCentrado(
            f"{CommonUtils.getMonthName(self.diaSeleccionadoFin.month)} - {self.diaSeleccionadoFin.year}"))
