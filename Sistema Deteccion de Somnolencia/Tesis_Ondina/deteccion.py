# -*- coding: utf-8 -*-
import os
import cv2
from alarma import Alarma

global aux
aux = True
a = Alarma()
path = os.path.dirname(__file__)
	

def deteccionFacial(gris):
    """Este modulo detecta los rostros utilizando el algoritmo Haar Cascade,
       retorna el area obtenida de la cara estableciendo el tamaño en 64*64"""

    #Cargar el archivo que contiene Haar Cascade
    cara = cv2.CascadeClassifier(path+'/haarcascades/haarcascade_frontalface_alt.xml')

    # Detecta la cara
    rectangulos = cara.detectMultiScale(gris)
    #faces = cv.HaarDetectObjects(            smallImage, faceCascade, cv.CreateMemStorage(0),            haar_scale, min_neighbors, haar_flags, min_size        )

    #print len(rectangulos)
    if not len(rectangulos)>0:
	  global aux
	  aux = False
    else:
	  global aux
	  aux = True
    #Sobrepone el rectangulo sobre el video por cada cara encontrada
    for x,y, width,height in rectangulos:
        cara_cortada = gris[y:y+height,x:x+width]
        #print "data",cv2.resize(cara_cortada,(64,64))
        return cv2.resize(cara_cortada,(64,64))

def deteccionFacial1(gris):
    """Este modulo detecta los rostros utilizando el algoritmo Haar Cascade,
       retorna el area obtenida de la cara estableciendo el tamaño en 64*64"""

    #Cargar el archivo que contiene Haar Cascade
    cara = cv2.CascadeClassifier(path+'/haarcascades/haarcascade_frontalface_alt.xml')

    # Detecta la cara
    rectangulos = cara.detectMultiScale(gris)

    #Sobrepone el rectangulo sobre el video por cada cara encontrada
    for x,y, width,height in rectangulos:
        cara_cortada = gris[y:y+height,x:x+width]
        return cv2.resize(cara_cortada,(64,64))



def deteccionFacialImg(nombre,gris):
    """Este modulo detecta los rostros utilizando el algoritmo Haar Cascade,
       retorna el area obtenida de la cara estableciendo el tamaño en 64*64"""

    #Cargar el archivo que contiene Haar Cascade
    cara = cv2.CascadeClassifier(path+'/haarcascades/haarcascade_frontalface_alt.xml')

    # Detecta la cara
    rectangulos = cara.detectMultiScale(gris)

    #Sobrepone el rectangulo sobre el video por cada cara encontrada
    for x,y, width,height in rectangulos:
        cara_cortada = gris[y:y+height,x:x+width]
        cv2.imwrite(path + '/static/img/caras/'+nombre, cv2.resize(cara_cortada,(64,64))) 


