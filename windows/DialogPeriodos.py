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
        self.loadData()

        self.haGuardado = True 

        self.diaSeleccionadoInicio = arrow.now()
        self.selectInicio.calendarWidget().setFirstDayOfWeek(QtCore.Qt.Monday)
        self.selectInicio.calendarWidget().setLocale(QtCore.QLocale(QtCore.QLocale.Spanish))
        self.calendarioDia.setSelectedDate(CommonUtils.arrowToQdate(self.diaSeleccionadoInicio))
        self.calendarioDia.showSelectedDate()

        self.botonAnadir.clicked.connect(self.anadirPeriodo)

    def closeWindow(self):
        self.close()

    def loadData(self):
        self.userData = CommonUtils.getUserData()
        self.recargarTablaPeriodos()

    def anadirPeriodo(self):
        tipo = self.comboTipoPeriodo.currentText()
        fechaInicio = self.selectInicio.date()

        if tipo == "Mes":
            fechaInicio = CommonUtils.siguienteMes(fechaInicio)
        
        elif tipo == "Semestre":
            fechaInicio = CommonUtils.siguienteSemestre(fechaInicio)
        
        else:
            fechaInicio = CommonUtils.siguienteAnyo(fechaInicio)
        
        self.periodos.append({"
            "inicio" : f"{CommonUtils.arrowToString(CommonUtils.qdateToArrow(fechaInicio))}",
            "tipo"   : f"{tipo}"
        "})

        CommonUtils.updateUserData(self.userData)

    def recargarTablaPeriodos(self):
        self.userData = CommonUtils.getUserData()
        self.periodos = self.userData["periodos"]

        self.periodosTable.setRowCount(len(self.periodos))
        
        for periodo_index in range(len(self.periodos)):
            periodo = self.periodos[periodo_index]
            
            inicio = periodo["inicio"]
            tipo = periodo["tipo"]
            duracion = {"Mes":1, "Semestre": 6, "Año":12}[tipo]
            fin = CommonUtils.arrowToString(CommonUtils.qdateToArrow(
                CommonUtils.arrowToQdate(
                CommonUtils.stringToArrow(inicio)).addMonths(duracion)))
            
            # Establecer el inicio y final
            self.periodosTable.setItem(periodo_index, 0, QtGui.QTableWidgetItem(inicio))
            self.periodosTable.setItem(periodo_index, 1, QtGui.QTableWidgetItem(fin))
            self.periodosTable.setItem(periodo_index, 2, QtGui.QTableWidgetItem(tipo))
        
        self.periodosTable.resizeColumnsToContents()
    
    def eliminarPeriodo(self):
        rowIndex = self.periodosTable.currentRow()
        self.periodosTable.removeRow(rowIndex)
        del self.userData["periodos"][rowIndex]

        CommonUtils.updateUserData(self.userData)
