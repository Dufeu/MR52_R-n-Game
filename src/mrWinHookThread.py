'''
Created on 28 oct. 2012

@author: Lois Aubree 

This thread is called by the mrQWindow when the recognized OS is Windows
'''
import pyHook
from PySide.QtCore import Signal,QThread
import time
from pyHook.HookManager import HookManager, HookConstants
from multiprocessing import Process, Queue, freeze_support
import pythoncom

class WinHookListener(Process):
    def __init__(self,queue):
        super(WinHookListener,self).__init__()
        self.queue = queue
        
    def on_event(self,event):
        self.queue.put(event)
        return True
    
    def run(self):
        self.hm = HookManager()
        self.hm.SubscribeKeyAll(self.on_event)
        self.hm.SubscribeMouseAll(self.on_event)
        self.hm.HookMouse()
        self.hm.HookKeyboard()
        pythoncom.PumpMessages()
        self.hm.UnhookMouse()
        self.hm.UnhookKeyboard()
        
class WinHookThread(QThread):
    
    dataReady = Signal(object)
    
    def __init__(self,queue):
        super(WinHookThread,self).__init__()
        self.queue = queue
        self.isRunning  = True

    def run(self):
        self.isRunning  = True
        while self.isRunning:
            try:
                event = self.queue.get(timeout=1)
            except:
                pass
            else:
                self.dataReady.emit(event)
     
    def stop(self):
        self.isRunning = False