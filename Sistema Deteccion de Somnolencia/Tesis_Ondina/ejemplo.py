import sys
from PyQt4 import QtCore, QtGui 
class MainWindow(QtGui.QMainWindow):
    """A new window for the application."""
    def __init__(self):
        super(MainWindow, self).__init__()
        self.size = QtCore.QSize(20, 20)
        # This button will emit the signal when it is clicked.
        self.signal_button = QtGui.QPushButton("Click here", self)
        # This name is used to identify the  in the function.
        self.signal_button.setObjectName("signal_button")
        # This will wire up the signals and slots depending on names.
        QtCore.QMetaObject.connectSlotsByName(self)

    @QtCore.pyqtSlot()
    def on_signal_button_clicked(self):
        """This function will be triggered when the button is clicked."""
        self.resize(400,400)

def main():
    """docstring for main"""
    application = QtGui.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    application.exec_()

if __name__ == '__main__':
    main()
