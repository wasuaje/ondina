# -*- coding: utf-8 -*-
import os
import time
import json
import datetime
from bson import BSON
from bson import json_util
from pymongo import MongoClient
from time import gmtime, strftime


###############################################################################
"""Declaracion de variables"""
#Direccion de la carpeta raiz del programa
path = os.path.dirname(__file__)

#Variables del sistema
fecha = datetime.datetime.utcnow()

#Declaracion de la base de datos y las colecciones
MONGODB_URI = 'mongodb://jf-taberu:jfbasc1989@ds027318.mongolab.com:27318/taberu'
client = MongoClient(MONGODB_URI)

"""
    #A partir de aca se debe colocar la interaccion de la base de datos
"""

db = client['taberu']
usuarios = db['usuarios']
ingresos = db['ingresos']
gastos = db['gastos']
ahorros = db['ahorros']
impuestos = db['impuestos']


class Ingresos:

    def __init__(self):
        pass

    def guardar(self, datos):
        ingreso = db.ingresos
        dato = {'Fecha' : fecha,
                'Razon' : datos[0],
                'Monto' : float(datos[1]),
                'Tipo' : datos[2],
                }
        ingreso.insert(dato)

    def guardarT(self, datos):
        ingreso = db.ingresos
        dato = {'Fecha' : fecha,
                'Razon' : datos[0],
                'Monto' : float(datos[1]),
                'Tipo' : datos[5],
                }
        ingreso.insert(dato)

        impuesto = db.impuestos
        datoim = {'Fecha' : fecha,
                  'Razon' : datos[0],
                  'Factura' : int(datos[2]),
                  'Sub-Total': float(datos[1]),
                  'IVA' : datos[3],
                  'Total' : datos[4]
                  }
        impuestos.insert(datoim)

    def consultarTodo(self):
        return db.ingresos.find()

    def consultaDia(self,(anio,mes,dia)):
        return db.ingresos.find({'Fecha':(anio,mes,dia)})

    def consultaMensual(self,(anio,mes)):
        return db.ingresos.find({'Fecha':(anio,mes)})

    def consultaAnual(self,fechaAnual):
        return db.ingresos.find({'Fecha':fechaAnual})

    def totalDiario(self,(anio,mes,dia)):
        valor = 0
        ii = db.ingresos.find({'Fecha':(anio,mes,dia)})
        for i in ii:
            valor = valor + i['Monto']
        return valor
        
    def totalMensual(self,(anio,mes)):
        valor = 0
        ii = db.ingresos.find({'Fecha':(anio,mes)})
        for i in ii:
            valor = valor + i['Monto']
        return valor

    def totalAnual(self,fechaAnual):
        valor = 0
        ii = db.ingresos.find({'Fecha':fechaAnual})
        for i in ii:
            valor = valor + i['Monto']
        return valor
    
    def totalIngresado(self):
        valor = 0
        ii = db.ingresos.find()
        for i in ii:
            valor = valor + i['Monto']
        return valor

    def totalRegistros(self):
        return db.ingresos.find().count()

class Gastos:

    def __init__(self):
        pass

    def guardar(self, datos):
        gasto = db.gastos
        dato = {'Fecha' : fecha,
                'Razon' : datos[0],
                'Monto' : float(datos[1]),
                'Tipo' : datos[2],
               }
        gasto.insert(dato)

    def consultarTodo(self):
        return db.gastos.find()

    def consultaDia(self,(anio,mes,dia)):
        return db.gastos.find({'Fecha':(anio,mes,dia)})

    def consultaMensual(self,(anio,mes)):
        return db.gastos.find({'Fecha':(anio,mes)})

    def consultaAnual(self,fechaAnual):
        return db.gastos.find({'Fecha':fechaAnual})

    def totalDiario(self,(anio,mes,dia)):
        valor = 0
        gg = db.gastos.find({'Fecha':(anio,mes,dia)})
        for g in gg:
            valor = valor + g['Monto']
        return valor

    def totalMensual(self,(anio,mes)):
        valor = 0
        gg = db.gastos.find({'Fecha':(anio,mes)})
        for g in gg:
            valor = valor + g['Monto']
        return valor

    def totalAnual(self,fechaAnual):
        valor = 0
        gg = db.gastos.find({'Fecha':fechaAnual})
        for g in gg:
            valor = valor + g['Monto']
        return valor        

    def totalGastado(self):
        valor = 0
        gg = db.gastos.find()
        for g in gg:
            valor = valor + g['Monto']
        return valor

    def totalRegistros(self):
        return db.gastos.find().count()


