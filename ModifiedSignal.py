# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ModifiedSignal.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from pyqtgraph import PlotWidget
from SoundEquilizer2 import Ui_SoundEquilizer
from Final1 import Ui_FinalWindow

class Ui_ModifiedSignal(object):
    def __init__(self,data,output,rate):
        self.data=data
        self.output=output
        self.rate=rate
    def setupUi(self, ModifiedSignal):
        ModifiedSignal.setObjectName("ModifiedSignal")
        ModifiedSignal.resize(940, 754)
        self.centralwidget = QtWidgets.QWidget(ModifiedSignal)
        self.centralwidget.setObjectName("centralwidget")
        self.graphicsView = PlotWidget(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(30, 30, 881, 511))
        self.graphicsView.setObjectName("graphicsView")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(40, 580, 851, 101))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        ModifiedSignal.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ModifiedSignal)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 940, 25))
        self.menubar.setObjectName("menubar")
        ModifiedSignal.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ModifiedSignal)
        self.statusbar.setObjectName("statusbar")
        ModifiedSignal.setStatusBar(self.statusbar)

        self.retranslateUi(ModifiedSignal)
        QtCore.QMetaObject.connectSlotsByName(ModifiedSignal)

    def retranslateUi(self, ModifiedSignal):
        _translate = QtCore.QCoreApplication.translate
        ModifiedSignal.setWindowTitle(_translate("ModifiedSignal", "ModifiedSignal"))
        self.pushButton_2.setText(_translate("ModifiedSignal", "Compare"))
        self.pushButton.setText(_translate("ModifiedSignal", "Change IT AGAIN!!"))
        self.DrawModified()
        self.pushButton_2.clicked.connect(lambda:self.CompareOutput(ModifiedSignal))
        self.pushButton.clicked.connect(lambda:self.ChangeAgain(ModifiedSignal))


    def DrawModified(self):
        self.graphicsView.plot(self.output)

    def CompareOutput(self , ModifiedSignal):
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_FinalWindow(self.data,self.output,self.rate)
        self.ui.setupUi(self.window)
        ModifiedSignal.hide()
        self.window.show()

    def ChangeAgain(self , ModifiedSignal):
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_SoundEquilizer(self.data,self.output,self.rate)
        self.ui.setupUi(self.window)
        ModifiedSignal.hide()
        self.window.show()