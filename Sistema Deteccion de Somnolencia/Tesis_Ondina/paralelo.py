# -*- coding: utf-8 -*-
import threading
import deteccion as d
import redneuronal as rn

class hiloCara(threading.Thread):
     def __init__(self,imagen,red,alarma):
         threading.Thread.__init__(self)
         self.alarma = alarma
         self.red = red
         self.imagen = imagen
         self.resultado = None

     def run(self):
         cara = d.deteccionFacial(self.imagen)
         if cara == None:
            """Si el sistema no encuentra ninguna cara debera generar una notificacion de sonido
               para avisar que hay algun problema"""
            self.alarma.deteccionNula()
         else:
             print "cara"
             self.resultado = rn.estimularRN(self.red,cara.flatten())
             return self.resultado


class hiloOjoIz(threading.Thread):
     def __init__(self,imagen,red,alarma):
         threading.Thread.__init__(self)
         self.alarma = alarma
         self.red = red
         self.imagen = imagen
         self.resultado = None

     def run(self):
         ojo_izq = d.deteccionOjoIzquierdo(self.imagen)
         if ojo_izq == None:
            """Si el sistema no encuentra ninguna cara debera generar una notificacion de sonido
               para avisar que hay algun problema"""
            self.alarma.deteccionNula()
         else:
             print "ojo izquierdo"
             self.resultado = rn.estimularRN(self.red,ojo_izq.flatten())
             return self.resultado


class hiloOjoDe(threading.Thread):
     def __init__(self,imagen,red,alarma):
         threading.Thread.__init__(self)
         self.alarma = alarma
         self.red = red
         self.imagen = imagen
         self.resultado = None

     def run(self):
         ojo_der = d.deteccionOjoDerecho(self.imagen)
         if ojo_der == None:
            """Si el sistema no encuentra ninguna cara debera generar una notificacion de sonido
               para avisar que hay algun problema"""
            self.alarma.deteccionNula()
         else:
             print "ojo derecho"
             self.resultado = rn.estimularRN(self.red,ojo_der.flatten())
             return self.resultado

