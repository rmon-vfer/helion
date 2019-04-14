import os
import pickle
import shutil
import sys

import arrow
from PyQt4 import *
from PyQt4 import QtCore, QtGui

from CommonUtils import CommonUtils
from SocratesUI.DialogResumenSemestral import \
    Ui_Dialog as Ui_DialogResSemestral
from windows import *


class DialogResSemestral(QtGui.QDialog, Ui_DialogResSemestral, object):
    
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

            if(tipo == "Semestre"):
                periodos_validos.append(periodo)

        self.periodos_validos = periodos_validos
        self.periodosTable.setRowCount(len(periodos_validos))

        for periodo_index in range(len(periodos_validos)):
            periodo = periodos_validos[periodo_index]
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

    def mostrarTrabajadoresEnPeriodo(self):
        periodoSeleccionado = self.periodos_validos[self.periodosTable.currentRow()]
        inicio = CommonUtils.stringToArrow(periodoSeleccionado["inicio"])
        final = CommonUtils.stringToArrow(periodoSeleccionado["final"])

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
            
            print("Mostrando datos...")

            # Mostrar al empleado solo si ha realizado guardias en el periodo
            # seleccionado
            if horasTotales > 0 or (nombre.strip() == "" or apellidos.strip() == "" ):
                
                numTrabajadoresValidos += 1

                self.resultsTable.setRowCount(numTrabajadoresValidos)
                self.resultsTable.setItem(numTrabajadoresValidos -1, 0, QtGui.QTableWidgetItem(nombre))
                self.resultsTable.setItem(numTrabajadoresValidos -1, 1, QtGui.QTableWidgetItem(apellidos))
                self.resultsTable.setItem(numTrabajadoresValidos -1, 2, QtGui.QTableWidgetItem(str(horasLectivas)))
                self.resultsTable.setItem(numTrabajadoresValidos -1, 3, QtGui.QTableWidgetItem(str(horasEspeciales)))
                self.resultsTable.setItem(numTrabajadoresValidos -1, 4, QtGui.QTableWidgetItem(str(horasTotales)))
