# Copyright Ramón Vila Ferreres
# ramonvilafer <at> gmail.com - 2019

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
        self.calendarioDia = self.selectInicio.calendarWidget()
        
        self.calendarioDia.setFirstDayOfWeek(QtCore.Qt.Monday)
        self.calendarioDia.setLocale(QtCore.QLocale(QtCore.QLocale.Spanish))
        self.calendarioDia.setSelectedDate(CommonUtils.arrowToQdate(self.diaSeleccionadoInicio))
        self.calendarioDia.showSelectedDate()

        self.botonAnadir.clicked.connect(self.anadirPeriodo)
        self.botonEliminar.clicked.connect(self.eliminarPeriodo)

    def closeWindow(self):
        self.close()

    def loadData(self):
        self.userData = CommonUtils.getUserData()
        self.recargarTablaPeriodos()

    def anadirPeriodo(self):
        tipo = self.comboTipoPeriodo.currentText()
        fechaInicio = self.selectInicio.date()
        fechaInicio = CommonUtils.qdateToArrow(fechaInicio)

        if tipo == "Mes":
            fechaInicio = CommonUtils.siguienteMes(fechaInicio)
        
        elif tipo == "Semestre":
            fechaInicio = CommonUtils.siguienteSemestre(fechaInicio)
        
        else:
            fechaInicio = CommonUtils.siguienteAnyo(fechaInicio)
        
        self.periodos.append({
            "inicio" : f"{CommonUtils.arrowToString(fechaInicio)}",
            "tipo"   : f"{tipo}"
        })

        CommonUtils.updateUserData(self.userData)
        self.recargarTablaPeriodos()

    def recargarTablaPeriodos(self):
        self.userData = CommonUtils.getUserData()
        self.periodos = self.userData["periodos"]

        self.tablaPeriodos.setRowCount(len(self.periodos))
        
        for periodo_index in range(len(self.periodos)):
            periodo = self.periodos[periodo_index]
            
            inicio = periodo["inicio"]
            tipo = periodo["tipo"]
            fin = CommonUtils.arrowToString(CommonUtils.calcularFinal(inicio, tipo))
            
            # Establecer el inicio y final
            self.tablaPeriodos.setItem(periodo_index, 0, QtGui.QTableWidgetItem(CommonUtils.formatForTable(inicio)))
            self.tablaPeriodos.setItem(periodo_index, 1, QtGui.QTableWidgetItem(CommonUtils.formatForTable(fin)))
            self.tablaPeriodos.setItem(periodo_index, 2, QtGui.QTableWidgetItem(CommonUtils.formatForTable(tipo)))
        
        self.tablaPeriodos.resizeColumnsToContents()
    
    def eliminarPeriodo(self):
        rowIndex = self.tablaPeriodos.currentRow()
        self.tablaPeriodos.removeRow(rowIndex)
        del self.userData["periodos"][rowIndex]

        CommonUtils.updateUserData(self.userData)
        self.recargarTablaPeriodos()

        self.haGuardado = False
