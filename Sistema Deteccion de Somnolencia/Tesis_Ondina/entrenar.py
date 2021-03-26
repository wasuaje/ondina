# -*- coding: utf-8 -*-
import os
import cv2
import deteccion as d
import procesarImagen as p
from pybrain.datasets import SupervisedDataSet
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.tools.xml.networkwriter import NetworkWriter
from pybrain.tools.xml.networkreader import NetworkReader

path = os.path.dirname(__file__)


def entrenarOperador(red):
    #Se inicializa el dataset
    ds = SupervisedDataSet(4096,1)

    """Se crea el dataset, para ello procesamos cada una de las imagenes obteniendo los rostros,
       luego se le asignan los valores deseados del resultado la red neuronal."""


    for i,c in enumerate(os.listdir(os.path.dirname(path + '/static/img/operadores/'))):
        a = 0
        while a < 50:
            try:
                a += 1 
                im3 = cv2.imread(path + '/static/img/operadores/'+c)
                procesado = p.procesarImagen(im3)
                cara = d.deteccionFacial1(procesado)
                ds.addSample(cara.flatten(),10)
            except:
                pass
            

    trainer = BackpropTrainer(red, ds)
    print "Entrenando hasta converger"
    trainer.trainOnDataset(ds,100)
    NetworkWriter.writeToFile(red, 'rna_operador.xml')


def entrenarSonoliento(red):
    #Se inicializa el dataset
    ds = SupervisedDataSet(4096,1)

    """Se crea el dataset, para ello procesamos cada una de las imagenes obteniendo los rostros,
       luego se le asignan los valores deseados del resultado la red neuronal."""


    for i,c in enumerate(os.listdir(os.path.dirname(path + '/static/img/sleepy/'))):
        a = 0
        while a < 50:
            try:
                a += 1 
                im3 = cv2.imread(path + '/static/img/sleepy/'+c)
                procesado = p.procesarImagen(im3)
                cara = d.deteccionFacial1(procesado)
                ds.addSample(cara.flatten(),10)
            except:
                pass
            

    trainer = BackpropTrainer(red, ds)
    print "Entrenando hasta converger"
    trainer.trainOnDataset(ds,100)
    NetworkWriter.writeToFile(red, 'rna_somnolencia.xml')



#para entrenar operadores manualmente
#red_operador = NetworkReader.readFrom('rna_operador.xml')
#entrenarOperador(red_operador)

#para entrenar somnolencia manualmente
#red_somno = NetworkReader.readFrom('rna_somnolencia.xml')
#entrenarSonoliento(red_somno)