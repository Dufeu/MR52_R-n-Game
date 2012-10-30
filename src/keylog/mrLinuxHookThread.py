'''
Created on 28 oct. 2012

@author: Lois Aubree

This thread is called by the mrQWindow when the recognized OS is Windows

'''

import pyxhook
import thread
import threading

class LinuxHookThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.is_alive = False
        self.hm = pyxhook.HookManager()
        self.hm.KeyDown = self.hm.printevent
        self.hm.KeyUp = self.hm.printevent
        self.hm.MouseAllButtonsDown = self.hm.printevent
        self.hm.MouseAllButtonsUp = self.hm.printevent
        
    def run(self):
        self.is_alive = True
        self.hm.HookKeyboard()
        self.hm.HookMouse()
        self.hm.start()
        
    def stop(self):
        self.hm.cancel()
        self.is_alive = False
    
    def isAlive(self):
        return self.is_alive

def RunAllCallBack(self):
    assert(self.HookThread.isAlive()==False)
    self.HookThread.runAll()

def StopAllCallBack(self):
    assert(self.HookThread.isAlive()==True)
    self.HookThread.stop()
    
def RunKeyCallBack(self):
    pass

def StopKeyCallBack(self):
    pass
    
def RunMouseCallBack(self):
    pass
    
def StopMouseCallBack(self):
    pass