# Copyright Ramón Vila Ferreres
# ramonvilafer <at> gmail.com - 2019

import os
import pickle
import shutil
import sys
import holidays
import arrow

from arrow import Arrow
from PyQt4 import *
from PyQt4 import QtCore, QtGui

class CommonUtils(QtGui.QMessageBox, QtGui.QCalendarWidget, object):
    """ Contiene métodos y atributos comunes a todas las clases del programa """

    BASE_PATH = os.getcwd()
    SAVES_DIR_PATH = os.path.join(BASE_PATH, "saves")
    SAVEFILE_PATH = os.path.join(SAVES_DIR_PATH, "savedData")
    CONFIGFILE_PATH = os.path.join(SAVES_DIR_PATH, "config")
        
    @staticmethod
    def textoCentrado(texto):
        """
        Devuelve el texto recibido envuelto en un HTML centrado
        :param texto: texto a centrar
        :return: texto centrado

        """
        return f"""
        <html>
            <head/>
            <body>
                <p align="center"><span style=" font-weight:400;">{texto}</span>
                </p>
            </body>
        </html>
        """

    @staticmethod
    def showMessageBox(title, text, moreInfo = "", type = QtGui.QMessageBox.Information):
        """
        Muestra un mensaje en una ventana de diálogo
        :param title: Título de la ventana
        :param text: Breve descripción (una o dos palabras) del contenido del mensaje
        :param moreInfo: Texto de mensaje propiamente dicho
        :param type: Tipo de mensaje, en función del tipo se mostrará un icon u otro, todos 
                     los tipos posibles están en QtGui.QMessageBox.<TIPO_AQUI>
        """

        msg = QtGui.QMessageBox()
        msg.setWindowIcon(QtGui.QIcon("./graphics/icon.ico"))
        
        msg.setIcon(type)
        msg.setText(text)

        if moreInfo != "":
            msg.setInformativeText(moreInfo)

        msg.setWindowTitle(title)
        msg.setStandardButtons(QtGui.QMessageBox.Ok | QtGui.QMessageBox.Cancel)
        respuesta = msg.exec_()
        return respuesta
        

    @staticmethod
    def dateTupleToArrow(dateTuple):
        return CommonUtils.stringToArrow(dateTuple[0])

    
    @staticmethod
    def formatForTable(string):
        longitud = len(string) + 10
        return "{:<18}".format(string)

    @staticmethod
    def siguienteMes(date):
        date = date.shift(months=1)
        return date.date()

    @staticmethod
    def siguienteSemestre(date):
        date = date.shift(months=6)
        return date.date()
    
    @staticmethod
    def siguienteAnyo(date):
        date = date.shift(years=1)
        return date.date()

    @staticmethod
    def getMonthName(monthNumber):
        """ Obtiene el nombre de un mes a partir de su número """
        return {
            1: "Enero", 
            2: "Febrero", 
            3: "Marzo", 
            4: "Abril", 
            5: "Mayo", 
            6: "Junio", 
            7: "Julio", 
            8: "Agosto", 
            9: "Septiembre", 
            10: "Octubre", 
            11: "Noviembre", 
            12: "Diciembre"}[monthNumber]

    @staticmethod
    def getWeekDayName(dayNumber):
        """ Obtiene el nombre de un día de la semana a partir de su número """
        return {
            0 : "lunes",
            1 : "martes",
            2 : "miércoles",
            3 : "jueves",
            4 : "viernes",
            5 : "sábado",
            6 : "domingo"
        }[dayNumber]
    
    @staticmethod
    def existenArchivosDeGuardado():
        """
        Comprueba si existen los archivos de guardado en el directorio del programa
        """
        return os.path.exists(CommonUtils.SAVEFILE_PATH)
    
    @staticmethod
    def esFechaEspecial(date):
        """
        Recibe una fecha (Arrow) y comprueba si es especial
        Se consideran especiales las siguientes fechas:
            * Fiestas regionales
            * Festivos nacionales
            * Otros festivos
            * Sábados y domingos
        """
        vacaciones = holidays.Spain()
        date = date.strftime("%m-%d-%Y")
        mes, dia, anyo = date.split("-")

        if date in vacaciones:
            return f"Sí ({vacaciones.get(date)})"

        elif CommonUtils.esFindeSemana(Arrow(int(anyo), int(mes), int(dia))):
            return f"Sí (Fin de semana)"  

        else:
            return "No"

    @staticmethod
    def getConfigData():
        """
        Obtiene los datos de configuración como un JSON
        """

        with open(CommonUtils.CONFIGFILE_PATH, "rb") as configfile:
            configData = pickle.load(configfile)
        return configData

    @staticmethod
    def getUserData():
        """
        Obtiene los datos de todos los usuarios como JSON
        """

        with open(CommonUtils.SAVEFILE_PATH, "rb") as savefile:
            userData = pickle.load(savefile)
        return userData
    
    @staticmethod
    def updateUserData(newUserData):
        """
        Reescribe los datos de usuario
        """
        #TODO: Evitar que pueda borrarlo todo!
        with open(CommonUtils.SAVEFILE_PATH, "wb") as savefile:
            pickle.dump(newUserData, savefile)
        
    @staticmethod
    def nuevoTrabajador(nombre, apellidos, turnos = []):
        """
        Devuelve un Dict con los datos de un nuevo trabajador
        """
        #TODO: Documentar parametros
        return {
            "nombre": nombre,
            "apellidos": apellidos,
            "turnos": turnos,
            "horasTrabajadas" : []
        }

    @staticmethod
    def stringToArrow(dateString):
        """
        Convierte una cadena de fecha (dia/mes/año) a un objeto Arrow
        """
        if (type(dateString) == Arrow): 
            return dateString
        else:
            dia, mes, anyo = dateString.split("/")
            return Arrow(int(anyo), int(mes), int(dia))
    
    @staticmethod
    def anadirDiaTrabajado(trabajador, date, tipo):
        trabajador["horasTrabajadas"].append(
            {
                "fecha": CommonUtils.arrowToString(date),
                "festivo" : CommonUtils.esDiaFestivo(date),
                "tipo" : tipo 
            }
        )
        return trabajador

    @staticmethod
    def arrowToString(date):

        """Convierte un objeto Arrow a cadena de fecha (dia/mes/año)"""
        return f"{date.day}/{date.month}/{date.year}"

    @staticmethod
    def initializeStorage():
        if not os.path.exists("./saves"):
            os.makedirs("./saves")

        """Prepara el almacenamiento para poder guardar los datos de los usuarios"""
        template = {
            "trabajadores":[],
            "periodos": []
        }
        CommonUtils.updateUserData(template)
    
    @staticmethod
    def esFindeSemana(date):
        """ Comprueba si una fecha determinada es sábado o domingo """
        return date.weekday() == 5 or date.weekday() == 6
    
    @staticmethod
    def qdateToArrow(qdate):
        return Arrow(int(qdate.year()), int(qdate.month()), int(qdate.day()))

    @staticmethod
    def arrowToQdate(arrowDate):
        return QtCore.QDate.fromString(arrowDate.format("YYYY-M-D"), "yyyy-MM-d")

    @staticmethod
    def calcularFinal(inicio, tipo):
        duracion = {"Mes":1, "Semestre": 6, "Año":12}[tipo]

        fin = CommonUtils.stringToArrow(inicio)
        if duracion <= 6:
            fin = fin.shift(months = duracion)
        else:
            fin = fin.shift(years = 1)

        return fin 
