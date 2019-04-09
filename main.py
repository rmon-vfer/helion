import pickle, sys, os, shutil
import arrow
from PyQt4 import QtCore, QtGui
from PyQt4 import *

from CommonUtils import CommonUtils
from windows import DialogEditorTurnos, DialogGestorPersonal, DialogPrimerInicio, DialogResSemestral, MainWindow 

def main():
    app = QtGui.QApplication(sys.argv)
    window = MainWindow.MainWindow(None)
    window.show()
    app.exec_()

main()
    