# -*- coding: utf-8 -*-
import modelo as m

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtWebKit import *

class Reportes:

    def __init__(self):
        self.Ingresos = m.Ingresos()
        self.Gastos = m.Gastos()

    def balance(self,ingreso,gasto):
        balance = ingreso - gasto
        return balance

    def reporteDiario(self,fechaDia):
        dataIngresos = self.Ingresos.consultaDia(fechaDia)
        dataGastos = self.Gastos.consultaDia(fechaDia)
        ingreso = self.Ingresos.totalDiario(fechaDia)
        gasto = self.Gastos.totalDiario(fechaDia)
        balance = self.balance(ingreso,gasto)
        return dataIngresos, dataGastos, ingreso, gasto, balance

    def reporteMensual(self,fechaMes):
        dataIngresos = self.Ingresos.consultaMensual(fechaMes)
        dataGastos = self.Gastos.consultaMensual(fechaMes)
        ingreso = self.Ingresos.totalMensual(fechaMes)
        gasto = self.Gastos.totalMensual(fechaMes)
        balance = self.balance(ingreso,gasto)
        return dataIngresos, dataGastos, ingreso, gasto, balance

    def reporteAnual(self,fechaAnual):
        dataIngresos = self.Ingresos.consultaAnual(fechaAnual)
        dataGastos = self.Gastos.consultaAnual(fechaAnual)
        ingreso = self.Ingresos.totalAnual(fechaAnual)
        gasto = self.Gastos.totalAnual(fechaAnual)
        balance = self.balance(ingreso,gasto)
        return dataIngresos, dataGastos, ingreso, gasto, balance

class Reportar:

    def __init__(self):
        self.app = QApplication(sys.argv)
        self.web = QWebView()

    def convertir(self,url,nombre):
        self.web.load(QUrl(url))

        printer = QPrinter()
        printer.setPageSize(QPrinter.A4)
        printer.setOutputFormat(QPrinter.PdfFormat)
        printer.setOutputFileName(nombre+".pdf")
 
        self.web.print_(printer)
        print "Pdf generated"
        QApplication.exit()
        QObject.connect(web, SIGNAL("loadFinished(bool)"), convertIt)
        sys.exit(self.app.exec_())

class HTML:

    def __init__(self):
        pass

    def generar():
        pass