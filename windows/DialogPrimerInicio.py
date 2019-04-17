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
from SocratesUI.DialogInfoPrimerInicio import \
    Ui_Dialog as Ui_DialogPrimerInicio
from windows import (DialogEditorTurnos, DialogGestorPersonal,
                     DialogPrimerInicio, DialogResSemestral, MainWindow)


class DialogPrimerInicio(QtGui.QDialog, Ui_DialogPrimerInicio, object):
    
    def __init__(self, parent = None):
        QtGui.QDialog.__init__(self,parent) 
        self.setupUi(self)

        self.continuarB.clicked.connect(self.continuarClick)
    
    def continuarClick(self):
        self.close()
        
        window = DialogGestorPersonal.DialogGestorPersonal(None)
        window.show()
        window.exec_()
