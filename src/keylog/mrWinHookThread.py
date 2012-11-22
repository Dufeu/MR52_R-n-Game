'''
Created on 28 oct. 2012

@author: Lois Aubree 

This thread is called by the mrQWindow when the recognized OS is Windows
'''
import sys
import pyHook
import thread
import threading
import pythoncom
import time
from PyQt4 import QtCore,QtGui


class WinHookThread(QtCore.QThread):
    def __init__(self):
        QtCore.QThread.__init__(self)
        self.is_Key_alive = False
        self.is_Mouse_alive = False
        self.hm = pyHook.HookManager()
        self.hm.KeyUp = self.OnKeyboardEvent
        self.hm.KeyDown = self.OnKeyboardEvent
        self.hm.MouseAllButtonsDown = self.OnMouseEvent
        self.hm.MouseAllButtonsUp = self.OnMouseEvent
        self.tableKey = [["","",0,0]]
        self.tableMouse = []
    
    def runAll(self):
        self.hm.HookMouse()
        self.hm.HookKeyboard()
        self.is_Key_alive = True
        self.is_Mouse_alive = True
        pythoncom.PumpMessages()
    
    def runKey(self):
        self.hm.HookKeyboard()
        self.is_Key_alive = True
        pythoncom.PumpMessages()
    
    def runMouse(self):
        self.hm.HookMouse()
        self.is_Mouse_alive = True
        pythoncom.PumpMessages()
        
        
    def stop(self):
        self.hm.UnhookMouse()
        self.hm.UnhookKeyboard()
        self.is_Key_alive = False
        self.is_Mouse_alive = False
    
    def stopKey(self):
        self.hm.UnhookKeyboard()
        self.is_Key_alive = False
    
    def stopMouse(self):
        self.hm.UnhookMouse()
        self.is_Mouse_alive = False
    
    def isAliveKey(self):
        return self.is_Key_alive
    
    def isAliveMouse(self):
        return self.is_Mouse_alive
    
    def setOnkeyBoardEvent(self,func):
        self.hm.KeyUp = func
        self.hm.KeyDown = func
    
    def setOnkeyMouseEvent(self,func):
        self.hm.MouseAllButtonsUp = func
        self.hm.MouseAllButtonsDown = func
        
    def OnMouseEvent(self,event):
        '''
        print('MessageName:',event.MessageName)
        print('Message:',event.Message)
        print('Time:',event.Time)
        print('Window:',event.Window)
        print('WindowName:',event.WindowName)
        print('Position:',event.Position)
        print('Wheel:',event.Wheel)
        print('Injected:',event.Injected)
        print('---')
        '''
        self.tableMouse.append([event.MessageName,event.Time])
        #print([event.MessageName,event.Position,event.Time])
        self.emit(QtCore.SIGNAL('sendTableMouse'),self.tableMouse)
        
        # return True to pass the event to other handlers
        # return False to stop the event from propagating
        return True

    def OnKeyboardEvent(self,event):
        '''
        print('MessageName:',event.MessageName)
        print('Message:',event.Message)
        print('Time:',event.Time)
        print('Window:',event.Window)
        print('WindowName:',event.WindowName)
        print('Ascii:', event.Ascii, chr(event.Ascii))
        print('Key:', event.Key)
        print('KeyID:', event.KeyID)
        print('ScanCode:', event.ScanCode)
        print('Extended:', event.Extended)
        print('Injected:', event.Injected)
        print('Alt', event.Alt)
        print('Transition', event.Transition)
        print('---')
        '''
        if (event.MessageName != self.tableKey[-1][0] or event.Key != self.tableKey[-1][1]):
            self.tableKey.append([event.MessageName,event.Key,chr(event.Ascii),event.Time])
            #print([event.MessageName,event.Key,chr(event.Ascii),event.Time])
            self.emit(QtCore.SIGNAL('sendTableKey'),self.tableKey)
        return True
        
def RunAllCallBack(self):
    if self.HookThread.isAliveKey() == False and self.HookThread.isAliveMouse() == False:
        self.HookThread.runAll()
    elif self.isAliveMouse() == True:
        self.HookThread.runKey()
    else:
        self.HookThread.runMouse()

def StopAllCallBack(self):
    self.HookThread.stop()
    
def RunKeyCallBack(self):
    assert(self.HookThread.isAliveKey() == False)
    self.HookThread.runKey()

def StopKeyCallBack(self):
    assert(self.HookThread.isAliveKey())
    self.HookThread.stopKey()
    
def RunMouseCallBack(self):
    assert(self.HookThread.isAliveMouse() == False)
    self.HookThread.runMouse()
    
def StopMouseCallBack(self):
    assert(self.HookThread.isAliveMouse())
    self.HookThread.stopMouse()