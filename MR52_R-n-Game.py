'''
Created on 13 dec. 2012

@author: Aubree lois
'''

from src import mrQWindow
from ui import mrMainWindow
import sys
from multiprocessing import freeze_support

from PyQt4 import QtCore,QtGui

class mrRnGameApp(QtGui.QApplication):
    def __init__(self,argv):
        QtGui.QApplication.__init__(self,argv)
        self.platform = sys.platform
        self.win = mrQWindow.mrWindow(sys.platform)
        self.win.show()
    

if __name__ == "__main__":
    freeze_support()
    app =  mrRnGameApp(sys.argv)
    sys.exit(app.exec_())