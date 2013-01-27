'''
Created on 27 oct. 2012

@author: Lois Aubree
'''
import time
import os
import sys
from ui import mrMainWindow
from mrFigureCanvas import mrFigureKey
from mrFigureCanvas import mrFigureMouse
from PyQt4 import QtGui,QtCore
from mrKeyboardGraphicsView import mrKeyboardGraphicsView
from mrClickGraphcisView import mrClickGraphicsView
import ctypes
import xlwt
from multiprocessing import Queue,Process,freeze_support

"""if sys.platform == "linux2":
    import mrLinuxHookThread
elif sys.platform == "win32": 
    import mrWinHookThread
else :
    print("OS not recognized")"""
from mrWinHookThread import *
    
class mrWindow(QtGui.QMainWindow):

    def __init__(self,platform):
        super(mrWindow,self).__init__()
        self.initUI(platform)
    
    def initUI(self,platform):
        self.ui = mrMainWindow.Ui_MainWindow()
        self.ui.setupUi(self)
        #self.setWindowIcon(QtGui.QIcon("../../res/icon/icon.png"))
        self.setWindowTitle("Rhythm'n'Games")
        self.tableKey = [["","",0]]
        self.tableMouse = []
        self.tableKeyStats = []
        self.startTime = 0
        self.refreshGraphTimer = QtCore.QTimer(self)
        self.refreshTimerLevel = 10000
        self.IsKeyRecord = False
        self.IsMouseRecord = False
        
        """ number global Stats """
        self.nbTotKeyPress = 0 
        self.nbTotKeyReleased = 0
        self.nbTotRightClic = 0
        self.nbTotLeftCLic = 0
        self.nbTotCilc = 0
        self.nbClicSec = 0
        self.nbKeySec = 0
        
        self.statusBarLabel = QtGui.QLabel("Hook is not running")
        
        self.q = Queue()
        self.event_Listener = WinHookListener(self.q)
        self.HookThread = WinHookThread(self.q)
        self.HookThread.dataReady.connect(self.on_hook_event)
        
        self.ui.statusbar.addWidget(self.statusBarLabel)
        self.trayIcon = QtGui.QSystemTrayIcon(QtGui.QIcon("image/icon/icon.png"), self)
        self.sysMenu = QtGui.QMenu()
        self.sysShowAction = QtGui.QAction("Show",self)
        self.sysQuitAction = QtGui.QAction("Quit",self)
        self.sysMenu.addAction(self.sysShowAction)
        self.sysMenu.addAction(self.sysQuitAction)
        
        
        """***************************  INPUTS TABLES **********************************"""
        self.tableKeyWigdet = QtGui.QTableWidget(self)
        list = QtCore.QStringList
        list = ["State", " Key "," Key Input ", " Time "]
        self.tableKeyWigdet.setColumnCount(4)
        self.tableKeyWigdet.setRowCount(0)
        self.tableKeyWigdet.setHorizontalHeaderLabels(list)
        self.ui.KeyTabLayout.addWidget(self.tableKeyWigdet)
        
        self.tableMouseWidget = QtGui.QTableWidget(self)
        list = ["State", " Time "]
        self.tableMouseWidget.setColumnCount(2)
        self.tableMouseWidget.setRowCount(0)
        self.tableMouseWidget.setHorizontalHeaderLabels(list)
        self.ui.MouseTabLayout.addWidget(self.tableMouseWidget)
        
        """*********************** Key Stats Window ****************************"""
        self.winKeyStats = QtGui.QMdiSubWindow(self)
        self.winKeyStats.setWindowTitle(" Key Stats ")
        self.tableKeyStatsWidget = QtGui.QTableWidget(self)
        list = ["Key", "count"]
        self.tableKeyStatsWidget.setColumnCount(2)
        self.tableKeyStatsWidget.setRowCount(0)
        self.tableKeyStatsWidget.setHorizontalHeaderLabels(list)
        self.winKeyStats.setWidget(self.tableKeyStatsWidget)
        self.winKeyStats.show()
        
        """"********************** Graphics Windows ****************************"""
        self.winMouseGraph = QtGui.QMdiSubWindow(self)
        self.winMouseGraph.setWindowTitle(" Mouse frequence graphic ")
        self.figureMouse = mrFigureMouse(self)
        
        self.winKeyGraph = QtGui.QMdiSubWindow(self)
        self.winKeyGraph.setWindowTitle(" Key frequence graphic ")
        self.figureKey = mrFigureKey(self)
        
        self.winKeyGraph.setWidget(self.figureKey)
        self.winMouseGraph.setWidget(self.figureMouse)  
        self.winKeyGraph.show()
        self.winMouseGraph.show()
        
        """********************* Click distribution Window *************************"""
        
        self.winClickDistrib = QtGui.QMdiSubWindow(self)
        self.winClickDistrib.setWindowTitle(" Click distribution ")
        self.distribClickView = mrClickGraphicsView()
        self.winClickDistrib.setWidget(self.distribClickView)
        self.distribClickView.show()
        self.winClickDistrib.show()
        
        """******************* Keyboard distribution Window **************************"""
        
        self.winKeyDistrib = QtGui.QMdiSubWindow(self)
        self.winKeyDistrib.setWindowTitle(" Keyboard distribution")
        self.distribKeyView = mrKeyboardGraphicsView()
        self.winKeyDistrib.setWidget(self.distribKeyView)
        self.distribKeyView.show()
        self.winKeyDistrib.show()
        
        self.ui.mdiArea.addSubWindow(self.winMouseGraph)
        self.ui.mdiArea.addSubWindow(self.winKeyGraph)
        self.ui.mdiArea.addSubWindow(self.winKeyStats)
        self.ui.mdiArea.addSubWindow(self.winClickDistrib)
        self.ui.mdiArea.addSubWindow(self.winKeyDistrib)
        
        
        """if sys.platform == "linux2":
            self.HookThread = mrLinuxHookThread.LinuxHookThread()
        elif sys.platform == "win32":"""
              
        self.connect(self.ui.actionRun_All_Record, QtCore.SIGNAL('triggered()'),self.RunHookAllCallBack)
        self.connect(self.ui.actionRun_Key_Record, QtCore.SIGNAL('triggered()'),self.RunHookKeyCallBack)
        self.connect(self.ui.actionRun_Mouse_Record, QtCore.SIGNAL('triggered()'),self.RunHookMouseCallBack)
        self.connect(self.ui.actionStop_All_Record, QtCore.SIGNAL('triggered()'),self.StopHookAllCallBack)
        self.connect(self.ui.actionStop_Key_Record, QtCore.SIGNAL('triggered()'),self.StopHookKeyCallBack)
        self.connect(self.ui.actionStop_Mouse_Record, QtCore.SIGNAL('triggered()'),self.StopHookMouseCallBack)
        
        self.connect(self.ui.actionQuit,QtCore.SIGNAL('triggered()'),self.close)
        self.connect(self.ui.actionOpen,QtCore.SIGNAL('triggered()'),self.openFile)
        self.connect(self.ui.actionSave, QtCore.SIGNAL('triggered()'),self.saveFile)
        self.connect(self.ui.actionAbout_Me,QtCore.SIGNAL('triggered()'),self.openAbout)
        self.connect(self.ui.actionVersion,QtCore.SIGNAL('triggered()'),self.openVersion)
        self.connect(self.ui.actionClick_Distribution,QtCore.SIGNAL('triggered()'),self.openCLickDistrib)
        self.connect(self.ui.actionKeyboard_frequency_graph,QtCore.SIGNAL('triggered()'),self.openWinKeyGraph)
        self.connect(self.ui.actionMouse_frequency_graph,QtCore.SIGNAL('triggered()'),self.openWinMouseGraph)
        self.connect(self.ui.actionKeyboard_Stats, QtCore.SIGNAL('triggered()'),self.openWinKeyStats)
        self.connect(self.ui.actionReset_Inputs, QtCore.SIGNAL('triggered()'),self.resetAllInputs)
        
        self.connect(self.sysQuitAction,QtCore.SIGNAL('triggered()'),self.closeApplicaton)
        self.connect(self.sysShowAction,QtCore.SIGNAL('triggered()'),self.showApplication)
        
        self.connect(self.refreshGraphTimer, QtCore.SIGNAL('timeout()'),self.updateSecValues)
    
    
    def on_hook_event(self,event):
        
        if(self.IsKeyRecord == True and (event.MessageName == "key up" or event.MessageName == "key down")):
            if (event.MessageName != self.tableKey[-1][0] or event.Key != self.tableKey[-1][1]):
                self.tableKey.append([event.MessageName,event.Key,chr(event.Ascii)])
                #print([event.MessageName,event.Key,chr(event.Ascii),event.Time])
                self.updateTableKey()
        elif(self.IsMouseRecord == True and (event.MessageName == 'mouse left down' or event.MessageName == 'mouse right down')):    
            self.tableMouse.append([event.MessageName])
            self.updateTableMouse()
            self.updateClicDistribution(event.Position)
        else:
            print([event.MessageName,event.Time])
        
    def updateSecValues(self):
        self.figureKey.update_figure(self.nbKeySec)
        self.figureMouse.update_figure(self.nbClicSec)
        self.nbKeySec = 0
        self.nbClicSec = 0
    
    def resetSecValues(self):
        self.figureKey.reset_figure()
        self.figureMouse.reset_figure() 
        
    def openWinMouse(self):
        self.winMouseGraph.show()
        self.tableMouseWidget.show()
        
    def openWinKey(self):
        self.winKeyGraph.show()
        self.tableKeyWigdet.show()
        
    def closeEvent(self,event):
        if not self.isHidden():
            event.ignore()
        self.hide()

        self.trayIcon.setContextMenu(self.sysMenu)
        self.trayIcon.show()
        self.trayIcon.showMessage("R'n'Games info","R'n'Games is still running in background !")
        
    def closeApplicaton(self):
        if self.event_Listener.is_alive():
            self.event_Listener.terminate()
        if self.HookThread.isRunning:
            self.HookThread.isRunning = False
            self.HookThread.wait()
        self.close()
        
    def showApplication(self):
        self.show()
        self.trayIcon.hide()
        
    def openWinKeyStats(self):
        if self.ui.actionKeyboard_Stats.isChecked():
            self.winKeyStats.show()
        else:
            self.winKeyStats.hide()
        
    def openWinKeyGraph(self):
        if self.ui.actionKeyboard_frequency_graph.isChecked():
            self.winKeyGraph.show()
        else:
            self.winKeyGraph.hide()
            
    def openWinMouseGraph(self):
        if self.ui.actionMouse_frequency_graph.isChecked():
            self.winMouseGraph.show()
        else:
            self.winMouseGraph.hide()
        
    def openCLickDistrib(self):
        if self.ui.actionClick_Distribution.isChecked():
            self.winClickDistrib.show()
        else:
            self.winClickDistrib.hide()
        
    def openFile(self):
        filename = QtGui.QFileDialog.getOpenFileName(self,"Open R'n'Game file","","*txt")
    
    def saveFile(self):
        filename = unicode(QtGui.QFileDialog.getSaveFileName(self,"Save R'n'Game file as ...","",".xls(*.xls)"))
        self.workBk = xlwt.Workbook()
        if self.tableKey != [["","",0]]:
            self.sheetKey = self.workBk.add_sheet("Key", cell_overwrite_ok=True)
            for rows in range(self.tableKeyWigdet.rowCount()):
                for cols in range(self.tableKeyWigdet.columnCount()):
                    try:
                        txt = str(self.tableKeyWigdet.item(rows, cols).text())
                        self.sheetKey.write(rows, cols, txt)
                    except AttributeError:
                            pass
        if self.tableKeyStats != []:
            self.sheetKeyStats = self.workBk.add_sheet("Key global", cell_overwrite_ok=True)
            for rows in range(self.tableKeyStatsWidget.rowCount()):
                for cols in range(self.tableKeyStatsWidget.columnCount()):
                    try:
                        txt = str(self.tableKeyStatsWidget.item(rows, cols).text())
                        self.sheetKeyStats.write(rows,cols, txt)
                    except AttributeError:
                            pass
        if self.tableMouse != []:
            self.sheetMouse = self.workBk.add_sheet("Mouse", cell_overwrite_ok=True)
            for rows in range(self.tableMouseWidget.rowCount()):
                for cols in range(self.tableMouseWidget.columnCount()):
                    try:
                        txt = str(self.tableMouseWidget.item(rows, cols).text())
                        self.sheetMouse.write(rows, cols, txt)
                    except AttributeError:
                            pass
        self.workBk.save(filename)
      
    def openAbout(self):
        msgBox = QtGui.QMessageBox(self)
        msgBox.setWindowTitle("About R'n'Game")
        msgBox.setText(" This program was created by Lois Aubree")
        msgBox.show()
        
    def openVersion(self):
        msgBox = QtGui.QMessageBox(self)
        if sys.platform == 'win32':
            msgBox.setWindowTitle("Version : v1.0a - Win32")
            msgBox.setText(" Version : v1.0a - Win32 \n This version is the alpha version \n\n If you encounter any problem, Please send me a report.  ")
        if sys.platform == "linux2":
            msgBox.setWindowTitle("Version : v1.0a - Linux")
            msgBox.setText(" Version : v1.0a - Linux \n This version is the alpha version \n\n If you encounter any problem, Please send me a report.  ")
        msgBox.show()
    
    def updateTableKey(self):
        self.tableKeyWigdet.setRowCount(self.tableKeyWigdet.rowCount()+1)
        
        item = QtGui.QTableWidgetItem(self.tableKey[-1][0])
        item.setFlags(QtCore.Qt.ItemIsEditable)
        self.tableKeyWigdet.setItem(self.tableKeyWigdet.rowCount()-1,0,item)
        
        item = QtGui.QTableWidgetItem(self.tableKey[-1][1])
        item.setFlags(QtCore.Qt.ItemIsEditable)
        self.tableKeyWigdet.setItem(self.tableKeyWigdet.rowCount()-1,1,item)
        
        item = QtGui.QTableWidgetItem(self.tableKey[-1][2])
        item.setFlags(QtCore.Qt.ItemIsEditable)
        self.tableKeyWigdet.setItem(self.tableKeyWigdet.rowCount()-1,2,item)
        
        item = QtGui.QTableWidgetItem(QtCore.QString.number(time.time()-self.startTime))
        item.setFlags(QtCore.Qt.ItemIsEditable)
        self.tableKeyWigdet.setItem(self.tableKeyWigdet.rowCount()-1,3,item)
        self.updateTableKeyStats()
        
    
    def updateTableMouse(self):
        self.tableMouseWidget.setRowCount(self.tableMouseWidget.rowCount()+1)        
        item = QtGui.QTableWidgetItem(self.tableMouse[-1][0])
        item.setFlags(QtCore.Qt.ItemIsEditable)
        self.tableMouseWidget.setItem(self.tableMouseWidget.rowCount()-1,0,item)
        item = QtGui.QTableWidgetItem(QtCore.QString.number(time.time()-self.startTime))
        item.setFlags(QtCore.Qt.ItemIsEditable)
        self.tableMouseWidget.setItem(self.tableMouseWidget.rowCount()-1,1,item)       
        self.updateTableMouseStats()
        
    def updateTableMouseStats(self):
        if self.tableMouse[-1][0] == 'mouse left down':
            self.nbTotLeftCLic += 1
            self.nbClicSec += 1
        if self.tableMouse[-1][0] == 'mouse right down':
            self.nbTotRightClic += 1 
            self.nbClicSec += 1     
        self.updateGlobalStats()
        
    
    def updateClicDistribution(self,position):
        if self.tableMouse[-1][0] == 'mouse left down' or self.tableMouse[-1][0] == 'mouse right down':
            self.distribClickView.updateClickView(position,self.nbTotCilc)
            
    def updateTableKeyStats(self):
        found = False
        if self.tableKey[-1][0] == 'key down':
            self.nbTotKeyPress += 1
            self.nbKeySec += 1
            for key in self.tableKeyStats:
                for i in key:
                    if i == self.tableKey[-1][1]:
                        key[1] +=1
                        items = self.tableKeyStatsWidget.findItems(i, QtCore.Qt.MatchExactly)
                        for it in items:
                            item = self.tableKeyStatsWidget.item(it.row(), it.column()+1)
                            newItem = QtGui.QTableWidgetItem(QtCore.QString.number(int(item.text())+1))
                            newItem.setFlags(QtCore.Qt.ItemIsEditable)
                            self.tableKeyStatsWidget.setItem(item.row(),item.column(),newItem)
                        found = True
            if found != True:
                self.tableKeyStats.append([self.tableKey[-1][1],1])
                
                self.tableKeyStatsWidget.setRowCount(self.tableKeyStatsWidget.rowCount()+1)
        
                item = QtGui.QTableWidgetItem(self.tableKeyStats[-1][0])
                item.setFlags(QtCore.Qt.ItemIsEditable)
                self.tableKeyStatsWidget.setItem(self.tableKeyStatsWidget.rowCount()-1,0,item)
                
                item = QtGui.QTableWidgetItem(QtCore.QString.number(self.tableKeyStats[-1][1]))
                item.setFlags(QtCore.Qt.ItemIsEditable)
                self.tableKeyStatsWidget.setItem(self.tableKeyStatsWidget.rowCount()-1,1,item)
                
        self.distribKeyView.updateKeyBoardView(self.tableKeyStats)
            
        if self.tableKey[-1][0] == 'key up':
            self.nbTotKeyReleased +=1
            
        self.updateGlobalStats()
    
    def updateGlobalStats(self):
        self.ui.TotKeyPressValue.setText(QtCore.QString.number(self.nbTotKeyPress))
        self.ui.TotKeyReleasedValue.setText(QtCore.QString.number(self.nbTotKeyReleased))
        self.ui.TotMouseLeftValue.setText(QtCore.QString.number(self.nbTotLeftCLic))
        self.ui.TotMouseRightValue.setText(QtCore.QString.number(self.nbTotRightClic))
        self.ui.TotMouseValue.setText(QtCore.QString.number(self.nbTotLeftCLic+self.nbTotRightClic))
               
    def resetAllInputs(self):
        self.tableKey = [["","",0]]
        self.tableMouse = []
        self.tableKeyStats = []
        self.nbClicSec = 0
        self.nbKeySec = 0
        self.nbTotCilc = 0
        self.nbTotKeyPress = 0
        self.nbTotKeyReleased = 0
        self.nbTotLeftCLic = 0
        self.nbTotRightClic = 0
        
        self.ui.KeyTabLayout.removeWidget(self.tableKeyWigdet)
        self.tableKeyWigdet.deleteLater()
        self.tableKeyWigdet = QtGui.QTableWidget(self)
        list = QtCore.QStringList
        list = ["State", " Key "," Key Input ", " Time "]
        self.tableKeyWigdet.setColumnCount(4)
        self.tableKeyWigdet.setRowCount(0)
        self.tableKeyWigdet.setHorizontalHeaderLabels(list)
        self.ui.KeyTabLayout.addWidget(self.tableKeyWigdet)
        
        self.ui.MouseTabLayout.removeWidget(self.tableMouseWidget)
        self.tableMouseWidget.deleteLater()
        self.tableMouseWidget = QtGui.QTableWidget(self)
        list = ["State", " Time "]
        self.tableMouseWidget.setColumnCount(2)
        self.tableMouseWidget.setRowCount(0)
        self.tableMouseWidget.setHorizontalHeaderLabels(list)
        self.ui.MouseTabLayout.addWidget(self.tableMouseWidget)
        
        self.tableKeyStatsWidget.deleteLater()
        self.tableKeyStatsWidget = QtGui.QTableWidget(self)
        list = ["Key", "count"]
        self.tableKeyStatsWidget.setColumnCount(2)
        self.tableKeyStatsWidget.setRowCount(0)
        self.tableKeyStatsWidget.setHorizontalHeaderLabels(list)
        self.winKeyStats.setWidget(self.tableKeyStatsWidget)
        
        self.distribClickView.reset()
        
        self.resetSecValues()
        self.update()
        
    """ ---------------------------------------- Menu actions CallBacks ----------------------------------------------------"""     
        
    def RunHookAllCallBack(self):
        self.IsKeyRecord = True
        self.IsMouseRecord = True
        self.updateMenuActions()
        self.event_Listener.start()   
        self.HookThread.start()
 
    def RunHookKeyCallBack(self):
        self.IsKeyRecord = True
        self.updateMenuActions()
        self.event_Listener.start()
        self.HookThread.start()
  
    def RunHookMouseCallBack(self):
        self.IsMouseRecord = True
        self.updateMenuActions()
        self.event_Listener.start()      
        self.HookThread.start()

    def StopHookAllCallBack(self):
        self.IsKeyRecord = False
        self.IsMouseRecord = False
        self.updateMenuActions()
        
    def StopHookKeyCallBack(self):
        self.IsKeyRecord = False
        self.updateMenuActions()
    
    def StopHookMouseCallBack(self):
        self.IsMouseRecord = False
        self.updateMenuActions()

    def updateMenuActions(self):
        if self.IsKeyRecord:
            self.ui.actionRun_Key_Record.setDisabled(True)
            self.ui.actionStop_Key_Record.setEnabled(True)
            if not(self.refreshGraphTimer.isActive()):
                self.refreshGraphTimer.start(self.refreshTimerLevel)
                self.startTime = time.time()
                self.statusBarLabel.setText("Hook is running")
                
        if self.IsMouseRecord:
            self.ui.actionRun_Mouse_Record.setDisabled(True)
            self.ui.actionStop_Mouse_Record.setEnabled(True)
            if not(self.refreshGraphTimer.isActive()):
                self.refreshGraphTimer.start(self.refreshTimerLevel)
                self.startTime = time.time()
                self.statusBarLabel.setText("Hook is running")
                
        if not(self.IsKeyRecord):
            self.ui.actionRun_Key_Record.setEnabled(True)
            self.ui.actionStop_Key_Record.setDisabled(True)
            
        if not(self.IsMouseRecord):
            self.ui.actionRun_Mouse_Record.setEnabled(True)
            self.ui.actionStop_Mouse_Record.setDisabled(True)
            
        if self.IsKeyRecord & self.IsMouseRecord:
            self.ui.actionRun_All_Record.setDisabled(True)
            self.ui.actionStop_All_Record.setEnabled(True)
            
        if not(self.IsKeyRecord | self.IsMouseRecord):
            self.statusBarLabel.setText("Hook is not running")
            self.ui.actionRun_All_Record.setEnabled(True)
            self.ui.actionStop_All_Record.setDisabled(True)
            self.startTime = 0
            self.HookThread.stop()
            self.refreshGraphTimer.stop()
        
        