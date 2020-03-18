# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Final2.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from pyqtgraph import PlotWidget
from pydub import AudioSegment
from pydub.playback import play

class Ui_FinalWindow(object):
    def __init__(self,data,output1,output2,rate):
        self.data=data
        self.output1=output1
        self.output2=output2
        self.rate=rate
    def setupUi(self, FinalWindow):
        FinalWindow.setObjectName("FinalWindow")
        FinalWindow.resize(1343, 916)
        self.centralwidget = QtWidgets.QWidget(FinalWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.PlaySecondOutput = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PlaySecondOutput.sizePolicy().hasHeightForWidth())
        self.PlaySecondOutput.setSizePolicy(sizePolicy)
        self.PlaySecondOutput.setObjectName("PlaySecondOutput")
        self.verticalLayout_2.addWidget(self.PlaySecondOutput)
        self.SaveSecondOutput = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SaveSecondOutput.sizePolicy().hasHeightForWidth())
        self.SaveSecondOutput.setSizePolicy(sizePolicy)
        self.SaveSecondOutput.setObjectName("SaveSecondOutput")
        self.verticalLayout_2.addWidget(self.SaveSecondOutput)
        self.gridLayout.addLayout(self.verticalLayout_2, 3, 1, 1, 1)
        self.ViewSecondOutput = PlotWidget(self.centralwidget)
        self.ViewSecondOutput.setObjectName("ViewSecondOutput")
        self.gridLayout.addWidget(self.ViewSecondOutput, 3, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.PlayOriginal = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PlayOriginal.sizePolicy().hasHeightForWidth())
        self.PlayOriginal.setSizePolicy(sizePolicy)
        self.PlayOriginal.setObjectName("PlayOriginal")
        self.verticalLayout.addWidget(self.PlayOriginal)
        self.gridLayout.addLayout(self.verticalLayout, 0, 1, 1, 1)
        self.ViewFirstOutput = PlotWidget(self.centralwidget)
        self.ViewFirstOutput.setObjectName("ViewFirstOutput")
        self.gridLayout.addWidget(self.ViewFirstOutput, 2, 0, 1, 1)
        self.ViewOriginal = PlotWidget(self.centralwidget)
        self.ViewOriginal.setObjectName("ViewOriginal")
        self.gridLayout.addWidget(self.ViewOriginal, 0, 0, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.PlayFirstOutput = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PlayFirstOutput.sizePolicy().hasHeightForWidth())
        self.PlayFirstOutput.setSizePolicy(sizePolicy)
        self.PlayFirstOutput.setObjectName("PlayFirstOutput")
        self.verticalLayout_3.addWidget(self.PlayFirstOutput)
        self.SaveFirstOutput = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SaveFirstOutput.sizePolicy().hasHeightForWidth())
        self.SaveFirstOutput.setSizePolicy(sizePolicy)
        self.SaveFirstOutput.setObjectName("SaveFirstOutput")
        self.verticalLayout_3.addWidget(self.SaveFirstOutput)
        self.gridLayout.addLayout(self.verticalLayout_3, 2, 1, 1, 1)
        self.PlayAll = QtWidgets.QPushButton(self.centralwidget)
        self.PlayAll.setObjectName("PlayAll")
        self.gridLayout.addWidget(self.PlayAll, 4, 0, 1, 2)
        FinalWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(FinalWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1343, 25))
        self.menubar.setObjectName("menubar")
        FinalWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(FinalWindow)
        self.statusbar.setObjectName("statusbar")
        FinalWindow.setStatusBar(self.statusbar)

        # self.audio1
        # self.audio2
        # self.audio3

        self.retranslateUi(FinalWindow)
        QtCore.QMetaObject.connectSlotsByName(FinalWindow)

    def retranslateUi(self, FinalWindow):
        _translate = QtCore.QCoreApplication.translate
        FinalWindow.setWindowTitle(_translate("FinalWindow", "FinalWindow"))
        self.PlaySecondOutput.setText(_translate("FinalWindow", "Play"))
        self.SaveSecondOutput.setText(_translate("FinalWindow", "Save"))
        self.PlayOriginal.setText(_translate("FinalWindow", "Play"))
        self.PlayFirstOutput.setText(_translate("FinalWindow", "Play"))
        self.SaveFirstOutput.setText(_translate("FinalWindow", "Save"))
        self.PlayAll.setText(_translate("FinalWindow", "Play All"))
        self.ViewOriginal.plot(self.data)
        self.ViewFirstOutput.plot(self.output1)
        self.ViewSecondOutput.plot(self.output2)
        self.PlayOriginal.clicked.connect(self.PlayOriginalSong)
        self.PlayFirstOutput.clicked.connect(self.PlayFirstOutputSong)
        self.PlaySecondOutput.clicked.connect(self.PlaySecondOutputSong)
        self.PlayAll.clicked.connect(self.PlayAllSongs)
        self.SaveFirstOutput.clicked.connect(self.SaveFirstOutputSong)
        self.SaveSecondOutput.clicked.connect(self.SaveSecondOutputSong)


    def PlayOriginalSong(self):
        self.audio1 = AudioSegment(self.data.tobytes(),frame_rate=self.rate,sample_width=self.data.dtype.itemsize, channels=1)
        play(self.audio1) 

    def PlayFirstOutputSong(self):
        self.audio2 = AudioSegment(self.output1.tobytes(),frame_rate=self.rate,sample_width=self.data.dtype.itemsize, channels=1)
        play(self.audio2) 

    def PlaySecondOutputSong(self):
        self.audio3 = AudioSegment(self.output2.tobytes(),frame_rate=self.rate,sample_width=self.data.dtype.itemsize, channels=1)
        play(self.audio3) 

    def PlayAllSongs(self):
        self.audio1 = AudioSegment(self.data.tobytes(),frame_rate=self.rate,sample_width=self.data.dtype.itemsize, channels=1)
        self.audio2 = AudioSegment(self.output1.tobytes(),frame_rate=self.rate,sample_width=self.data.dtype.itemsize, channels=1)
        self.audio3 = AudioSegment(self.output2.tobytes(),frame_rate=self.rate,sample_width=self.data.dtype.itemsize, channels=1)
        mixed = self.audio1.overlay(self.audio2)         
        mixed1  = mixed.overlay(self.audio3)
        play(mixed1) 

    def SaveFirstOutputSong(self):
        self.audio2 = AudioSegment(self.output1.tobytes(),frame_rate=self.rate,sample_width=self.data.dtype.itemsize, channels=1)
        self.audio2.export("Change1.mp3", format='mp3')

    def SaveSecondOutputSong(self):
        self.audio3 = AudioSegment(self.output2.tobytes(),frame_rate=self.rate,sample_width=self.data.dtype.itemsize, channels=1)
        self.audio3.export("Change2.mp3", format='mp3')

