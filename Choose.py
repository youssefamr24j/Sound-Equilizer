# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Choose.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from YourSignal import Ui_YourSignalWindow
from SoundEquilizer import Ui_SoundEquilizer


class Ui_ChooseWindow(object):
    def __init__(self,data,rate):
        self.data=data
        self.rate=rate
    def setupUi(self, ChooseWindow):
        ChooseWindow.setObjectName("ChooseWindow")
        ChooseWindow.resize(537, 354)
        self.centralwidget = QtWidgets.QWidget(ChooseWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(60, 50, 421, 201))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.View = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.View.setObjectName("View")
        self.verticalLayout.addWidget(self.View)
        self.Change = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.Change.setObjectName("Change")
        self.verticalLayout.addWidget(self.Change)
        ChooseWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ChooseWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 537, 25))
        self.menubar.setObjectName("menubar")
        ChooseWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ChooseWindow)
        self.statusbar.setObjectName("statusbar")
        ChooseWindow.setStatusBar(self.statusbar)

        

        self.retranslateUi(ChooseWindow)
        QtCore.QMetaObject.connectSlotsByName(ChooseWindow)

    def retranslateUi(self, ChooseWindow):
        _translate = QtCore.QCoreApplication.translate
        ChooseWindow.setWindowTitle(_translate("ChooseWindow", "ChooseWindow"))
        self.View.setText(_translate("ChooseWindow", "View Your Signal"))
        self.Change.setText(_translate("ChooseWindow", "Change IT !!"))
        self.View.clicked.connect(self.DisplaySignal)
        self.Change.clicked.connect(lambda:self.SoundEquilizer(ChooseWindow))




   

    def DisplaySignal(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_YourSignalWindow(self.data)
        self.ui.setupUi(self.window)
        self.window.show()  


    def SoundEquilizer(self ,ChooseWindow):
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_SoundEquilizer(self.data,self.rate)
        self.ui.setupUi(self.window)
        ChooseWindow.hide()
        self.window.show()