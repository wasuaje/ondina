import numpy as np
import os
import cv2

path = os.path.dirname(__file__)

camara = cv2.VideoCapture(1)

    #Se Establece resolucion del video en 320x240
camara.set(3, 320)
camara.set(4, 240)

if not camara.isOpened():
    print("No se puede abrir la camara")

cara = cv2.CascadeClassifier(path+'/haarcascades/haarcascade_frontalface_alt.xml')

while True:
    val, frame = camara.read()
    gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    fb = cv2.bilateralFilter(gris, 0, 32, 2)
    ip = cv2.equalizeHist(fb)


    # Detecta la cara
    rectangulos = cara.detectMultiScale(ip)

    #Sobrepone el rectangulo sobre el video por cada cara encontrada
    for (x,y,w,h) in rectangulos:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = ip[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        

    cv2.imshow('img',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        cv2.destroyAllWindows()




def convertirGris(frame):
    """Convierte la imagen a color a escala de grises"""
    try:
        gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    except:
        gris = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    return gris

def histograma(frame):
    """Procesa la imagen mejorada en escala de grises utilizando la equalizacion por
histogramas."""
    #Imagen mejorada por Equalizacion de Histogramas.
    histograma = cv2.equalizeHist(frame)
    return histograma

if __name__ == "__main__":
    main()
