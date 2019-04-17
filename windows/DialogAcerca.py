# Copyright Ramón Vila Ferreres
# ramonvilafer <at> gmail.com - 2019

import pickle, sys, os, shutil
import arrow
from PyQt4 import QtCore, QtGui
from PyQt4 import *

from SocratesUI.DialogAcerca import Ui_Dialog as Ui_DialogAcerca
from CommonUtils import CommonUtils
from windows import *


class DialogAcerca(QtGui.QDialog, Ui_DialogAcerca, object):
    
    def __init__(self, parent = None):
        QtGui.QDialog.__init__(self,parent) 
        self.setupUi(self)
