# -*- coding: utf-8 -*-
import cv2
import video as v
import sys

def procesarImagen(frame):
    """Este es el modulo principal del procesamiento de la imagen y sigue los
       siguientes pasos:
           -Convierte la imagen a escala de grises
           -Suaviza la imagen para reducir el ruido de la imagen
           -Mejora la imagen mediante la equalizacion por histogramas"""
    gris = convertirGris(frame)
    noruido = filtroBilateral(gris)
    mejorado = histograma(noruido)    
    #mejorado=gris
    return mejorado


def filtroBilateral(frame):
    """Procesa la imagen en escala de grises utilizando filtro bilateral para reducir
       el ruido de la imagen producido, bien sea, por la baja luminosidad o por la
       calidad de la imagen obtenida."""
    fb = cv2.bilateralFilter(frame, 0, 32, 2)
    return fb

def convertirGris(frame):
    """Convierte la imagen a color a escala de grises"""
    #grayscale = cv2.createimage((frame.width, frame.height), 8, 1)
    #print "frame",frame
    try:
        gris = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY, (64,64))
        #gris = cv2.CvtColor(frame, grayscale, cv2.CV_BGR2GRAY)
    except:
        print "Error convirtiendo a gris",sys.exc_info()[0],sys.exc_info()[1]        
        #gris = cv2.CvtColor(frame, grayscale, cv2.CV_BGR2GRAY)
        #gris = cv2.cvtColor(frame, cv2.CV_RGB2GRAY)

    return gris

def histograma(frame):
    """Procesa la imagen mejorada en escala de grises utilizando la equalizacion por
       histogramas."""
    #Imagen mejorada por Equalizacion de Histogramas.
    histograma = cv2.equalizeHist(frame)
    return histograma

