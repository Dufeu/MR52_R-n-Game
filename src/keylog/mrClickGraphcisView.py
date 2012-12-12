'''
Created on 10 dec. 2012

@author: lois Aubree
'''
from PyQt4 import QtGui,QtCore

class mrClickGraphicsView (QtGui.QGraphicsView):
    def __init__(self):
        QtGui.QGraphicsView.__init__(self)
        self.clickScene = QtGui.QGraphicsScene(self)
        self.setScene(self.clickScene)
        self.WIN_RESX = QtGui.QDesktopWidget().screenGeometry().width()
        self.WIN_RESY = QtGui.QDesktopWidget().screenGeometry().height()
        self.nbDivWidth = 40
        self.nbDivHeight = 40
        self.RECT_WIDTH = QtGui.QDesktopWidget().screenGeometry().width()/float(self.nbDivWidth)
        self.RECT_HEIGHT = QtGui.QDesktopWidget().screenGeometry().height()/float(self.nbDivHeight)
        self.viewportRect = QtCore.QRectF(QtGui.QDesktopWidget().screenGeometry())
        self.scale(0.5,0.5)
        self.pen = QtGui.QPen(QtCore.Qt.NoPen)
        
        self.setSceneRect(self.viewportRect)
        self.clickScene.addRect(self.viewportRect)
        self.nbClickTotal = 0
        self.max = 0
        self.tableRect = []
        
        for  i in range(self.nbDivWidth):
            for j in range(self.nbDivHeight):
                tmp = QtCore.QRectF(i*self.RECT_WIDTH,j*self.RECT_HEIGHT,self.RECT_WIDTH,self.RECT_HEIGHT)
                self.tableRect.append([tmp,0])
                self.clickScene.addRect(tmp,self.pen)
    
    def updateClickView(self,position,clickTot):
        self.nbClickTotal = clickTot
        self.clickScene.clear()
         
        for rect in self.tableRect:
            if position[0] >= rect[0].x() and position[0] <= rect[0].x()+rect[0].width():
                if position[1] >= rect[0].y() and position[1] <= rect[0].y()+rect[0].height():
                    rect[1]+=1
            if rect[1] >= self.max:
                self.max = rect[1] 
        for rect in self.tableRect:
            brush = self.getBrushColor(rect[1],self.max)
            self.clickScene.addRect(rect[0], self.pen,brush);
        
        self.clickScene.setSceneRect(self.viewportRect)
        self.clickScene.addRect(self.viewportRect)
        
    def getBrushColor(self,value,max):
        color = (510*value)/max
        if color-255 > 0:
            blue = 255
            green = color-255
        else:
            blue = color
            green = 0  
        return QtGui.QBrush(QtGui.QColor(255,255-green,255-blue))
    
    def reset(self):
        
        self.setSceneRect(self.viewportRect)
        self.clickScene.addRect(self.viewportRect)
        self.max = 0
        
        for rect in self.tableRect:
            rect[1] = 0
        
        