# Copyright Ramón Vila Ferreres
# ramonvilafer <at> gmail.com - 2019

import os
import pickle
import shutil
import sys

import arrow
from PyQt4 import *
from PyQt4 import QtCore, QtGui

from CommonUtils import CommonUtils
from SocratesUI.DialogResumenAnual import Ui_Dialog as Ui_DialogResAnual
from windows import *


class DialogResAnual(QtGui.QDialog, Ui_DialogResAnual, object):
    
    def __init__(self, parent = None):
        QtGui.QDialog.__init__(self,parent) 
        self.setupUi(self)
        self.userData = ""
        self.periodos = []
        self.periodos_validos = []
        self.ahora = arrow.now()
        
        self.loadData()
        self.periodosTable.clicked.connect(self.mostrarTrabajadoresEnPeriodo)

    def loadData(self):
        self.userData = CommonUtils.getUserData()
        self.recargarTablaPeriodos()
    
    def recargarTablaPeriodos(self):
        self.userData = CommonUtils.getUserData()
        self.periodos = self.userData["periodos"]
        periodos_validos = []
        
        for periodo_index in range(len(self.periodos)):
            periodo = self.periodos[periodo_index]
            inicio = periodo["inicio"]
            tipo = periodo["tipo"]

            if(tipo == "Año"):
                periodos_validos.append(periodo)


        self.periodos_validos = periodos_validos
        self.periodosTable.setRowCount(len(periodos_validos))

        for periodo_index in range(len(periodos_validos)):
            periodo = periodos_validos[periodo_index]
                        
            inicio = periodo["inicio"]
            tipo = periodo["tipo"]
            fin = CommonUtils.arrowToString(CommonUtils.calcularFinal(inicio, tipo))
                
            # Establecer el inicio y final
            self.periodosTable.setItem(periodo_index, 0, QtGui.QTableWidgetItem(CommonUtils.formatForTable(inicio)))
            self.periodosTable.setItem(periodo_index, 1, QtGui.QTableWidgetItem(CommonUtils.formatForTable(fin)))
            self.periodosTable.setItem(periodo_index, 2, QtGui.QTableWidgetItem(CommonUtils.formatForTable(tipo)))
        
        self.periodosTable.resizeColumnsToContents()

    def mostrarTrabajadoresEnPeriodo(self):
        periodoSeleccionado = self.periodos_validos[self.periodosTable.currentRow()]
        inicio = CommonUtils.stringToArrow(periodoSeleccionado["inicio"])
        tipo = periodoSeleccionado["tipo"]
        final = CommonUtils.arrowToString(CommonUtils.calcularFinal(inicio, tipo))

        numTrabajadoresValidos = 0

        trabajadores = self.userData["trabajadores"]

        for trabajador_index in range(len(trabajadores)):
            trabajador = trabajadores[trabajador_index]
            nombre = trabajador["nombre"]
            apellidos = trabajador["apellidos"]
            horasLectivas = 0
            horasEspeciales = 0

            guardiasEnPeriodo = []

            # Recorrer todas las guardias guardadas
            for guardia in trabajador["turnos"]:

                fechaGuardia = CommonUtils.stringToArrow(guardia[0])
                final = CommonUtils.stringToArrow(final)
                tipoGuardia = guardia[1]

                # Si la guardia está en el periodo seleccionado, entonces
                # añadirla a la lista de guardias válidas

                if fechaGuardia >= inicio and fechaGuardia <= final:
                    print("La guardia esta en el periodo selecionado")
                    guardiasEnPeriodo.append(guardia)

                    if CommonUtils.esFechaEspecial(fechaGuardia) != "No":
                        horasEspeciales += 24
                    else:
                        horasLectivas += 17

            horasTotales = horasLectivas + horasEspeciales
            
            # Mostrar al empleado solo si ha realizado guardias en el periodo
            # seleccionado
            if horasTotales > 0 or nombre.strip() == "":
                
                numTrabajadoresValidos += 1

                self.resultsTable.setRowCount(numTrabajadoresValidos)
                self.resultsTable.setItem(numTrabajadoresValidos -1, 0, QtGui.QTableWidgetItem(CommonUtils.formatForTable(nombre)))
                self.resultsTable.setItem(numTrabajadoresValidos -1, 1, QtGui.QTableWidgetItem(CommonUtils.formatForTable(apellidos)))
                self.resultsTable.setItem(numTrabajadoresValidos -1, 2, QtGui.QTableWidgetItem(CommonUtils.formatForTable(str(horasLectivas))))
                self.resultsTable.setItem(numTrabajadoresValidos -1, 3, QtGui.QTableWidgetItem(CommonUtils.formatForTable(str(horasEspeciales))))
                self.resultsTable.setItem(numTrabajadoresValidos -1, 4, QtGui.QTableWidgetItem(CommonUtils.formatForTable(str(horasTotales))))
