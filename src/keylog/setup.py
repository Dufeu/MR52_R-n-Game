'''
Created on 28 oct. 2012

@author: Lois Aubree
'''

  
import py2exe
from distutils.core import setup

from glob import glob
data_files = [("Microsoft.VC90.CRT", glob(r'C:\Program Files\Microsoft Visual Studio 9.0\VC\redist\x86\Microsoft.VC90.CRT\*.*'))]
setup(data_files=data_files)
setup(console=['mrProg.py'])

