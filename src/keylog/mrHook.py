'''
Created on 27 oct. 2012

@author: lois aubree
'''

import os 
import sys
import thread
import threading

from mrFunctions import *
from PyQt4 import QtCore,QtGui

if sys.platform == "linux2":
    
        import pyxhook
        import time
        
elif sys.platform == "win32":

        import pyHook
        import time
        import pythoncom
        
else:
    print("Os not recognized")

class HookClassThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.is_alive = False
        if sys.platform == 'linux2':
            self.hm = pyxhook.HookManager()
            self.hm.KeyDown = self.hm.printevent
            self.hm.KeyUp = self.hm.printevent
            self.hm.MouseAllButtonsDown = self.hm.printevent
            self.hm.MouseAllButtonsUp = self.hm.printevent
        
        if sys.platform == 'win32':
            self.hm = pyHook.HookManager()
            self.hm.KeyUp = OnKeyboardEvent
            self.hm.KeyDown = OnKeyboardEvent
            self.hm.MouseAllButtonsDown = OnMouseEvent
            self.hm.MouseAllButtonsUp = OnMouseEvent
    
    def run(self):
        self.is_alive = True
        if sys.platform == 'win32':
            print("Windows Distribution")
            self.hm.HookMouse()
            self.hm.HookKeyboard()
            pythoncom.PumpMessages()
            
        elif sys.platform == 'linux2':
            print("Linux Distribution")
            self.hm.HookKeyboard()
            self.hm.HookMouse()
            self.hm.start()
        
        else :
            print("OS is not recognized by this program")
    
    def stop(self):
        if sys.platform == 'win32':
            self.hm.UnhookMouse()
            self.hm.UnhookKeyboard()
            
        elif sys.platform == 'linux2':
            self.hm.cancel()
        self.is_alive = False
            
    def isAlive(self):
        return self.is_alive
        
def RunKeyCallBack(self):
    if self.HookThread.isAlive():
        self.HookThread.stop()
    else:
        self.HookThread.run()
    