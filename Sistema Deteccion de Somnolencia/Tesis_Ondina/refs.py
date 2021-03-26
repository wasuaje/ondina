# -*- coding: utf-8 -*-
import os
import time
import cv2
import procesarImagen as pi
import deteccion as d
import redneuronal as rn
#import video as v
from alarma import Alarma
from pybrain.tools.xml.networkreader import NetworkReader
import sys

def run():
    """Es la clase principal en el cual se sigue la secuencia del procesamiento"""
    a = Alarma()
    """Al inicializar genera un sonido inidicado queel dispositivo esa funcionando
    sin contratiempos"""
    a.inicio()

    #Crear Red Neuronal
    red1 = rn.crearRN()
    red2 = rn.crearRN()
    red3 = rn.crearRN()

    #Se verifica si el archivo xml que contiene la red neuronal entrenada existe
    path = os.path.dirname(__file__)

    if os.path.isfile('rna_somnolencia.xml'):
        red_somnolencia = NetworkReader.readFrom('rna_somnolencia.xml')
    else:
        print "No existe la red neuronal solicitada"

    if os.path.isfile('rna_atento.xml'):
        red_atento = NetworkReader.readFrom('rna_atento.xml')
    else:
        print "No existe la red neuronal solicitada"

    if os.path.isfile('rna_operador.xml'):
        red_operador = NetworkReader.readFrom('rna_operador.xml')
    else:
        print "No existe la red neuronal solicitada"    
    
    #Se la camara con la que se va a trabajar
    #try:
    #    camara = v.capturarVideo()
    #except:
    #    print "no camara",sys.exc_info()[0],sys.exc_info()[1]        
    #    a.noCamara()
	
    camara = cv2.VideoCapture(0)
    #camara.set(15,8.0)
    camara.set(cv2.cv.CV_CAP_PROP_BRIGHTNESS, 160)
    camara.set(cv2.cv.CV_CAP_PROP_EXPOSURE, 20.0)
    time.sleep(3) 
    while True:
        Somnolencia = 0.00001
        Atencion = 0.00001
        Operador = 0.00001
        #print "leyendo camara"
        is_sucessfully_read, img = camara.read()

        # is_sucessfuly_read retorna falso cuando no puede apturar de la camara         
        if(is_sucessfully_read):
            cv2.imshow("Camera Feed", img)
        else:
            print "No se pudo detectar entrada de video desde %s. Saliendo..." % capture
            break
       
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
             break 
        

        #print "procesando imagen"
        frame=img
     #    #Procesar imagenes del video
        improcesada = pi.procesarImagen(frame)
        cara = d.deteccionFacial(improcesada) 
        try:
            if not cara:
                print "No hay operador frente el Monitor"                    
                a.ajeno()
        except ValueError:
            #print "procesando somno"
            Somnolencia = rn.estimularRN(red_somnolencia,cara.flatten())
            #print "procesando atencion"
            Atencion = rn.estimularRN(red_atento,cara.flatten())
            #print "procesando operador"
            Operador = rn.estimularRN(red_operador,cara.flatten())
            print "Somnolencia: %s  Atencion: %s  Operador:%s" %  (float(Somnolencia[0]), float(Atencion[0]), float(Operador[0]))
            if float(Operador[0]) < 5:
                print "Estado de la alarma: Persona no reconocida"
                a.ajeno()
            if float(Atencion[0]) < 5:
                print "Estado de la alarma: Distraido"
                a.distraido()
            if float(Somnolencia[0]) < 9.82:
                print "Estado de la alarma: Somnoliento"
                a.somnoliento()
            # try:
            #     Somnolencia = rn.estimularRN(red_somnolencia,cara.flatten())
            #     Atencion = rn.estimularRN(red_atento,cara.flatten())
            #     Operador = rn.estimularRN(red_operador,cara.flatten())
            
            # except:
            #     print "Nadie frente el Monitor"
                # Colocar junto a la linea de arriba para ver codigo de error ,sys.exc_info()[0],sys.exc_info()[1]                
        #time.sleep(2)
    cv2.destroyAllWindows()
    camara.release()    

if __name__ == "__main__":
    run()
