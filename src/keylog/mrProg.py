'''
Created on 27 oct. 2012

@author: Lois Aubree
'''

import Tkinter
import sys
import mrQWindow
import py2exe
from distutils.core import setup
from PyQt4  import QtCore,QtGui,Qt

"""top = Tkinter.Tk()
top.title("ma fenetre")
button = Tkinter.Button(top,text = "Run Keylogger",command = mrHook.RunKeyCallBack)
button.pack()
top.mainloop()"""

app = QtGui.QApplication(sys.argv)   
win = mrQWindow.mrCWin(sys.platform)
app.exec_()

"""setup(console =["hello world !"])"""