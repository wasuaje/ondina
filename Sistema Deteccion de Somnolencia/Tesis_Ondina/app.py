# -*- coding: utf-8 -*-

"""This contain the Desktop app that calls the Web application"""

__author__ = "Ondina"
__version__ = 0.1


import sys
import web
from PyQt4 import QtCore, QtGui, QtWebKit

class WebDesktop(QtGui.QMainWindow):

    def __init__(self):
        super(WebDesktop, self).__init__()
        self.size = QtCore.QSize(40, 10)
        # This button will emit the signal when it is clicked.
        self.signal_button = QtGui.QPushButton("Click here", self)
        # This name is used to identify the  in the function.
        self.signal_button.setObjectName("signal_button")
        # This will wire up the signals and slots depending on names.
        QtCore.QMetaObject.connectSlotsByName(self)

    @QtCore.pyqtSlot()
    def on_signal_button_clicked(self):
        """
            Initialize the browser GUI and connect the events
        """

        self.resize(1400,800)
        self.centralwidget = QtGui.QWidget(self)

        self.mainLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.mainLayout.setSpacing(0)
        self.mainLayout.setMargin(1)

        self.frame = QtGui.QFrame(self.centralwidget)

        self.gridLayout = QtGui.QVBoxLayout(self.frame)
        self.gridLayout.setMargin(0)
        self.gridLayout.setSpacing(0)

        self.horizontalLayout = QtGui.QHBoxLayout()

        self.gridLayout.addLayout(self.horizontalLayout)

        self.html = QtWebKit.QWebView()
        self.gridLayout.addWidget(self.html)
        self.mainLayout.addWidget(self.frame)
        self.setCentralWidget(self.centralwidget)

        self.url = "http://127.0.0.1:8080/"
        self.browse()
        
        #Barra de menu
        fileMenu = self.menuBar().addMenu(self.tr("&Inicio"))
        inicio = fileMenu.addAction(self.tr("Inicio"))
        eliminar = fileMenu.addAction(self.tr("Eliminar Operador"))
        entrenar = fileMenu.addAction(self.tr("Reestablecer Programa"))
        cambiar = fileMenu.addAction(self.tr("Cambiar Password"))
        salir = fileMenu.addAction(self.tr("Salir"))
        helpMenu = self.menuBar().addMenu(self.tr("&Ayuda"))
        ayuda = helpMenu.addAction(self.tr("&Ayuda"))
        acerca = helpMenu.addAction(self.tr("&Acerca de"))
        self.connect(inicio, QtCore.SIGNAL("triggered()"), self.ini)
        self.connect(eliminar, QtCore.SIGNAL("triggered()"), self.eliminar)
        self.connect(entrenar, QtCore.SIGNAL("triggered()"), self.entrenar)
        self.connect(cambiar, QtCore.SIGNAL("triggered()"), self.cambiar)
        self.connect(salir, QtCore.SIGNAL("triggered()"), QtCore.SLOT("close()"))
        self.connect(ayuda, QtCore.SIGNAL("triggered()"), self.mosAyuda)
        self.connect(acerca, QtCore.SIGNAL("triggered()"), self.showAboutBox)

        # Set up the rest of the window.

    def ini(self):
        self.url = "http://127.0.0.1:8080/"
        self.html.hide()
        self.html.load(QtCore.QUrl(self.url))
        self.html.show()

    def eliminar(self):
        self.url = "http://127.0.0.1:8080/eliminar"
        self.html.hide()
        self.html.load(QtCore.QUrl(self.url))
        self.html.show()
    
    def cambiar(self):
        self.url = "http://127.0.0.1:8080/cambiar"
        self.html.hide()
        self.html.load(QtCore.QUrl(self.url))
        self.html.show()

    def entrenar(self):
        self.url = "http://127.0.0.1:8080/entrenar"
        self.html.hide()
        self.html.load(QtCore.QUrl(self.url))
        self.html.show()

    def mosAyuda(self):
        self.url = "http://127.0.0.1:8080/ayuda"
        self.html.hide()
        self.html.load(QtCore.QUrl(self.url))
        self.html.show()

    def showAboutBox(self):
        QtGui.QMessageBox.information(self, self.tr("Acerca de este programa"),
        self.tr(u"Esta es la version "+str(__version__)+" del Sistema de Reconocimiento de Somnolencia. \n Hecha por "+__author__.encode("utf-8")))

    def browse(self):
        """
            Make a web browse on a specific url and show the page on the
            Webview widget.
        """

        self.html.load(QtCore.QUrl(self.url))
        self.html.show()

def run():
    app = QtGui.QApplication(sys.argv)
    main = WebDesktop()
    nombre = 'Reconocimiento de somnolencia'
    main.setWindowTitle(nombre.decode('utf8'))
    main.show()
    app.exec_()
   

