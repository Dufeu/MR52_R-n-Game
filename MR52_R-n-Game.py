'''
Created on 13 dec. 2012

@author: Aubree lois
'''

from src import mrQWindow
from ui import mrMainWindow
import sys
import pythoncom

from PyQt4 import QtCore,QtGui

class mrRnGameApp(QtGui.QApplication):
    def __init__(self,argv):
        QtGui.QApplication.__init__(self,argv)
        self.platform = sys.platform
        self.win = mrQWindow.mrWindow(sys.platform)
    
        self.connect(self.win, QtCore.SIGNAL('closeApplication'),self.closeApp)
        self.win.show()
    
    def closeApp(self):
        sys.exit(0)
        
        

if __name__ == "__main__":
    app =  mrRnGameApp(sys.argv)

    app.exec_()
    
