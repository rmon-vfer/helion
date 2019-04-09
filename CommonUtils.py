import pickle, sys, os, shutil
from arrow import *
import pickle
import holidays
from PyQt4 import QtCore, QtGui
from PyQt4 import *

class CommonUtils(QtGui.QMessageBox, QtGui.QCalendarWidget, object):
    
    BASE_PATH = os.getcwd()
    SAVES_DIR_PATH = os.path.join(BASE_PATH, "saves")
    SAVEFILE_PATH = os.path.join(SAVES_DIR_PATH, "savedData")
    CONFIGFILE_PATH    = os.path.join(SAVES_DIR_PATH, "config")
        
    @staticmethod
    def textoCentrado(texto):
        return f"""
        <html>
            <head/>
            <body>
                <p align="center"><span style=" font-weight:400;">{texto}</span>
                </p><
            /body>
        </html>
        """

    @staticmethod
    def showMessageBox(title, text, moreInfo = "", type = QtGui.QMessageBox.Information):
        msg = QtGui.QMessageBox()
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
        day, month, year = dateTuple[0].split("/")
        return Arrow(int(year), int(month), int(day))

    @staticmethod
    def getMonthName(monthNumber):
        return {
            1: "Enero", 2: "Febrero", 3: "Marzo", 4: "Abril", 5: "Mayo", 6: "Junio", 
            7: "Julio", 8: "Agosto", 9: "Septiembre", 10: "Octubre", 11: "Noviembre", 12: "Diciembre"
            }[monthNumber]

    @staticmethod
    def getWeekDayName(dayNumber):
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
        return os.path.exists(CommonUtils.SAVEFILE_PATH)
    
    @staticmethod
    def esFechaEspecial(date):
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
        with open(CommonUtils.CONFIGFILE_PATH, "rb") as configfile:
            configData = pickle.load(configfile)
        return configData

    @staticmethod
    def getUserData():
        with open(CommonUtils.SAVEFILE_PATH, "rb") as savefile:
            userData = pickle.load(savefile)
        return userData
    
    @staticmethod
    def updateUserData(newUserData):
        with open(CommonUtils.SAVEFILE_PATH, "wb") as savefile:
            pickle.dump(newUserData, savefile)
        
    @staticmethod
    def nuevoTrabajador(nombre, apellidos, turnos = []):
        return {
            "nombre": nombre,
            "apellidos": apellidos,
            "turnos": turnos,
            "horasTrabajadas" : []
        }

    @staticmethod
    def stringToArrow(dateString):
        dia, mes, anyo = dateString.split("/")
        return Arrow(int(anyo), int(mes), int(dia))
    
    @staticmethod
    def anadirDiaTrabajado(trabajador, date, tipo):
        trabajador["horasTrabajadas"].append(
            {
                "fecha": CommonUtils.arrowToString(date),
                "festivo" : CommonUtils.esDiaFestivo(date),
                "tipo" : tipo #A o B
            }
        )
        return trabajador

    @staticmethod
    def arrowToString(date):
        return f"{date.day}/{date.month}/{date.year}"

    @staticmethod
    def anadirPeriodo(inicio, final):
        data = CommonUtils.getUserData()
        data["periodos"].append(
            {"inicio" : CommonUtils.arrowToString(inicio), "final" : CommonUtils.arrowToString(final)})

        CommonUtils.updateUserData(data)

    @staticmethod
    def initializeStorage():
        template = {
            "trabajadores":[],
            "periodos": []
        }
        CommonUtils.updateUserData(template)
    
    @staticmethod
    def esFindeSemana(date):
        return date.weekday() == 5 or date.weekday() == 6

    @staticmethod
    def horasTrabajadasPorPeriodo(trabajador, periodo):
        horasTrabajadas = trabajador["horasTrabajadas"]
        totalHoras = 0

        for periodoTrabajado in horasTrabajadas:
            inicio = CommonUtils.stringToArrow(periodo["inicio"])
            fin = CommonUtils.stringToArrow(periodo["final"])

            fechaPeriodo = CommonUtils.stringToArrow(periodoTrabajado["fecha"])
            esFestivo = periodoTrabajado["festivo"]

            if (inicio < fechaPeriodo and fin > fechaPeriodo):
                if esFestivo or CommonUtils.esFindeSemana(fechaPeriodo):
                    totalHoras += 24
                
                else:
                    totalHoras += 17
        
        return totalHoras