class Ahorros:

    def __init__(self):
        pass

    def guardar(self, datos):
        ahorros = db.ahorros
        dato = {'Fecha' : fecha,
                'Porcentaje' : datos[0],
                'Total_Ahorrado': datos[1],
                }
        ahorros.insert(dato)

    def consultarTodo(self):
        return db.ahorros.find()

    def consultaDia(self,(anio,mes,dia)):
        return db.ahorros.find({'Fecha':(anio,mes,dia)})

    def consultaMensual(self,(anio,mes)):
        return db.ahorros.find({'Fecha':(anio,mes)})

    def consultaAnual(self,fechaAnual):
        return db.ahorros.find({'Fecha':fechaAnual})

    def totalDiario(self,(anio,mes,dia)):
        valor = 0
        ii = db.ahorros.find({'Fecha':(anio,mes,dia)})
        for i in ii:
            valor = valor + i['Total_Ahorrado']
        return valor
        
    def totalMensual(self,(anio,mes)):
        valor = 0
        ii = db.ahorros.find({'Fecha':(anio,mes)})
        for i in ii:
            valor = valor + i['Total_Ahorrado']
        return valor

    def totalAnual(self,fechaAnual):
        valor = 0
        ii = db.ahorros.find({'Fecha':fechaAnual})
        for i in ii:
            valor = valor + i['Total_Ahorrado']
        return valor
    
    def totalAhorrado(self):
        valor = 0
        ii = db.ahorros.find()
        for i in ii:
            valor = valor + i['Total_Ahorrado']
        return valor

    def totalRegistros(self):
        return db.ahorros.find().count()


class Impuestos:

    def __init__(self):
        pass

    def consultarTodo(self):
        return db.impuestos.find()

    def consultaDia(self,(anio,mes,dia)):
        return db.impuestos.find({'Fecha':(anio,mes,dia)})

    def consultaMensual(self,(anio,mes)):
        return db.impuestos.find({'Fecha':(anio,mes)})

    def consultaAnual(self,fechaAnual):
        return db.impuestos.find({'Fecha':fechaAnual})

    def totalDiario(self,(anio,mes,dia)):
        valor = 0
        ii = db.impuestos.find({'Fecha':(anio,mes,dia)})
        for i in ii:
            valor = valor + i['IVA']
        return valor
        
    def totalMensual(self,(anio,mes)):
        valor = 0
        ii = db.impuestos.find({'Fecha':(anio,mes)})
        for i in ii:
            valor = valor + i['IVA']
        return valor

    def totalAnual(self,fechaAnual):
        valor = 0
        ii = db.impuestos.find({'Fecha':fechaAnual})
        for i in ii:
            valor = valor + i['IVA']
        return valor
    
    def totalImpuestos(self):
        valor = 0
        im = db.impuestos.find()
        for i in im:
            valor = valor + i['IVA']
        return valor

    def totalRegistros(self):
        return db.impuestos.find().count()


class Balance:
    
    def __init__(self):
        self.ingres = Ingresos()
        self.gast = Gastos()
        self.aho = Ahorros()
        self.imp = Impuestos()

    def total(self):
        ingre = 0
        gas = 0
        aho = 0
        imp = 0

        ingre = self.ingres.totalIngresado()
        gas = self.gast.totalGastado()
        aho = self.aho.totalAhorrado()
        imp = self.imp.totalImpuestos()

        balance = 0

        if ingre > 0:
            if gas > 0:
                balance = ingre - gas
        return balance, aho, imp
    
    def tipoIngreso(self):
        jtis = []
        tit = db.tipoIngreso.find()
        for ti in tit:
            jti = json.dumps(ti['tipo'], default=json_util.default)
            jtis.append(jti)
        return jtis
    
    def tipoGasto(self):
        jtgs = []
        tgt = db.tipoGasto.find()
        for tg in tgt:
            jtg = json.dumps(tg['tipo'], default=json_util.default)
            jtgs.append(jtg)
        return jtgs


