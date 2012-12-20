'''
Created on 28 oct. 2012

@author: Lois Aubree
'''

  
"""import py2exe
from distutils.core import setup
import matplotlib


includes = ['sip','PyQt4.QtCore','PyQt4.QtGui','src','ui','pylab','matplotlib.backends.backend_qt4agg',
                      'matplotlib.figure','pyHook','numpy.numarray']

excludes = [ 'matplotlib.backends.backend_tkagg','_gtkagg' , '_tkagg' , 'curses', 'email', 'pywin.debugger',
        'pywin.debugger.dbgcon', 'pywin.dialogs', 'tcl',
        'Tkconstants', 'Tkinter']

dll_excludes = ['libgdk-win32-2.0-0.dll', 'libgobject-2.0-0.dll', 'tcl85.dll','tk85.dll']
 
setup(windows=[{ 'script' : "MR52_R-n-Game.py",
                'icon_ressource': [(1,'image/icon/icon.png')]}],
      name='R\'n\'Game',
      version='1.0.0',
      author='Aubree Lois',
      options={ 'py2exe': { 
        'compressed' : 2, 
        'optimize' : 2,
        'includes' : includes,
        'excludes' : excludes,
        'dll_excludes' : dll_excludes}},
      data_files=matplotlib.get_py2exe_datafiles())"""
      
from cx_Freeze import setup, Executable

includes = []
excludes = ['_gtkagg', '_tkagg', 'bsddb', 'curses', 'email', 'pywin.debugger',
             'pywin.debugger.dbgcon', 'pywin.dialogs', 'tcl','Tkconstants', 'Tkinter']

include_files = ['image/keyboard.png','image/icon/icon.png']

setup(
    name = "R'n'Game.exe",
    version = "0.1",
    description = "R'n'Game",
    author = "Lois Aubree",
    options = {"build_exe" : {"includes" : includes,
                               "excludes" : excludes,
                               "include_files" : include_files,
                               "packages" : [],
                               "path" : []}},
    executables = [Executable("MR52_R-n-Game.py", base = "Win32GUI" , icon = 'image/icon/icon.ico',targetName="R'n'Game.exe")])
      
      

