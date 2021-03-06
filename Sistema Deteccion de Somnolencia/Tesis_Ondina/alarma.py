# -*- coding: utf-8 -*-
import os
import pyglet
import pygame
from fuzzy import LogicaDifusa as ld

path = os.path.dirname(__file__)

 
def playmusic(soundfile):
    """Stream music with mixer.music module in blocking manner.
    This will stream the sound from disk while playing.
    """
    pygame.init()
    pygame.mixer.music.load(soundfile)
    pygame.mixer.music.play(0)

    clock = pygame.time.Clock()
    clock.tick(10)
    while pygame.mixer.music.get_busy():
	pygame.event.poll()
	clock.tick(10)
 
def stopmusic():
    """stop currently playing music"""
    pygame.mixer.music.stop()
 
def getmixerargs():
    pygame.mixer.init()
    freq, size, chan = pygame.mixer.get_init()
    return freq, size, chan
 
 
def initMixer():
    BUFFER = 3072 # audio buffer size, number of samples since pygame 1.8.
    FREQ, SIZE, CHAN = getmixerargs()
    pygame.mixer.init(FREQ, SIZE, CHAN, BUFFER)

class Alarma:

    def __init__(self):
        self.auxs = 0
        self.auxd = 0
        self.somnolencia = ""
        self.atencion = ""
        self.estado = ""
        self.esres = ""
        self.aux = False
        self.reglas = ld.iniReglas()
        self.iniBloqueDifusor()


    def iniBloqueDifusor(self):
        self.somnolencia = ld.declararConjunto("Somnolencia",0.00000,10.00000)
        ld.variableLinguistica(self.somnolencia,"Pocas")
        ld.variableLinguistica(self.somnolencia,"Intermedias")
        ld.variableLinguistica(self.somnolencia,"Dormido")

        ld.asignarFuncionPertenencia(self.somnolencia,0,"Triangular",(0.00000,02.50000,05.00000))
        ld.asignarFuncionPertenencia(self.somnolencia,1,"Triangular",(02.50001,05.00001,07.50000))
        ld.asignarFuncionPertenencia(self.somnolencia,2,"Triangular",(05.00002,07.50001,10.00000))


        self.atencion = ld.declararConjunto("Atento",0.00000,10.00000)
        ld.variableLinguistica(self.atencion,"Poco")
        ld.variableLinguistica(self.atencion,"Moderado")
        ld.variableLinguistica(self.atencion,"Atento")

        ld.asignarFuncionPertenencia(self.atencion,0,"Triangular",(0.00000,02.50000,05.00000))
        ld.asignarFuncionPertenencia(self.atencion,1,"Triangular",(02.500001,05.00001,07.50000))
        ld.asignarFuncionPertenencia(self.atencion,2,"Triangular",(05.00002,07.50001,10.00000))


        self.estado = ld.declararConjunto("Estado",0.00000,5.00000)
        ld.variableLinguistica(self.estado,"Atento")
        ld.variableLinguistica(self.estado,"Distraido")
        ld.variableLinguistica(self.estado,"Somnoliento")
        ld.variableLinguistica(self.estado,"Dormido")

        ld.asignarFuncionPertenencia(self.estado,0,"Triangular",(0.00000,1.00000,2.00000))
        ld.asignarFuncionPertenencia(self.estado,1,"Triangular",(1.00001,2.00001,3.00000))
        ld.asignarFuncionPertenencia(self.estado,2,"Triangular",(2.00002,3.00001,4.00000))
        ld.asignarFuncionPertenencia(self.estado,3,"Triangular",(3.00002,4.00001,5.00000))


        ld.crearReglas(self.reglas,"if Somnolencia is Pocas and Atento is Poco then Estado is Distraido")
        ld.crearReglas(self.reglas,"if Somnolencia is Intermedias and Atento is Poco then Estado is Distraido")
        ld.crearReglas(self.reglas,"if Somnolencia is Dormido and Atento is Poco then Estado is Dormido")

        ld.crearReglas(self.reglas,"if Somnolencia is Pocas and Atento is Moderado then Estado is Distraido")
        ld.crearReglas(self.reglas,"if Somnolencia is Intermedias and Atento is Moderado then Estado is Somnoliento")
        ld.crearReglas(self.reglas,"if Somnolencia is Dormido and Atento is Moderado then Estado is Dormido")

        ld.crearReglas(self.reglas,"if Somnolencia is Pocas and Atento is Atento then Estado is Atento")
        ld.crearReglas(self.reglas,"if Somnolencia is Intermedias and Atento is Atento then Estado is Somnoliento")
        ld.crearReglas(self.reglas,"if Somnolencia is Dormido and Atento is Atento then Estado is Dormido")

    def motorDifuso(self,Somnolencia,Atencion):
        if Somnolencia<0.00000:
           Somnolencia = 0.00001
        if Somnolencia>10:
           Somnolencia = 9.99999
        if Atencion<0.00000:
           Atencion = 0.00001
        if Atencion>10:
           Atencion = 9.99999
        fsomnolencia = ld.fusificar(Somnolencia,self.somnolencia)
        fatencion = ld.fusificar(Atencion,self.atencion)


        motor = ld.inicializarMotor()
        ld.agregarAlMotor(motor,self.somnolencia,fsomnolencia)
        ld.agregarAlMotor(motor,self.atencion,fatencion)

        resultado = ld.procesar(self.reglas,motor,self.estado)
        return resultado

    def alertar(self,resultado):
        estado, val = resultado

        if not self.aux:
            self.aux = True
        else:
            if estado == "Distraido":
                self.distraido()
            if estado == "Somnoliento":
                self.somnoliento()
            if estado == "Dormido":
                self.somnoliento()
            if estado == "Desconocido":
                self.ajeno()


    def noCamara(self):
        pygame.init()
	pygame.mixer.music.load("error.mp3")
	pygame.mixer.music.play(0)

	clock = pygame.time.Clock()
	clock.tick(5)
	while pygame.mixer.music.get_busy():
	    pygame.event.poll()
	    clock.tick(5)
        pygame.mixer.music.stop()
            
    def deteccionNula(self):
	print "Alarma no deteccion"
        pygame.init()
	pygame.mixer.music.load("error2.mp3")
	pygame.mixer.music.play(0)

	clock = pygame.time.Clock()
	clock.tick(5)
	while pygame.mixer.music.get_busy():
	    pygame.event.poll()
	    clock.tick(5)
        pygame.mixer.music.stop()

    def distraido(self):
        pygame.init()
	pygame.mixer.music.load("a3.mp3")
	pygame.mixer.music.play(0)

	clock = pygame.time.Clock()
	clock.tick(5)
	while pygame.mixer.music.get_busy():
	    pygame.event.poll()
	    clock.tick(5)
        pygame.mixer.music.stop()

    def somnoliento(self):
        pygame.init()
	pygame.mixer.music.load("a2-3.mp3")
	pygame.mixer.music.play(0)

	clock = pygame.time.Clock()
	clock.tick(52)
	while pygame.mixer.music.get_busy():
	    pygame.event.poll()
	    clock.tick(5)
        pygame.mixer.music.stop()
    
    def ajeno(self):
        pygame.init()
	pygame.mixer.music.load("a2-3.mp3")
	pygame.mixer.music.play(0)

	clock = pygame.time.Clock()
	clock.tick(10)
	while pygame.mixer.music.get_busy():
	    pygame.event.poll()
	    clock.tick(10)
        pygame.mixer.music.stop()

    def inicio(self):
	print "Alarma inicio"
        pygame.init()
	pygame.mixer.music.load("ok.mp3")
	pygame.mixer.music.play(0)

	clock = pygame.time.Clock()
	clock.tick(10)
	while pygame.mixer.music.get_busy():
	    pygame.event.poll()
	    clock.tick(10)
        pygame.mixer.music.stop()


