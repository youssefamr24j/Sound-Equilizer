# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'YourSignal.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from pyqtgraph import PlotWidget

class Ui_YourSignalWindow(object):
    def __init__(self,data):
        self.data=data
    def setupUi(self, YourSignalWindow):
        YourSignalWindow.setObjectName("YourSignalWindow")
        YourSignalWindow.resize(888, 658)
        self.centralwidget = QtWidgets.QWidget(YourSignalWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.graphicsView = PlotWidget(self.centralwidget)
        self.graphicsView.setObjectName("graphicsView")
        self.gridLayout.addWidget(self.graphicsView, 0, 0, 1, 1)
        YourSignalWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(YourSignalWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 888, 25))
        self.menubar.setObjectName("menubar")
        YourSignalWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(YourSignalWindow)
        self.statusbar.setObjectName("statusbar")
        YourSignalWindow.setStatusBar(self.statusbar)

        self.retranslateUi(YourSignalWindow)
        QtCore.QMetaObject.connectSlotsByName(YourSignalWindow)

    def retranslateUi(self, YourSignalWindow):
        _translate = QtCore.QCoreApplication.translate
        YourSignalWindow.setWindowTitle(_translate("YourSignalWindow", "YourSignalWindow"))
        self.DrawOriginalSiganal()



    def DrawOriginalSiganal(self):
        self.graphicsView.plot(self.data)


