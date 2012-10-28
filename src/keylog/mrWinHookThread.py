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

def OnMouseEvent(event):
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
    
    tableKey = []
    tableKey.append([event.MessageName,event.Position,event.Time])
    print(tableKey)
    # return True to pass the event to other handlers
    # return False to stop the event from propagating
    return True

def OnKeyboardEvent(event):
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
    
    tableKey = []
    tableKey.append([event.MessageName,event.Key,chr(event.Ascii),event.Time])
    print(tableKey)
    return True


class WinHookThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.is_alive = False
        timeF = time.time()
        self.hm = pyHook.HookManager()
        self.hm.KeyUp = OnKeyboardEvent
        self.hm.KeyDown = OnKeyboardEvent
        self.hm.MouseAllButtonsDown = OnMouseEvent
        self.hm.MouseAllButtonsUp = OnMouseEvent
    
    def run(self):
        print("Windows Distribution")
        self.hm.HookMouse()
        self.hm.HookKeyboard()
        pythoncom.PumpMessages()
        
    def stop(self):
        self.hm.UnhookMouse()
        self.hm.UnhookKeyboard()
        self.is_alive = False
    
    def isAlive(self):
        return self.is_alive
        
def RunKeyCallBack(self):
    if self.HookThread.isAlive():
        self.HookThread.stop()
    else:
        self.HookThread.run()