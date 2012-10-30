'''
Created on 27 oct. 2012

@author: Lois Aubree
'''
from PyQt4 import QtGui,QtCore
import time
import os
import sys
from ui import mrMainWindow

if sys.platform == "linux2":
    import mrLinuxHookThread
elif sys.platform == "win32": 
    import mrWinHookThread
else :
    print("OS not recognized")
class mrCWin(QtGui.QMainWindow):

    def __init__(self,platform):
        super(mrCWin,self).__init__()
        self.initUI(platform)
    
    def initUI(self,platform):
        self.setWindowTitle(" Ma fenetre")
        self.ui = mrMainWindow.Ui_MainWindow()
        self.ui.setupUi(self)
        
        if platform == "linux2":
            self.HookThread = mrLinuxHookThread.LinuxHookThread()
            self.connect(self.ui.actionRun_All_Record, QtCore.SIGNAL('triggered()'),self.RunHookLinuxAllCallBack)
            self.connect(self.ui.actionRun_Key_Record, QtCore.SIGNAL('triggered()'),self.RunHookLinuxKeyCallBack)
            self.connect(self.ui.actionRun_Mouse_Record, QtCore.SIGNAL('triggered()'),self.RunHookLinuxMouseCallBack)
            
            self.connect(self.ui.actionStop_All_Record, QtCore.SIGNAL('triggered()'),self.StopHookLinuxAllCallBack)
            self.connect(self.ui.actionStop_Key_Record, QtCore.SIGNAL('triggered()'),self.StopHookLinuxKeyCallBack)
            self.connect(self.ui.actionStop_Mouse_Record, QtCore.SIGNAL('triggered()'),self.StopHookLinuxMouseCallBack)
            
            
        elif platform == "win32":
            self.HookThread = mrWinHookThread.WinHookThread()
            self.HookThread.setOnkeyBoardEvent(self.OnKeyboardEvent)
            self.HookThread.setOnkeyMouseEvent(self.OnMouseEvent)
            self.connect(self.ui.actionRun_All_Record, QtCore.SIGNAL('triggered()'),self.RunHookWinAllCallBack)
            self.connect(self.ui.actionRun_Key_Record, QtCore.SIGNAL('triggered()'),self.RunHookWinKeyCallBack)
            self.connect(self.ui.actionRun_Mouse_Record, QtCore.SIGNAL('triggered()'),self.RunHookWinMouseCallBack)
            
            self.connect(self.ui.actionStop_All_Record, QtCore.SIGNAL('triggered()'),self.StopHookWinAllCallBack)
            self.connect(self.ui.actionStop_Key_Record, QtCore.SIGNAL('triggered()'),self.StopHookWinKeyCallBack)
            self.connect(self.ui.actionStop_Mouse_Record, QtCore.SIGNAL('triggered()'),self.StopHookWinMouseCallBack)
            
        
        self.connect(self.ui.actionQuit,QtCore.SIGNAL('triggered()'),self.CallBackExit)
            
        
            
        self.show()
        
    """ ---------------------------------------- Linux CallBacks ----------------------------------------------------"""     
        
    def RunHookLinuxAllCallBack(self):
        self.ui.actionRun_All_Record.setDisabled(True)
        self.ui.actionRun_Key_Record.setDisabled(True)
        self.ui.actionRun_Mouse_Record.setDisabled(True)
        self.ui.actionStop_All_Record.setEnabled(True)
        self.ui.actionStop_Key_Record.setEnabled(True)
        self.ui.actionStop_Mouse_Record.setEnabled(True)
        mrLinuxHookThread.RunAllCallBack(self)
    
    def RunHookLinuxKeyCallBack(self):
        self.ui.actionRun_Key_Record.setDisabled(True)
        self.ui.actionStop_Key_Record.setEnabled(True)
        mrLinuxHookThread.RunKeyCallBack(self)
    
    def RunHookLinuxMouseCallBack(self):
        self.ui.actionRun_Mouse_Record.setDisabled(True)
        self.ui.actionStop_Mouse_Record.setEnabled(True)
        mrLinuxHookThread.RunMouseCallBack(self)
    
    
    def StopHookLinuxAllCallBack(self):
        self.ui.actionRun_All_Record.setEnabled(True)
        self.ui.actionRun_Key_Record.setEnabled(True)
        self.ui.actionRun_Mouse_Record.setEnabled(True)
        self.ui.actionStop_All_Record.setDisabled(True)
        self.ui.actionStop_Key_Record.setDisabled(True)
        self.ui.actionStop_Mouse_Record.setDisabled(True)
        mrLinuxHookThread.StopAllCallBack(self)
    
    def StopHookLinuxKeyCallBack(self):
        self.ui.actionRun_Key_Record.setEnabled(True)
        self.ui.actionStop_Key_Record.setDisabled(True)
        mrLinuxHookThread.StopKeyCallBack(self)

    def StopHookLinuxMouseCallBack(self):
        self.ui.actionRun_Mouse_Record.setEnabled(True)
        self.ui.actionStop_Mouse_Record.setDisabled(True)
        mrLinuxHookThread.StopMouseCallBack(self)

    """ ---------------------------------------- Linux CallBacks ----------------------------------------------------"""
        
    def RunHookWinAllCallBack(self):
        self.ui.actionRun_All_Record.setDisabled(True)
        self.ui.actionRun_Key_Record.setDisabled(True)
        self.ui.actionRun_Mouse_Record.setDisabled(True)
        self.ui.actionStop_All_Record.setEnabled(True)
        self.ui.actionStop_Key_Record.setEnabled(True)
        self.ui.actionStop_Mouse_Record.setEnabled(True)
        mrWinHookThread.RunAllCallBack(self)
        
    def RunHookWinKeyCallBack(self):
        self.ui.actionRun_Key_Record.setDisabled(True)
        self.ui.actionStop_Key_Record.setEnabled(True)
        mrWinHookThread.RunKeyCallBack(self)
    
    def RunHookWinMouseCallBack(self):
        self.ui.actionRun_Mouse_Record.setDisabled(True)
        self.ui.actionStop_Mouse_Record.setEnabled(True)
        mrWinHookThread.RunMouseCallBack(self)
    
    def StopHookWinAllCallBack(self):
        self.ui.actionRun_All_Record.setEnabled(True)
        self.ui.actionRun_Key_Record.setEnabled(True)
        self.ui.actionRun_Mouse_Record.setEnabled(True)
        self.ui.actionStop_All_Record.setDisabled(True)
        self.ui.actionStop_Key_Record.setDisabled(True)
        self.ui.actionStop_Mouse_Record.setDisabled(True)
        mrWinHookThread.StopAllCallBack(self)
        
    def StopHookWinKeyCallBack(self):
        self.ui.actionRun_Key_Record.setEnabled(True)
        self.ui.actionStop_Key_Record.setDisabled(True)
        mrWinHookThread.StopKeyCallBack(self)
    
    def StopHookWinMouseCallBack(self):
        self.ui.actionRun_Mouse_Record.setEnabled(True)
        self.ui.actionStop_Mouse_Record.setDisabled(True)
        mrWinHookThread.StopMouseCallBack(self)
    
    def CallBackExit(self):
        exit()
        
    """ --------------------------------------- Events -------------------------------------------------------------------"""
    def OnKeyboardEvent(self,event):
        tableKey = []
        tableKey.append([event.MessageName,event.Key,chr(event.Ascii),event.Time])
        print(tableKey)
        print "coucou"
        return True
    
    def OnMouseEvent(self,event):
        tableKey = []
        tableKey.append([event.MessageName,event.Position,event.Time])
        print(tableKey)
        print "coucou"
        return True

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)   
    win = mrCWin(sys.platform)
    app.exec_()
        
        