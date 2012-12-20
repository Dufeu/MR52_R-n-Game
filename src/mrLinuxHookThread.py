'''
Created on 28 oct. 2012

@author: Lois Aubree

This thread is called by the mrQWindow when the recognized OS is Windows

'''

import pyxhook
import thread
import threading
from PyQt4 import QtCore,QtGui

class LinuxHookThread(QtCore.QThread):
    def __init__(self):
        QtCore.QThread.__init__(self)
        self.is_Key_alive = False
        self.is_Mouse_alive = False
        self.hm = pyxhook.HookManager()
        self.hm.KeyDown = self.OnkeyboardEvent
        self.hm.KeyUp = self.OnkeyboardEvent
        self.hm.MouseAllButtonsDown = self.OnMouseEvent
        self.hm.MouseAllButtonsUp = self.OnMouseEvent
        self.tableKey = [["","",0,0]]
        self.tableMouse = []
        
    def runAll(self):
        self.hm.HookKeyboard()
        self.hm.HookMouse()
        self.hm.start()
        self.is_Key_alive = True
        self.is_Mouse_alive = True
        
    def runKey(self):
        self.hm.HookKeyboard()
        self.is_Key_alive = True
             
    def runMouse(self):
        self.hm.HookMouse()
        self.is_Mouse_alive = True
        
    def stop(self):
        self.hm.cancel()
        self.is_alive = False
        
    def stopKey(self):
        self.hm.cancel()
        self.is_Key_alive = False
        
    def stopMouse(self):
        self.hm.cancel()
        self.is_Mouse_alive = False
    
    def isAliveKey(self):
        return self.is_Key_alive
    
    def isAliveMouse(self):
        return self.is_Mouse_alive
    
    def OnkeyboardEvent(self,event):
        if (event.MessageName != self.tableKey[-1][0] or event.Key != self.tableKey[-1][1]):
            self.tableKey.append([event.MessageName,event.Key,chr(event.Ascii),0])
            #print([event.MessageName,event.Key,chr(event.Ascii),event.Time])
            self.emit(QtCore.SIGNAL('sendTableKey'),self.tableKey)
        return True
    
    def OnMouseEvent(self,event):
        self.tableMouse.append([event.MessageName,0])
        self.emit(QtCore.SIGNAL('sendTableMouse'),self.tableMouse)
        
        return True
    

    def RunAllCallBack(self):
        if self.isAliveKey() == False and self.isAliveMouse() == False:
            self.runAll()
        elif self.isAliveMouse() == True:
            self.runKey()
        else:
            self.runMouse()
    
    def StopAllCallBack(self):
        self.stop()
        
    def RunKeyCallBack(self):
        assert(self.isAliveKey() == False)
        self.runKey()
    
    def StopKeyCallBack(self):
        assert(self.isAliveKey())
        self.stopKey()
        
    def RunMouseCallBack(self):
        assert(self.isAliveMouse() == False)
        self.runMouse()
        
    def StopMouseCallBack(self):
        assert(self.isAliveMouse())
        self.stopMouse()