
import cv2
import Image

def capturarVideo():

    """Se selecciona la camara a utilizar, en este caso al ser una sola, se utiliza el valor 0"""
    camara = cv2.VideoCapture(1)
    #camara = cv.CaptureFromCAM(0)


    #Se Establece resolucion del video en 320x240
    # esta funcion cno existe en vc2
    #camara.set(3, 640)
    #camara.set(4, 480)

    # esta funcion cno existe en vc2
    #if not camara.isOpened():
    #    print("No se puede abrir la camara")

    return camara

#-----------------------------------------OBTENER VIDEO-----------------------------

def obtenerVideo(camara):
    """Una vez obtenida la camara de donde se va a obtner el video, debemos obtener cada uno de
       los frames para dar inicio al procesamiento en tiempo real."""
    val, frame = camara.read()
    return val, frame

def mostrarVideo(nombre,frame):
    """Muestra en pantalla el video obtenido"""
    cv2.imshow(nombre, frame)
