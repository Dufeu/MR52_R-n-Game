from pyxhook import *

hm = HookManager()
hm.HookKeyboard()
hm.HookMouse()
hm.KeyDown = hm.printevent
hm.KeyUp = hm.printevent
hm.MouseAllButtonsDown = hm.printevent
hm.MouseAllButtonsUp = hm.printevent
hm.start()
time.sleep(10)
hm.cancel() 