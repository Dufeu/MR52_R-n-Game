'''
Created on 23 nov. 2012

@author: Lois Aubree
'''
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class mrFigureCanvas(FigureCanvas):
    def __init__(self,parent=None,width=5,height=4,dpi=100):
        figure = Figure(figsize=(width,height),dpi=dpi)
        FigureCanvas.__init__(self,figure)
        self.setParent(parent)
        self.axes = figure.add_subplot(111)
        self.axes.hold(False)
        self.axeX = [0]
        
    def update_figure(self,nbSec):
        pass
    def reset_figure(self):
        pass
        


class mrFigureKey(mrFigureCanvas):
    def __init__(self,parent):
        mrFigureCanvas.__init__(self,parent)
        self.numSec = 0
        self.tableKeySec = [0]

    def update_figure(self,nbSec):
        self.numSec += 1
        self.tableKeySec.append(nbSec)
        self.axeX.append(self.numSec)
        self.axes.plot(self.axeX, self.tableKeySec)
        self.draw()
    
    def reset_figure(self):
        self.axes.plot(0,0)
        self.tableKeySec = [0]
        self.axeX = [0]
        self.draw()
        
        
class mrFigureMouse(mrFigureCanvas):
    def __init__(self,parent):
        mrFigureCanvas.__init__(self,parent)
        self.numSec = 0
        self.tableMouseSec = [0]

    def update_figure(self,nbSec):
        self.numSec += 1
        self.tableMouseSec.append(nbSec)
        self.axeX.append(self.numSec)
        self.axes.plot(self.axeX, self.tableMouseSec,'r')
        self.draw()
    def reset_figure(self):
        self.axes.plot(0,0)
        self.axeX = [0]
        self.tableMouseSec = [0]
        self.draw()

        