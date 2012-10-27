
'''
Created on 27 oct. 2012

@author: Lois Aubree
'''

import os 
from functions import *

if __name__ == "__main__":

    if os.name == "posix":
    
        import pyxhook
        import time
        
        print("Linux Distribution")
        
        hm = pyxhook.HookManager()
        hm.HookKeyboard()
        hm.HookMouse()
        hm.KeyDown = hm.printevent
        hm.KeyUp = hm.printevent
        hm.MouseAllButtonsDown = hm.printevent
        hm.MouseAllButtonsUp = hm.printevent
        hm.start()
        time.sleep(10)
        hm.cancel() 
        
    elif os.name == "nt":
        
        import pyHook
        import time
        import pythoncom
        
        print("Windows Distribution")
        
        hm = pyHook.HookManager()
        hm.KeyDown = OnKeyboardEvent
        hm.MouseAllButtonsDown = OnMouseEvent
        hm.MouseAllButtonsUp = OnMouseEvent
        
        hm.HookMouse()
        hm.HookKeyboard()
        
        pythoncom.PumpMessages()
        
    else:
        print("OS is not recognized by this program")