# -*- coding: utf-8 -*-
import os
import cv2

path = os.path.dirname(__file__)

def deteccionFacial(frame,gris):
    """Este modulo detecta los rostros utilizando el algoritmo Haar Cascade,
       retorna el area obtenida de la cara estableciendo el tamaño en 64*64"""

    #Cargar el archivo que contiene Haar Cascade
    cara = cv2.CascadeClassifier(path+'/haarcascades/haarcascade_frontalface_alt.xml')

    # Detecta la cara
    rectangulos = cara.detectMultiScale(gris)

    #Sobrepone el rectangulo sobre el video por cada cara encontrada
    for x, y, w, h in rectangulos:
        return cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0))
