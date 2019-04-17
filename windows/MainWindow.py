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
from SocratesUI.MainWindowMenu import Ui_MainWindow as Ui_MainWindowMenu
from windows import *
from windows import (DialogAcerca, DialogGestorPersonal, DialogPeriodos,
                     DialogPrimerInicio, DialogResAnual, DialogResMensual,
                     DialogResSemestral)
                     
class MainWindow(QtGui.QMainWindow, Ui_MainWindowMenu, object):

    def __init__(self, parent = None):
        QtGui.QMainWindow.__init__(self,parent) 
        self.setupUi(self)
        self.datosGuardados = ""

        #Comprobar que existan los archivos de guardado
        if (CommonUtils.existenArchivosDeGuardado()):
            self.datosGuardados = CommonUtils.getUserData()
        
        else:            
            CommonUtils.initializeStorage()
            
            # Lanzar la ventana de creacion de base de datos
            window = DialogPrimerInicio.DialogPrimerInicio(None)
            window.show()
            window.exec_()

        # --------------------------
        self.administrarPeriodos.clicked.connect(self.administrarPeriodosF)
        self.administrarPersonal.clicked.connect(self.administrarPersonalF)

        self.acerca.clicked.connect(self.acercaF)

        self.resAnual.clicked.connect(self.resAnualF)
        self.resMensual.clicked.connect(self.resMensualF)
        self.resSemestral.clicked.connect(self.resSemestralF)


    def acercaF(self):
        window = DialogAcerca.DialogAcerca(None)
        window.show()
        window.exec_()

    def administrarPeriodosF(self):
        window = DialogPeriodos.DialogPeriodos(None)
        window.show()
        window.exec_()
    
    def administrarPersonalF(self):
        window = DialogGestorPersonal.DialogGestorPersonal(None)
        window.show()
        window.exec_()

    def resMensualF(self):
        window = DialogResMensual.DialogResMensual(None)
        window.show()
        window.exec_()
    
    def resAnualF(self):
        window = DialogResAnual.DialogResAnual(None)
        window.show()
        window.exec_()
    
    def resSemestralF(self):
        window = DialogResSemestral.DialogResSemestral(None)
        window.show()
        window.exec_()