class Reportes:
    
    def __init__(self):
        self.ingres = Ingresos()
        self.gast = Gastos()
        self.aho = Ahorros()
    
    def graficaIngresos(self):
        ingreso = []
        ji = []

        i = self.ingres.consultarTodo()
        
        tri = self.ingres.totalRegistros()

        aux = ''
        cont = 0

        for ni, ti in enumerate(i):

            fecha = str(ti['Fecha']).split(' ')[0]

            if(aux == ''):
                aux = fecha
                cont = cont + ti['Monto']
            elif(aux == fecha):
                cont = cont + ti['Monto']
            else:
                ingreso.append(dict({ "Fecha" : aux, "Monto" : cont }))
                aux = fecha
                cont = ti['Monto']
            
            if((tri-1) == ni):
                ingreso.append(dict({ "Fecha" : aux, "Monto" : cont }))
                aux = ''
                cont = 0

        return ingreso
    
    def graficaGastos(self):
        gasto = []

        jg = []

        g = self.gast.consultarTodo()

        trg = self.gast.totalRegistros()

        aux = ''
        cont = 0

        for ng, tg in enumerate(g):

            fecha = str(tg['Fecha']).split(' ')[0]

            if(aux == ''):
                aux = fecha
                cont = cont + tg['Monto']
            elif(aux == fecha):
                cont = cont + tg['Monto']
            else:
                gasto.append(dict({ "Fecha" : aux, "Monto" : cont }))
                aux = fecha
                cont = tg['Monto']
            
            if((trg-1) == ng):
                gasto.append(dict({ "Fecha" : aux, "Monto" : cont }))
                aux = ''
                cont = 0

        return gasto

    def graficaAhorros(self):

        ahorro = []

        ja = []

        a = self.aho.consultarTodo()
        
        tra = self.aho.totalRegistros()

        aux = ''
        cont = 0

        for na, ta in enumerate(a):

            fecha = str(ta['Fecha']).split(' ')[0]

            if(ta['Total_Ahorrado'] == 0):
                pass

            elif(aux == ''):
                aux = fecha
                cont = cont + ta['Total_Ahorrado']
            elif(aux == fecha):
                cont = cont + ta['Total_Ahorrado']
            else:
                ahorro.append(dict({ "Fecha" : aux, "Monto" : cont }))
                aux = fecha
                cont = ta['Total_Ahorrado']
            
            if((tra-1) == na):
                ahorro.append(dict({ "Fecha" : aux, "Monto" : cont }))
                aux = ''
                cont = 0
        
        return ahorro

    def graficaDisIngresos(self):
        gingreso = []

        i = db.ingresos.find().sort( "Tipo", 1 )

        tri = self.ingres.totalRegistros()

        aux = ''
        cont = 0

        for ni, ti in enumerate(i):
            tipo = ti['Tipo']
            if(aux == ''):
                aux = ti['Tipo']
                cont = cont + ti['Monto']
            elif(aux == tipo):
                cont = cont + ti['Monto']
            else:
                gingreso.append(dict({ "label" : aux, "value" : cont }))
                aux = ti['Tipo']
                cont = ti['Monto']
            
            if((tri-1) == ni):
                gingreso.append(dict({ "label" : aux, "value" : cont }))
                aux = ''
                cont = 0
        return gingreso

    def graficaDisGastos(self):
        ggasto = []

        g = db.gastos.find().sort( "Tipo", 1 )

        trg = self.gast.totalRegistros()

        aux = ''
        cont = 0

        for ng, tg in enumerate(g):
            tipo = tg['Tipo']
            if(aux == ''):
                aux = tipo
                cont = cont + tg['Monto']
            elif(aux == tg['Tipo']):
                cont = cont + tg['Monto']
            else:
                ggasto.append(dict({ "label" : aux, "value" : cont }))
                aux = tg['Tipo']
                cont = tg['Monto']
            
            if((trg-1) == ng):
                ggasto.append(dict({ "label" : aux, "value" : cont }))
                aux = ''
                cont = 0

        return ggasto

class Auxuliar:
    
    def __init__(self,query):
        self.q = query

    def obtenerDia():
        dia = self.q['Fecha'].strftime("%d")
        return dia
    
    def obtenerMes():
        mes = self.q['Fecha'].strftime("%m")
        return mes

    def obtenerAnio():
        anio = self.q['Fecha'].strftime("%Y")
        return anio

