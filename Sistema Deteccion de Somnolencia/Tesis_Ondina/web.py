# -*- coding: utf-8 -*-
"""This contains the main CherryPy web server and the controller with all the function
   to process the HTTP request"""

__author__ = "Javier Arnoldo Fonseca Paredes"
__version__ = 0.1

import os
import cv2
import shutil
import jinja2
import hashlib
import cherrypy
import sqlite3 as sql
import entrenar as e
import deteccion as d
import redneuronal as rn
import procesarImagen as p
from cherrypy import tools
from simplejson import JSONEncoder

root_path = os.path.dirname(__file__)

# jinja2 template renderer
env = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.join(root_path, 'templates')))

config = {
 '/': {
   'tools.staticdir.root': root_path,

  },
 '/static': {
   'tools.staticdir.on': True,
   'tools.staticdir.dir': os.path.join(root_path, 'static'),
   },
}


encoder = JSONEncoder()

def jsonify_tool_callback(*args, **kwargs):
    response = cherrypy.response
    response.headers['Content-Type'] = 'application/json'
    response.body = encoder.iterencode(response.body)

cherrypy.tools.jsonify = cherrypy.Tool('before_finalize', jsonify_tool_callback, priority=30)


def render_template(template,**context):
    global env
    template = env.get_template(template)
    return template.render(context)


class WEB(object):

    @cherrypy.expose()
    def index(self):
        imagenes = []
        path = os.path.dirname(__file__)
        for i,c in enumerate(os.listdir(os.path.dirname(path + '/static/img/operadores/'))):
            imagenes.append(c)
        tmpl = env.get_template('index.html')
        return tmpl.render(imagenes=imagenes)
#        return render_template('index.html')


    @cherrypy.expose
    def guardarimagen(self, filUpload):
        mensaje = ""
        imagenes = []
        path = os.path.dirname(__file__)

       # cherrypy.cherry.session['filUpload'] = filUpload
        data_name = filUpload.filename
        upload_path = path + '/static/img/temp/' + filUpload.filename

        size = 0
        all_data = bytearray()
        while True:
            data = filUpload.file.read(8192)
            all_data += data
            if not data:
                break
            size += len(data)
        
        #Se guarda la imagen temporalmente
        saved_file=open(upload_path, 'wb') 
        saved_file.write(all_data) 
        saved_file.close()

        #Se hace la deteccion para verificar si la foto sirve
        try:
            img = cv2.imread(upload_path)
            procesado = p.procesarImagen(img)
            d.deteccionFacialImg(data_name,procesado)
            
            mensaje = "La foto fue guardada con exito"
            cv2.imwrite(path + '/static/img/operadores/'+data_name,img)
            os.remove(upload_path)
        except:
            mensaje = "Debe subir una foto clara tipo carnet para poder ser procesada"
            os.remove(upload_path)
        
        
        for i,c in enumerate(os.listdir(os.path.dirname(path + '/static/img/operadores/'))):
            imagenes.append(c)
        tmpl = env.get_template('index.html')
        return tmpl.render(mensaje=mensaje,imagenes=imagenes)




class Eliminar(object):
    """Las clases secundarias muestran las otras paginas"""
    @cherrypy.expose()
    def index(self):
        imagenes = []
        path = os.path.dirname(__file__)
        for i,c in enumerate(os.listdir(os.path.dirname(path + '/static/img/operadores/'))):
            imagenes.append(c)
        tmpl = env.get_template('eliminar.html')
        return tmpl.render(imagenes=imagenes)

    @cherrypy.expose
    def eliminarimagen(self, operador):
        imagenes = []
        path = os.path.dirname(__file__)
        
        filename = operador

        eliminar_path = path + '/static/img/operadores/' + filename

        os.remove(eliminar_path)

        for i,c in enumerate(os.listdir(os.path.dirname(path + '/static/img/operadores/'))):
            imagenes.append(c)
        tmpl = env.get_template('eliminar.html')
        return tmpl.render(mensaje="La foto fue eliminada con exito",imagenes=imagenes)


class Entrenar(object):
    """Las clases secundarias muestran las otras paginas"""
    @cherrypy.expose()
    def index(self):
        return render_template('entrenar.html')

    @cherrypy.expose
    @tools.json_out(on = True)
    @tools.json_out(on = True)
    def entrenar(self, **jsonText):
        
        path = os.path.dirname(__file__)
        

        #Se eliminan todos los operadores
        for i,c in enumerate(os.listdir(os.path.dirname(path + '/entrenamiento/'))):
            if(c):
                os.remove(path + '/entrenamiento/'+c)
            else:
                break

        #Se multiplica las fotos de los operadores x20
        for i,c in enumerate(os.listdir(os.path.dirname(path + '/static/img/caras/'))):
            img = cv2.imread(path + '/static/img/caras/'+c)
            a = 0
            while a < 20:
                a += 1 
                cv2.imwrite(path + '/entrenamiento/'+str(a)+c,img)

        red = rn.crearRN()
        e.entrenarOperador(red)
        return {'mensaje' : 'El sistema fue restructurado con exito' }
            

class Cambiar(object):
    """Las clases secundarias muestran las otras paginas"""
    @cherrypy.expose()
    def index(self):
        return render_template('cambiar.html')
    
    @cherrypy.expose
    @tools.json_out(on = True)
    @tools.json_out(on = True)
    def cambiar(self, **jsonText):
        
        path = os.path.dirname(__file__)
        context = jsonText

        valor = context['contra']
        
        encrypted_pass1 = hashlib.sha1(valor.encode('utf-8')).hexdigest()


        db = sql.connect('p.db')
        # Register the function
        c = db.cursor()
        c.execute("select * from users where password = ?",[encrypted_pass1])
        if(c.rowcount):
            mensaje = True
        else:
            mensaje = False
        db.close()
        return {'mensaje' : mensaje }

def run():
    root = WEB()
    root.eliminar = Eliminar()
    root.cambiar = Cambiar()
    root.entrenar = Entrenar()
    cherrypy.tree.mount(root,"/")
    cherrypy.tree.mount(root.eliminar,"/eliminar")
    cherrypy.tree.mount(root.entrenar,"/entrenar")
    cherrypy.tree.mount(root.cambiar,"/cambiar")
    #cherrypy.config.update({'server.socket_host': '0.0.0.0'})
    cherrypy.quickstart(WEB(), '/', config)
