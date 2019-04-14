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
        self.diaSeleccionadoInicio = arrow.now()
        self.selectInicio.calendarWidget().setFirstDayOfWeek(QtCore.Qt.Monday)
        self.selectInicio.calendarWidget().setLocale(QtCore.QLocale(QtCore.QLocale.Spanish))
        self.loadData()


    def closeWindow(self):
        self.close()

    def loadData(self):
        self.userData = CommonUtils.getUserData()
        #self.recargarTablaPeriodos()

    """
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
    """