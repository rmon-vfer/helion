import pickle, sys, os, shutil
import arrow
from PyQt4 import QtCore, QtGui
from PyQt4 import *


from SocratesUI.DialogInfoPrimerInicio import Ui_Dialog as Ui_DialogPrimerInicio
from CommonUtils import CommonUtils
from windows import DialogEditorTurnos, DialogGestorPersonal, DialogPrimerInicio, DialogResSemestral, MainWindow 


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
    