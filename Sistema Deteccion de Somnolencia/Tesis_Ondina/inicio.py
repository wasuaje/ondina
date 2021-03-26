# -*- coding: utf-8 -*-
import threading
from threading import Thread

def servidor():
    import web
    web.run()

def escritorio():
    import app
    app.run()

if __name__ == '__main__':
    Thread(target = servidor).start()
    Thread(target = escritorio).start()
