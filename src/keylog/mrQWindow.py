'''
Created on 27 oct. 2012

@author: Lois Aubree
'''
from PyQt4 import QtGui,QtCore
import time
import os
import sys
from ui import mrMainWindow


if sys.platform == "linux2":
    import mrLinuxHookThread
elif sys.platform == "win32": 
    import mrWinHookThread
else :
    print("OS not recognized")
class mrCWin(QtGui.QMainWindow):

    def __init__(self,platform):
        super(mrCWin,self).__init__()
        self.initUI(platform)
    
    def initUI(self,platform):
        self.ui = mrMainWindow.Ui_MainWindow()
        self.ui.setupUi(self)
        #self.setWindowIcon(QtGui.QIcon("../../res/icon/icon.png"))
        self.setWindowTitle(" Rythme'n'Game ")
        self.tableKey = []
        self.tableMouse = []
        
        self.winKey = QtGui.QMdiSubWindow(self)
        self.winKey.setWindowTitle(" Key Table ")
        self.tableKeyWigdet = QtGui.QTableWidget(self)
        list = QtCore.QStringList
        list = ["State", " Key "," Key Input ", " Time "]
        self.tableKeyWigdet.setColumnCount(4)
        self.tableKeyWigdet.setRowCount(0)
        self.tableKeyWigdet.setHorizontalHeaderLabels(list)
        self.winKey.setWidget(self.tableKeyWigdet)
        
        self.winMouse = QtGui.QMdiSubWindow(self)
        self.winMouse.setWindowTitle(" Mouse Table ")
        self.tableMouseWidget = QtGui.QTableWidget(self)
        list = ["State", " Time "]
        self.tableMouseWidget.setColumnCount(2)
        self.tableMouseWidget.setRowCount(0)
        self.tableMouseWidget.setHorizontalHeaderLabels(list)
        self.winMouse.setWidget(self.tableMouseWidget)
        
        self.winKey.show()
        self.winMouse.show()
        
        self.ui.mdiArea.addSubWindow(self.winMouse)
        self.ui.mdiArea.addSubWindow(self.winKey)
        
        if platform == "linux2":
            self.HookThread = mrLinuxHookThread.LinuxHookThread()
            self.connect(self.ui.actionRun_All_Record, QtCore.SIGNAL('triggered()'),self.RunHookLinuxAllCallBack)
            self.connect(self.ui.actionRun_Key_Record, QtCore.SIGNAL('triggered()'),self.RunHookLinuxKeyCallBack)
            self.connect(self.ui.actionRun_Mouse_Record, QtCore.SIGNAL('triggered()'),self.RunHookLinuxMouseCallBack)
            
            self.connect(self.ui.actionStop_All_Record, QtCore.SIGNAL('triggered()'),self.StopHookLinuxAllCallBack)
            self.connect(self.ui.actionStop_Key_Record, QtCore.SIGNAL('triggered()'),self.StopHookLinuxKeyCallBack)
            self.connect(self.ui.actionStop_Mouse_Record, QtCore.SIGNAL('triggered()'),self.StopHookLinuxMouseCallBack)
            
            
        elif platform == "win32":
            self.HookThread = mrWinHookThread.WinHookThread()
            self.connect(self.ui.actionRun_All_Record, QtCore.SIGNAL('triggered()'),self.RunHookWinAllCallBack)
            self.connect(self.ui.actionRun_Key_Record, QtCore.SIGNAL('triggered()'),self.RunHookWinKeyCallBack)
            self.connect(self.ui.actionRun_Mouse_Record, QtCore.SIGNAL('triggered()'),self.RunHookWinMouseCallBack)
            self.connect(self.HookThread, QtCore.SIGNAL('sendTableKey'),self.updateTableKey)
            self.connect(self.HookThread, QtCore.SIGNAL('sendTableMouse'),self.updateTableMouse)
            
            self.connect(self.ui.actionStop_All_Record, QtCore.SIGNAL('triggered()'),self.StopHookWinAllCallBack)
            self.connect(self.ui.actionStop_Key_Record, QtCore.SIGNAL('triggered()'),self.StopHookWinKeyCallBack)
            self.connect(self.ui.actionStop_Mouse_Record, QtCore.SIGNAL('triggered()'),self.StopHookWinMouseCallBack)

            
        self.connect(self, QtCore.SIGNAL('destroyed()'),self.closeApplication)
        self.connect(self.ui.actionQuit,QtCore.SIGNAL('triggered()'),self.closeApplication)
        self.connect(self.ui.actionOpen,QtCore.SIGNAL('triggered()'),self.openFile)
        self.connect(self.ui.actionSave, QtCore.SIGNAL('triggered()'),self.saveFile)
        self.connect(self.ui.actionAbout_Me,QtCore.SIGNAL('triggered()'),self.openAbout)
        self.connect(self.ui.actionVersion,QtCore.SIGNAL('triggered()'),self.openVersion)
        self.connect(self.ui.actionKeyboard_Table,QtCore.SIGNAL('triggered()'),self.openWinKey)
        self.connect(self.ui.actionMouse_Table,QtCore.SIGNAL('triggered()'),self.openMouseKey)
        self.connect(self.ui.actionReset_Inputs, QtCore.SIGNAL('triggered()'),self.resetAllInputs)
            
        self.show()
    
    def closeApplication(self):
        exit()
    
    def openMouseKey(self):
        self.winMouse.show()
        self.tableMouseWidget.show()
        
    def openWinKey(self):
        self.winKey.show()
        self.tableKeyWigdet.show()
        
    def openFile(self):
        filename = QtGui.QFileDialog.getOpenFileName(self,"Open R'n'Game file","","*txt")
    
    def saveFile(self):
        filename = QtGui.QFileDialog.getSaveFileName(self,"Save R'n'Game file as ...","","*.txt")
        
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
    
    def updateTableKey(self,tbKey):
        self.tableKey = tbKey
        self.tableKeyWigdet.setRowCount(self.tableKeyWigdet.rowCount()+1)
        
        item = QtGui.QTableWidgetItem(tbKey[-1][0])
        item.setFlags(QtCore.Qt.ItemIsEditable)
        self.tableKeyWigdet.setItem(self.tableKeyWigdet.rowCount()-1,0,item)
        
        item = QtGui.QTableWidgetItem(tbKey[-1][1])
        item.setFlags(QtCore.Qt.ItemIsEditable)
        self.tableKeyWigdet.setItem(self.tableKeyWigdet.rowCount()-1,1,item)
        
        item = QtGui.QTableWidgetItem(tbKey[-1][2])
        item.setFlags(QtCore.Qt.ItemIsEditable)
        self.tableKeyWigdet.setItem(self.tableKeyWigdet.rowCount()-1,2,item)
        
        item = QtGui.QTableWidgetItem(QtCore.QString.number(tbKey[-1][3]))
        item.setFlags(QtCore.Qt.ItemIsEditable)
        self.tableKeyWigdet.setItem(self.tableKeyWigdet.rowCount()-1,3,item)
        
    
    def updateTableMouse(self,tbMouse):
        self.tableMouse = tbMouse
        self.tableMouseWidget.setRowCount(self.tableMouseWidget.rowCount()+1)
        item = QtGui.QTableWidgetItem(tbMouse[-1][0])
        item.setFlags(QtCore.Qt.ItemIsEditable)
        self.tableMouseWidget.setItem(self.tableMouseWidget.rowCount()-1,0,item)
        item = QtGui.QTableWidgetItem(QtCore.QString.number(tbMouse[-1][1]))
        item.setFlags(QtCore.Qt.ItemIsEditable)
        self.tableMouseWidget.setItem(self.tableMouseWidget.rowCount()-1,1,item)
        
    def resetAllInputs(self):
        self.tableKey = []
        self.tableMouse = []
        
        self.tableKeyWigdet = QtGui.QTableWidget(self)
        list = QtCore.QStringList
        list = ["State", " Key "," Key Input ", " Time "]
        self.tableKeyWigdet.setColumnCount(4)
        self.tableKeyWigdet.setRowCount(0)
        self.tableKeyWigdet.setHorizontalHeaderLabels(list)
        self.winKey.setWidget(self.tableKeyWigdet)
        
        self.tableMouseWidget = QtGui.QTableWidget(self)
        list = ["State", " Time "]
        self.tableMouseWidget.setColumnCount(2)
        self.tableMouseWidget.setRowCount(0)
        self.tableMouseWidget.setHorizontalHeaderLabels(list)
        self.winMouse.setWidget(self.tableMouseWidget)
        
        
    """ ---------------------------------------- Linux CallBacks ----------------------------------------------------"""     
        
    def RunHookLinuxAllCallBack(self):
        self.ui.actionRun_All_Record.setDisabled(True)
        self.ui.actionRun_Key_Record.setDisabled(True)
        self.ui.actionRun_Mouse_Record.setDisabled(True)
        self.ui.actionStop_All_Record.setEnabled(True)
        self.ui.actionStop_Key_Record.setEnabled(True)
        self.ui.actionStop_Mouse_Record.setEnabled(True)
        mrLinuxHookThread.RunAllCallBack(self)
    
    def RunHookLinuxKeyCallBack(self):
        self.ui.actionRun_Key_Record.setDisabled(True)
        self.ui.actionStop_Key_Record.setEnabled(True)
        mrLinuxHookThread.RunKeyCallBack(self)
    
    def RunHookLinuxMouseCallBack(self):
        self.ui.actionRun_Mouse_Record.setDisabled(True)
        self.ui.actionStop_Mouse_Record.setEnabled(True)
        mrLinuxHookThread.RunMouseCallBack(self)
    
    
    def StopHookLinuxAllCallBack(self):
        self.ui.actionRun_All_Record.setEnabled(True)
        self.ui.actionRun_Key_Record.setEnabled(True)
        self.ui.actionRun_Mouse_Record.setEnabled(True)
        self.ui.actionStop_All_Record.setDisabled(True)
        self.ui.actionStop_Key_Record.setDisabled(True)
        self.ui.actionStop_Mouse_Record.setDisabled(True)
        mrLinuxHookThread.StopAllCallBack(self)
    
    def StopHookLinuxKeyCallBack(self):
        self.ui.actionRun_Key_Record.setEnabled(True)
        self.ui.actionStop_Key_Record.setDisabled(True)
        mrLinuxHookThread.StopKeyCallBack(self)

    def StopHookLinuxMouseCallBack(self):
        self.ui.actionRun_Mouse_Record.setEnabled(True)
        self.ui.actionStop_Mouse_Record.setDisabled(True)
        mrLinuxHookThread.StopMouseCallBack(self)

    """ ---------------------------------------- Win CallBacks ----------------------------------------------------"""
        
    def RunHookWinAllCallBack(self):
        self.ui.actionRun_All_Record.setDisabled(True)
        self.ui.actionRun_Key_Record.setDisabled(True)
        self.ui.actionRun_Mouse_Record.setDisabled(True)
        self.ui.actionStop_All_Record.setEnabled(True)
        self.ui.actionStop_Key_Record.setEnabled(True)
        self.ui.actionStop_Mouse_Record.setEnabled(True)
        mrWinHookThread.RunAllCallBack(self)
        
    def RunHookWinKeyCallBack(self):
        self.ui.actionRun_Key_Record.setDisabled(True)
        self.ui.actionStop_Key_Record.setEnabled(True)
        mrWinHookThread.RunKeyCallBack(self)
    
    def RunHookWinMouseCallBack(self):
        self.ui.actionRun_Mouse_Record.setDisabled(True)
        self.ui.actionStop_Mouse_Record.setEnabled(True)
        mrWinHookThread.RunMouseCallBack(self)
    
    def StopHookWinAllCallBack(self):
        self.ui.actionRun_All_Record.setEnabled(True)
        self.ui.actionRun_Key_Record.setEnabled(True)
        self.ui.actionRun_Mouse_Record.setEnabled(True)
        self.ui.actionStop_All_Record.setDisabled(True)
        self.ui.actionStop_Key_Record.setDisabled(True)
        self.ui.actionStop_Mouse_Record.setDisabled(True)
        mrWinHookThread.StopAllCallBack(self)
        
    def StopHookWinKeyCallBack(self):
        self.ui.actionRun_Key_Record.setEnabled(True)
        self.ui.actionStop_Key_Record.setDisabled(True)
        mrWinHookThread.StopKeyCallBack(self)
    
    def StopHookWinMouseCallBack(self):
        self.ui.actionRun_Mouse_Record.setEnabled(True)
        self.ui.actionStop_Mouse_Record.setDisabled(True)
        mrWinHookThread.StopMouseCallBack(self)
    

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)   
    win = mrCWin(sys.platform)
    app.exec_()
        
        