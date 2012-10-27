'''
Created on 27 oct. 2012

@author: Lois Aubree
'''
from PyQt4 import QtGui,QtCore
import mrHook

class mrCWin(QtGui.QWidget):

    def __init__(self):
        super(mrCWin,self).__init__()
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(" Ma fenetre")
        button = QtGui.QPushButton('button',self)
        button.clicked.connect(mrHook.RunKeyCallBack)
        self.show()
        