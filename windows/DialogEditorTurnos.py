import pickle, sys, os, shutil
from arrow import *
from PyQt4 import QtCore, QtGui
from PyQt4 import *
import pprint

from SocratesUI.DialogEditorTurnosPorEmpleado import Ui_Dialog as Ui_DialogEditorTurnos
from CommonUtils import CommonUtils
from windows import DialogEditorTurnos, DialogGestorPersonal, DialogPrimerInicio, DialogResSemestral, MainWindow 


class DialogEditorTurnos(QtGui.QDialog, Ui_DialogEditorTurnos, object):
   
    def __init__(self, selectedIndex, parent = None):
        # TODO: incluir un boton para volver al dia actual

        QtGui.QDialog.__init__(self,parent) 
        self.setupUi(self)
        self.userData = ""

        self.index = selectedIndex

        self.loadData()
        self.haGuardado = True

        self.trabajadorSeleccionado = self.userData["trabajadores"][self.index]

        # Por defecto se carga la fecha actual
        self.diaSeleccionado = Arrow.now()

        self.labelNombre.setText(self.trabajadorSeleccionado["nombre"])
        self.labelApellidos.setText(self.trabajadorSeleccionado["apellidos"])

        self.refrescarTodo()

        self.calendarioDia.clicked.connect(self.refrescarTodo)
        self.siguienteButton.clicked.connect(self.mesSiguiente)
        self.anteriorButton.clicked.connect(self.mesAnterior)
        self.addButton.clicked.connect(self.anadirTurno)
        self.botonOk.clicked.connect(self.closeWindow)
        self.botonAplicar.clicked.connect(self.aplicarCambios)
    
    def closeWindow(self):
        if self.haGuardado == False:
            respuesta = CommonUtils.showMessageBox("Alerta", "Guardado", "Has realizado cambios pero no los has guardado, ¿Quieres guardarlos?", QtGui.QMessageBox.Warning)
            
            if respuesta == QtGui.QMessageBox.Ok:
                self.aplicarCambios()
            elif respuesta == QtGui.QMessageBox.Cancel:
                self.close()
        else:
            self.close()
    
    def aplicarCambios(self):
        CommonUtils.showMessageBox("Guardado", "Correcto", "Los datos se han actualizado correctamente")
        CommonUtils.updateUserData(self.userData)
        self.haGuardado = True

    def loadData(self):
        self.userData = CommonUtils.getUserData()

    def mesSiguiente(self):
        self.calendarioDia.showNextMonth()
        self.refrescarTodo()

    def mesAnterior(self):
        self.calendarioDia.showPreviousMonth()
        self.refrescarTodo()

    def anadirTurno(self):
        fecha = self.fechaMarcadaEnCalendario()
        tipoTurno = self.comboTurno.currentText()
        self.nuevoTurnoATrabajador(fecha, tipoTurno)
        self.refrescarTodo()
        self.haGuardado = False

    def eliminarTurno(self):
        rowIndex = self.tableWidget.currentRow()
        self.tableWidget.removeRow(rowIndex)
        del self.trabajadorSeleccionado["turnos"][rowIndex]
        CommonUtils.updateUserData(self.userData)
        self.haGuardado = False

    def nuevoTurnoATrabajador(self, date, tipo):
        turno = (f"{date.day}/{date.month}/{date.year}", tipo)
        self.trabajadorSeleccionado["turnos"].append(turno)
        CommonUtils.updateUserData(self.userData)
        self.haGuardado = False
    
    def cargarTablaTurnos(self):
        trabajadorSeleccionado = self.trabajadorSeleccionado
        turnosSeleccionados = trabajadorSeleccionado["turnos"]

        pprint.pprint(turnosSeleccionados, indent=4)

        totalTurnosValidos = 0
        turnosValidos = []

        for turno in turnosSeleccionados:
            # Si el mes actual y el del turno coinciden
            if (self.diaSeleccionado.month == CommonUtils.dateTupleToArrow(turno).month):
                totalTurnosValidos += 1
                turnosValidos.append(turno)

        self.tableWidget.setRowCount(totalTurnosValidos) #? Debería cambiar el nombre xd "tableWidget"
 
        for numeroDeTurno in range(len(turnosValidos)):
            turnoActual = turnosValidos[numeroDeTurno]
            arrowDiaActual = CommonUtils.dateTupleToArrow(turnoActual)

            # Establecer el Nombre y apellido
            self.tableWidget.setItem(numeroDeTurno, 0, QtGui.QTableWidgetItem(
                f"{CommonUtils.getWeekDayName(arrowDiaActual.weekday())} {arrowDiaActual.day}"
                ))

            self.tableWidget.setItem(numeroDeTurno, 1, QtGui.QTableWidgetItem(turnoActual[1]))
            self.tableWidget.setItem(numeroDeTurno, 2, QtGui.QTableWidgetItem(
                CommonUtils.esFechaEspecial(arrowDiaActual)))

            # Ajustar el tamaño de las columnas para que quepa todo el texto
            self.tableWidget.resizeColumnsToContents()
    
    def fechaMostradaEnCalendario(self):
        dia = 1
        mes = self.calendarioDia.monthShown()
        anyo = self.calendarioDia.yearShown()
        return Arrow(anyo, mes, dia)

    def fechaMarcadaEnCalendario(self):
        mes = self.calendarioDia.selectedDate().month()
        dia = self.calendarioDia.selectedDate().day()
        anyo = self.calendarioDia.selectedDate().year()
        return Arrow(anyo, mes, dia)

    def refrescarTodo(self):
        self.diaSeleccionado = self.fechaMostradaEnCalendario()
        self.mesLabel.setText(CommonUtils.textoCentrado(f"{CommonUtils.getMonthName(self.diaSeleccionado.month)} - {self.diaSeleccionado.year}"))
        self.cargarTablaTurnos()

