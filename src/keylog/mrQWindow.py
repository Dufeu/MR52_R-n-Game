'''
Created on 27 oct. 2012

@author: Lois Aubree
'''
from PyQt4 import QtGui,QtCore
import time
import os
import sys
if sys.platform == "linux2":
    import mrLinuxHookThread
elif sys.platform == "win32": 
    import mrWinHookThread
else :
    print("OS not recognized")
class mrCWin(QtGui.QWidget):

    def __init__(self,platform):
        super(mrCWin,self).__init__()
        self.initUI(platform)
    
    def initUI(self,platform):
        self.setWindowTitle(" Ma fenetre")
        self.button = QtGui.QPushButton('button',self)
        if platform == "linux2":
            self.HookThread = mrLinuxHookThread.LinuxHookThread()
            self.connect(self.button, QtCore.SIGNAL('clicked()'),self.RunHookLinuxCallBack)
        elif platform == "win32":
            self.HookThread = mrWinHookThread.WinHookThread()
            self.connect(self.button, QtCore.SIGNAL('clicked()'),self.RunHookWinCallBack)
        
        timestr = time.localtime()
        timeF = time.time()
        print(" This window was created at this time:")
        print(timeF)
        self.show()
        
    def RunHookLinuxCallBack(self):
        mrLinuxHookThread.RunKeyCallBack(self)
        
    def RunHookWinCallBack(self):
        mrWinHookThread.RunKeyCallBack(self)