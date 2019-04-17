import os
import pickle
import shutil
import sys

import arrow
from PyQt4 import *
from PyQt4 import QtCore, QtGui

from CommonUtils import CommonUtils
from SocratesUI.DialogGestorPersonal import \
    Ui_Dialog as Ui_DialogGestorPersonal
from windows import (DialogEditorTurnos, DialogGestorPersonal,
                     DialogPrimerInicio, DialogResSemestral, MainWindow)
# TODO:
# - Actualizar las guardias de la tabla cada vez que se selecciona
#   un mes diferente en el calendario

class DialogGestorPersonal(QtGui.QDialog, Ui_DialogGestorPersonal, object):
    #TODO: Implementar edicion de datos directamente en la tabla de personal

    def __init__(self, parent = None):
        QtGui.QDialog.__init__(self,parent) 
        self.setupUi(self)

        self.userData = ""
        self.loadData()
        self.ULTIMOS_TURNOS_EDITADOS = []
        
        self.haGuardado = True

        self.addAPlantilla.clicked.connect(self.anadirTrabajador)
        self.tablaPersonal.itemClicked.connect(self.recargarTablaTurnos)
        self.configTurnosNuevo.clicked.connect(self.anadirTurnos)
        self.aplicarButton.clicked.connect(self.aplicarCambios)
        self.aceptarButton.clicked.connect(self.closeWindow)
        self.eliminarButton.clicked.connect(self.eliminarTrabajador)

    def closeWindow(self):
        if self.haGuardado == False:
            respuesta = CommonUtils.showMessageBox("Alerta", "Guardado", "Has realizado cambios pero no los has guardado, ¿Quieres guardarlos?", QtGui.QMessageBox.Warning)
            
            if respuesta == QtGui.QMessageBox.Ok:
                self.aplicarCambios()
            elif respuesta == QtGui.QMessageBox.Cancel:
                self.close()
                
        # Si no, cerrar la ventana   
        else:
            self.close()
        

    def loadData(self):
        self.userData = CommonUtils.getUserData()
        self.recargarTablaTrabajadores()
    
    def anadirTurnos(self):
        nombre = self.nombreNuevo.text()
        apellidos = self.apellidosNuevo.text()
        filaSeleccionada = self.tablaPersonal.currentRow()
        
        # Si hay texto, el usuario quiere añadir todos los datos a la vez
        if str(nombre).strip() != "" and str(apellidos).strip() != "":
            self.anadirTrabajador()
            totalFilas = self.tablaPersonal.rowCount()
            filaSeleccionada = self.tablaPersonal.rowCount() -1

        window = DialogEditorTurnos.DialogEditorTurnos(int(filaSeleccionada), None)
        window.show()
        window.exec_()
        self.loadData()
        self.recargarTablaTurnos()

        self.haGuardado = False

    def recargarTablaTrabajadores(self):
        self.trabajadores = self.userData["trabajadores"]
        self.tablaPersonal.setRowCount(len(self.trabajadores))
        
        for trabajador_index in range(len(self.trabajadores)):
            trabajador = self.trabajadores[trabajador_index]

            # Establecer el Nombre y apellido
            self.tablaPersonal.setItem(trabajador_index, 0, QtGui.QTableWidgetItem(CommonUtils.formatForTable(trabajador["nombre"])))
            self.tablaPersonal.setItem(trabajador_index, 1, QtGui.QTableWidgetItem(CommonUtils.formatForTable(trabajador["apellidos"])))
        
        self.tablaPersonal.resizeColumnsToContents()

    def recargarTablaTurnos(self):
        # Edición del nombre y los apellidos del empleado

        filaSeleccionada = self.tablaPersonal.currentRow()
        self.trabajadorSeleccionado = self.trabajadores[filaSeleccionada]
        turnosSeleccionados = self.trabajadorSeleccionado["turnos"]
        self.turnosSeleccionada.setRowCount(len(turnosSeleccionados))

        for turno_index in range(len(turnosSeleccionados)):
            turnoActual = turnosSeleccionados[turno_index]

            # Establecer el Nombre y apellido
            self.turnosSeleccionada.setItem(turno_index, 0, QtGui.QTableWidgetItem(CommonUtils.formatForTable(turnoActual[0])))
            self.turnosSeleccionada.setItem(turno_index, 1, QtGui.QTableWidgetItem(CommonUtils.formatForTable(turnoActual[1])))
            self.turnosSeleccionada.setItem(turno_index, 2, QtGui.QTableWidgetItem(
                CommonUtils.formatForTable(CommonUtils.esFechaEspecial(CommonUtils.stringToArrow(turnoActual[0]))
            )))

        self.turnosSeleccionada.resizeColumnsToContents()

    def anadirTrabajador(self):
        nombre = self.nombreNuevo.text()
        apellidos = self.apellidosNuevo.text()
        
        # Controlar nombres y apellidos vacios
        #TODO: Cambiar por un regex
        if str(nombre).strip() == "":
            CommonUtils.showMessageBox(
                "Error", "Campo vacio", "Compruebe que haya escrito correctamente el nombre y los apellidos",
                QtGui.QMessageBox.Warning)
        else:

            # Guardar al nuevo empleado en la BD
            self.userData["trabajadores"].append(CommonUtils.nuevoTrabajador(nombre, apellidos))
            CommonUtils.updateUserData(self.userData)
            self.recargarTablaTrabajadores()

            # Borrar el contenido de las cajas de texto
            self.nombreNuevo.setText("")
            self.apellidosNuevo.setText("")
            self.turnosSeleccionada.setRowCount(0)

        self.haGuardado = False
    
    def eliminarTrabajador(self):
        self.turnosSeleccionada.setRowCount(0)
        rowIndex = self.tablaPersonal.currentRow()
        self.tablaPersonal.removeRow(rowIndex)
        del self.userData["trabajadores"][rowIndex]

        self.haGuardado = False
    
    def aplicarCambios(self):
        CommonUtils.showMessageBox("Guardado", "Correcto", "Los datos se han actualizado correctamente")
        CommonUtils.updateUserData(self.userData)
        self.haGuardado = True
