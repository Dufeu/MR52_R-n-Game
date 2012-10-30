# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mrMainWindow.ui'
#
# Created: Tue Oct 30 14:55:56 2012
#      by: PyQt4 UI code generator 4.9.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.scrollArea = QtGui.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 780, 539))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.gridLayout_2 = QtGui.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.textEdit = QtGui.QTextEdit(self.scrollAreaWidgetContents)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.gridLayout_2.addWidget(self.textEdit, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuRun = QtGui.QMenu(self.menubar)
        self.menuRun.setObjectName(_fromUtf8("menuRun"))
        self.menuStop = QtGui.QMenu(self.menubar)
        self.menuStop.setObjectName(_fromUtf8("menuStop"))
        self.menuAbout = QtGui.QMenu(self.menubar)
        self.menuAbout.setObjectName(_fromUtf8("menuAbout"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtGui.QAction(MainWindow)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        self.actionSave = QtGui.QAction(MainWindow)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        self.actionQuit = QtGui.QAction(MainWindow)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.actionRun_All_Record = QtGui.QAction(MainWindow)
        self.actionRun_All_Record.setObjectName(_fromUtf8("actionRun_All_Record"))
        self.actionRun_Key_Record = QtGui.QAction(MainWindow)
        self.actionRun_Key_Record.setObjectName(_fromUtf8("actionRun_Key_Record"))
        self.actionRun_Mouse_Record = QtGui.QAction(MainWindow)
        self.actionRun_Mouse_Record.setObjectName(_fromUtf8("actionRun_Mouse_Record"))
        self.actionStop_All_Record = QtGui.QAction(MainWindow)
        self.actionStop_All_Record.setEnabled(False)
        self.actionStop_All_Record.setObjectName(_fromUtf8("actionStop_All_Record"))
        self.actionStop_Key_Record = QtGui.QAction(MainWindow)
        self.actionStop_Key_Record.setEnabled(False)
        self.actionStop_Key_Record.setObjectName(_fromUtf8("actionStop_Key_Record"))
        self.actionStop_Mouse_Record = QtGui.QAction(MainWindow)
        self.actionStop_Mouse_Record.setEnabled(False)
        self.actionStop_Mouse_Record.setObjectName(_fromUtf8("actionStop_Mouse_Record"))
        self.actionAbout_Me = QtGui.QAction(MainWindow)
        self.actionAbout_Me.setObjectName(_fromUtf8("actionAbout_Me"))
        self.actionVersion = QtGui.QAction(MainWindow)
        self.actionVersion.setObjectName(_fromUtf8("actionVersion"))
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menuRun.addAction(self.actionRun_All_Record)
        self.menuRun.addSeparator()
        self.menuRun.addAction(self.actionRun_Key_Record)
        self.menuRun.addAction(self.actionRun_Mouse_Record)
        self.menuStop.addAction(self.actionStop_All_Record)
        self.menuStop.addSeparator()
        self.menuStop.addAction(self.actionStop_Key_Record)
        self.menuStop.addAction(self.actionStop_Mouse_Record)
        self.menuAbout.addAction(self.actionAbout_Me)
        self.menuAbout.addAction(self.actionVersion)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuRun.menuAction())
        self.menubar.addAction(self.menuStop.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuRun.setTitle(QtGui.QApplication.translate("MainWindow", "Run", None, QtGui.QApplication.UnicodeUTF8))
        self.menuStop.setTitle(QtGui.QApplication.translate("MainWindow", "Stop", None, QtGui.QApplication.UnicodeUTF8))
        self.menuAbout.setTitle(QtGui.QApplication.translate("MainWindow", "About", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen.setText(QtGui.QApplication.translate("MainWindow", "Open", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave.setText(QtGui.QApplication.translate("MainWindow", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setText(QtGui.QApplication.translate("MainWindow", "Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRun_All_Record.setText(QtGui.QApplication.translate("MainWindow", "Run All Record", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRun_Key_Record.setText(QtGui.QApplication.translate("MainWindow", "Run Key Record", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRun_Mouse_Record.setText(QtGui.QApplication.translate("MainWindow", "Run Mouse Record", None, QtGui.QApplication.UnicodeUTF8))
        self.actionStop_All_Record.setText(QtGui.QApplication.translate("MainWindow", "Stop All Record", None, QtGui.QApplication.UnicodeUTF8))
        self.actionStop_Key_Record.setText(QtGui.QApplication.translate("MainWindow", "Stop Key Record", None, QtGui.QApplication.UnicodeUTF8))
        self.actionStop_Mouse_Record.setText(QtGui.QApplication.translate("MainWindow", "Stop Mouse Record", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout_Me.setText(QtGui.QApplication.translate("MainWindow", "About Me", None, QtGui.QApplication.UnicodeUTF8))
        self.actionVersion.setText(QtGui.QApplication.translate("MainWindow", "Version", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

