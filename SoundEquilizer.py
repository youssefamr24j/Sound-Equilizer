# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ChangeItWindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import wave
from pydub import AudioSegment
from pygame import mixer
from moviepy.editor import AudioFileClip
from os import path
import matplotlib.pyplot as plt
from scipy.io import wavfile as wav
from PyQt5 import QtCore, QtGui, QtWidgets
from pyqtgraph import PlotWidget,plot
from scipy.io import loadmat
import numpy as np
import time
import sys
from scipy.fftpack import fft
from numpy.fft import fft,fftfreq,ifft
import matplotlib.pyplot as plt
import math
from scipy import signal 
import hamming as hm
from ModifiedSignal import Ui_ModifiedSignal


class Ui_SoundEquilizer(object):
    def __init__(self,data,rate):
        self.data=data
        self.rate=rate
    def setupUi(self, SoundEquilizer):
        SoundEquilizer.setObjectName("SoundEquilizer")
        SoundEquilizer.resize(1268, 926)
        self.centralwidget = QtWidgets.QWidget(SoundEquilizer)
        self.centralwidget.setObjectName("centralwidget")
        self.HalfFourierTransformGraph = PlotWidget(self.centralwidget)
        self.HalfFourierTransformGraph.setGeometry(QtCore.QRect(20, 10, 1231, 541))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.HalfFourierTransformGraph.sizePolicy().hasHeightForWidth())
        self.HalfFourierTransformGraph.setSizePolicy(sizePolicy)
        self.HalfFourierTransformGraph.setObjectName("HalfFourierTransformGraph")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 570, 1071, 191))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.FirstBandSlider = QtWidgets.QSlider(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.FirstBandSlider.sizePolicy().hasHeightForWidth())
        self.FirstBandSlider.setSizePolicy(sizePolicy)
        self.FirstBandSlider.setMinimum(0)
        self.FirstBandSlider.setMaximum(100)
        self.FirstBandSlider.setTracking(True)
        self.FirstBandSlider.setOrientation(QtCore.Qt.Vertical)
        self.FirstBandSlider.setObjectName("FirstBandSlider")
        self.horizontalLayout.addWidget(self.FirstBandSlider)
        self.SecondBandSlider = QtWidgets.QSlider(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SecondBandSlider.sizePolicy().hasHeightForWidth())
        self.SecondBandSlider.setSizePolicy(sizePolicy)
        self.SecondBandSlider.setMinimum(0)
        self.SecondBandSlider.setMaximum(100)
        self.SecondBandSlider.setTracking(True)
        self.SecondBandSlider.setOrientation(QtCore.Qt.Vertical)
        self.SecondBandSlider.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.SecondBandSlider.setObjectName("SecondBandSlider")
        self.horizontalLayout.addWidget(self.SecondBandSlider)
        self.ThirdBandSlider = QtWidgets.QSlider(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ThirdBandSlider.sizePolicy().hasHeightForWidth())
        self.ThirdBandSlider.setSizePolicy(sizePolicy)
        self.ThirdBandSlider.setMinimum(0)
        self.ThirdBandSlider.setMaximum(100)
        self.ThirdBandSlider.setTracking(True)
        self.ThirdBandSlider.setOrientation(QtCore.Qt.Vertical)
        self.ThirdBandSlider.setObjectName("ThirdBandSlider")
        self.horizontalLayout.addWidget(self.ThirdBandSlider)
        self.FourthBandSlider = QtWidgets.QSlider(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.FourthBandSlider.sizePolicy().hasHeightForWidth())
        self.FourthBandSlider.setSizePolicy(sizePolicy)
        self.FourthBandSlider.setMinimum(0)
        self.FourthBandSlider.setMaximum(100)
        self.FourthBandSlider.setTracking(True)
        self.FourthBandSlider.setOrientation(QtCore.Qt.Vertical)
        self.FourthBandSlider.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.FourthBandSlider.setObjectName("FourthBandSlider")
        self.horizontalLayout.addWidget(self.FourthBandSlider)
        self.FifthBandSlider = QtWidgets.QSlider(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.FifthBandSlider.sizePolicy().hasHeightForWidth())
        self.FifthBandSlider.setSizePolicy(sizePolicy)
        self.FifthBandSlider.setMinimum(0)
        self.FifthBandSlider.setMaximum(100)
        self.FifthBandSlider.setTracking(True)
        self.FifthBandSlider.setOrientation(QtCore.Qt.Vertical)
        self.FifthBandSlider.setObjectName("FifthBandSlider")
        self.horizontalLayout.addWidget(self.FifthBandSlider)
        self.SixthBandSlider = QtWidgets.QSlider(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SixthBandSlider.sizePolicy().hasHeightForWidth())
        self.SixthBandSlider.setSizePolicy(sizePolicy)
        self.SixthBandSlider.setMinimum(0)
        self.SixthBandSlider.setMaximum(100)
        self.SixthBandSlider.setTracking(True)
        self.SixthBandSlider.setOrientation(QtCore.Qt.Vertical)
        self.SixthBandSlider.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.SixthBandSlider.setObjectName("SixthBandSlider")
        self.horizontalLayout.addWidget(self.SixthBandSlider)
        self.SeventhBandSlider = QtWidgets.QSlider(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SeventhBandSlider.sizePolicy().hasHeightForWidth())
        self.SeventhBandSlider.setSizePolicy(sizePolicy)
        self.SeventhBandSlider.setMinimum(0)
        self.SeventhBandSlider.setMaximum(100)
        self.SeventhBandSlider.setTracking(True)
        self.SeventhBandSlider.setOrientation(QtCore.Qt.Vertical)
        self.SeventhBandSlider.setObjectName("SeventhBandSlider")
        self.horizontalLayout.addWidget(self.SeventhBandSlider)
        self.EighthBandSlider = QtWidgets.QSlider(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.EighthBandSlider.sizePolicy().hasHeightForWidth())
        self.EighthBandSlider.setSizePolicy(sizePolicy)
        self.EighthBandSlider.setMinimum(0)
        self.EighthBandSlider.setMaximum(100)
        self.EighthBandSlider.setTracking(True)
        self.EighthBandSlider.setOrientation(QtCore.Qt.Vertical)
        self.EighthBandSlider.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.EighthBandSlider.setObjectName("EighthBandSlider")
        self.horizontalLayout.addWidget(self.EighthBandSlider)
        self.NinthBandSlider = QtWidgets.QSlider(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.NinthBandSlider.sizePolicy().hasHeightForWidth())
        self.NinthBandSlider.setSizePolicy(sizePolicy)
        self.NinthBandSlider.setMinimum(0)
        self.NinthBandSlider.setMaximum(100)
        self.NinthBandSlider.setTracking(True)
        self.NinthBandSlider.setOrientation(QtCore.Qt.Vertical)
        self.NinthBandSlider.setObjectName("NinthBandSlider")
        self.horizontalLayout.addWidget(self.NinthBandSlider)
        self.TenthBandSlider = QtWidgets.QSlider(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TenthBandSlider.sizePolicy().hasHeightForWidth())
        self.TenthBandSlider.setSizePolicy(sizePolicy)
        self.TenthBandSlider.setMinimum(0)
        self.TenthBandSlider.setMaximum(100)
        self.TenthBandSlider.setTracking(True)
        self.TenthBandSlider.setOrientation(QtCore.Qt.Vertical)
        self.TenthBandSlider.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.TenthBandSlider.setObjectName("TenthBandSlider")
        self.horizontalLayout.addWidget(self.TenthBandSlider)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(1080, 570, 171, 191))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Choose = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Choose.sizePolicy().hasHeightForWidth())
        self.Choose.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 7, 11))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 7, 11))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 7, 11))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.HighlightedText, brush)
        self.Choose.setPalette(palette)
        self.Choose.setObjectName("Choose")
        self.verticalLayout.addWidget(self.Choose)
        self.RectWindow = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.RectWindow.setAutoRepeat(False)
        self.RectWindow.setAutoExclusive(True)
        self.RectWindow.setObjectName("RectWindow")
        self.verticalLayout.addWidget(self.RectWindow)
        self.HamWindow = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.HamWindow.setAutoRepeat(False)
        self.HamWindow.setAutoExclusive(True)
        self.HamWindow.setObjectName("HamWindow")
        self.verticalLayout.addWidget(self.HamWindow)
        self.HanWindow = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.HanWindow.setAutoRepeat(False)
        self.HanWindow.setAutoExclusive(True)
        self.HanWindow.setObjectName("HanWindow")
        self.verticalLayout.addWidget(self.HanWindow)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 760, 1071, 61))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.FirstBandSpinBox = QtWidgets.QSpinBox(self.horizontalLayoutWidget_2)
        self.FirstBandSpinBox.setMinimum(0)
        self.FirstBandSpinBox.setMaximum(100)
        self.FirstBandSpinBox.setObjectName("FirstBandSpinBox")
        self.horizontalLayout_2.addWidget(self.FirstBandSpinBox)
        self.SecondBandSpinBox = QtWidgets.QSpinBox(self.horizontalLayoutWidget_2)
        self.SecondBandSpinBox.setMinimum(0)
        self.SecondBandSpinBox.setMaximum(100)
        self.SecondBandSpinBox.setObjectName("SecondBandSpinBox")
        self.horizontalLayout_2.addWidget(self.SecondBandSpinBox)
        self.ThirdBandSpinBox = QtWidgets.QSpinBox(self.horizontalLayoutWidget_2)
        self.ThirdBandSpinBox.setMinimum(0)
        self.ThirdBandSpinBox.setMaximum(100)
        self.ThirdBandSpinBox.setObjectName("ThirdBandSpinBox")
        self.horizontalLayout_2.addWidget(self.ThirdBandSpinBox)
        self.FourthBandSpinBox = QtWidgets.QSpinBox(self.horizontalLayoutWidget_2)
        self.FourthBandSpinBox.setMinimum(0)
        self.FourthBandSpinBox.setMaximum(100)
        self.FourthBandSpinBox.setObjectName("FourthBandSpinBox")
        self.horizontalLayout_2.addWidget(self.FourthBandSpinBox)
        self.FifthBandSpinBox = QtWidgets.QSpinBox(self.horizontalLayoutWidget_2)
        self.FifthBandSpinBox.setMinimum(0)
        self.FifthBandSpinBox.setMaximum(100)
        self.FifthBandSpinBox.setObjectName("FifthBandSpinBox")
        self.horizontalLayout_2.addWidget(self.FifthBandSpinBox)
        self.SixthBandSpinBox = QtWidgets.QSpinBox(self.horizontalLayoutWidget_2)
        self.SixthBandSpinBox.setMinimum(0)
        self.SixthBandSpinBox.setMaximum(100)
        self.SixthBandSpinBox.setObjectName("SixthBandSpinBox")
        self.horizontalLayout_2.addWidget(self.SixthBandSpinBox)
        self.SeventhBandSpinBox = QtWidgets.QSpinBox(self.horizontalLayoutWidget_2)
        self.SeventhBandSpinBox.setMinimum(0)
        self.SeventhBandSpinBox.setMaximum(100)
        self.SeventhBandSpinBox.setObjectName("SeventhBandSpinBox")
        self.horizontalLayout_2.addWidget(self.SeventhBandSpinBox)
        self.EighthBandSpinBox = QtWidgets.QSpinBox(self.horizontalLayoutWidget_2)
        self.EighthBandSpinBox.setMinimum(0)
        self.EighthBandSpinBox.setMaximum(100)
        self.EighthBandSpinBox.setObjectName("EighthBandSpinBox")
        self.horizontalLayout_2.addWidget(self.EighthBandSpinBox)
        self.NinthBandSpinBox = QtWidgets.QSpinBox(self.horizontalLayoutWidget_2)
        self.NinthBandSpinBox.setMinimum(0)
        self.NinthBandSpinBox.setMaximum(100)
        self.NinthBandSpinBox.setObjectName("NinthBandSpinBox")
        self.horizontalLayout_2.addWidget(self.NinthBandSpinBox)
        self.TenthBandSpinBox = QtWidgets.QSpinBox(self.horizontalLayoutWidget_2)
        self.TenthBandSpinBox.setMinimum(0)
        self.TenthBandSpinBox.setMaximum(100)
        self.TenthBandSpinBox.setObjectName("TenthBandSpinBox")
        self.horizontalLayout_2.addWidget(self.TenthBandSpinBox)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(10, 820, 1071, 51))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.FirstBandLabel = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.FirstBandLabel.setObjectName("FirstBandLabel")
        self.horizontalLayout_3.addWidget(self.FirstBandLabel)
        self.SecondBandLabel = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.SecondBandLabel.setObjectName("SecondBandLabel")
        self.horizontalLayout_3.addWidget(self.SecondBandLabel)
        self.ThirdBandLabel = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.ThirdBandLabel.setObjectName("ThirdBandLabel")
        self.horizontalLayout_3.addWidget(self.ThirdBandLabel)
        self.FourthBandLabel = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.FourthBandLabel.setObjectName("FourthBandLabel")
        self.horizontalLayout_3.addWidget(self.FourthBandLabel)
        self.FifthBandLabel = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.FifthBandLabel.setObjectName("FifthBandLabel")
        self.horizontalLayout_3.addWidget(self.FifthBandLabel)
        self.SixthBandLabel = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.SixthBandLabel.setObjectName("SixthBandLabel")
        self.horizontalLayout_3.addWidget(self.SixthBandLabel)
        self.SeventhBandLabel = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.SeventhBandLabel.setObjectName("SeventhBandLabel")
        self.horizontalLayout_3.addWidget(self.SeventhBandLabel)
        self.EighthBandLabel = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.EighthBandLabel.setObjectName("EighthBandLabel")
        self.horizontalLayout_3.addWidget(self.EighthBandLabel)
        self.NinthBandLabel = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.NinthBandLabel.setObjectName("NinthBandLabel")
        self.horizontalLayout_3.addWidget(self.NinthBandLabel)
        self.TenthBandLabel = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.TenthBandLabel.setObjectName("TenthBandLabel")
        self.horizontalLayout_3.addWidget(self.TenthBandLabel)
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(1080, 760, 171, 111))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.NextPushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.NextPushButton.sizePolicy().hasHeightForWidth())
        self.NextPushButton.setSizePolicy(sizePolicy)
        self.NextPushButton.setObjectName("NextPushButton")
        self.gridLayout.addWidget(self.NextPushButton, 0, 0, 1, 1)
        SoundEquilizer.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(SoundEquilizer)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1268, 25))
        self.menubar.setObjectName("menubar")
        SoundEquilizer.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(SoundEquilizer)
        self.statusbar.setObjectName("statusbar")
        SoundEquilizer.setStatusBar(self.statusbar)

        
        self.SliderArr=[self.FirstBandSlider,self.SecondBandSlider,self.ThirdBandSlider,self.FourthBandSlider,self.FifthBandSlider,self.SixthBandSlider,self.SeventhBandSlider,self.EighthBandSlider,self.NinthBandSlider,self.TenthBandSlider]
        self.SpinArr=[self.FirstBandSpinBox,self.SecondBandSpinBox,self.ThirdBandSpinBox,self.FourthBandSpinBox,self.FifthBandSpinBox,self.SixthBandSpinBox,self.SeventhBandSpinBox,self.EighthBandSpinBox,self.NinthBandSpinBox,self.TenthBandSpinBox]
        self.HalfFourier=[]
        self.NegativeHalf=[]
        self.BandsArray=[]
        self.Length=0
        self.SubLength=0
        self.Magnitude=[]
        self.RightMagnitude=[]
        self.LeftMagnitude=[]
        self.Phase=[]
        self.output=[]
        
        self.retranslateUi(SoundEquilizer)
        QtCore.QMetaObject.connectSlotsByName(SoundEquilizer)

    def retranslateUi(self, SoundEquilizer):
        _translate = QtCore.QCoreApplication.translate
        SoundEquilizer.setWindowTitle(_translate("SoundEquilizer", "SoundEquilizer"))
        self.Choose.setText(_translate("SoundEquilizer", "Choose one window"))
        self.RectWindow.setText(_translate("SoundEquilizer", "Rectangular"))
        self.HamWindow.setText(_translate("SoundEquilizer", "Hamming"))
        self.HanWindow.setText(_translate("SoundEquilizer", "Hanning"))
        self.FirstBandLabel.setText(_translate("SoundEquilizer", "First Band"))
        self.SecondBandLabel.setText(_translate("SoundEquilizer", "Second Band"))
        self.ThirdBandLabel.setText(_translate("SoundEquilizer", "Third Band"))
        self.FourthBandLabel.setText(_translate("SoundEquilizer", "Fourth Band"))
        self.FifthBandLabel.setText(_translate("SoundEquilizer", "Fifth Band"))
        self.SixthBandLabel.setText(_translate("SoundEquilizer", "Sixth Band"))
        self.SeventhBandLabel.setText(_translate("SoundEquilizer", "Seventh Band"))
        self.EighthBandLabel.setText(_translate("SoundEquilizer", "Eighth Band"))
        self.NinthBandLabel.setText(_translate("SoundEquilizer", "Ninth Band"))
        self.TenthBandLabel.setText(_translate("SoundEquilizer", "Tenth Band"))
        self.NextPushButton.setText(_translate("SoundEquilizer", "Next"))
        self.DrawHalfFourierSignal()
        self.FirstBandSlider.valueChanged.connect(lambda:self.SliderDetector(0))
        self.SecondBandSlider.valueChanged.connect(lambda:self.SliderDetector(1))
        self.ThirdBandSlider.valueChanged.connect(lambda:self.SliderDetector(2))
        self.FourthBandSlider.valueChanged.connect(lambda:self.SliderDetector(3))
        self.FifthBandSlider.valueChanged.connect(lambda:self.SliderDetector(4))
        self.SixthBandSlider.valueChanged.connect(lambda:self.SliderDetector(5))
        self.SeventhBandSlider.valueChanged.connect(lambda:self.SliderDetector(6))
        self.EighthBandSlider.valueChanged.connect(lambda:self.SliderDetector(7))
        self.NinthBandSlider.valueChanged.connect(lambda:self.SliderDetector(8))
        self.TenthBandSlider.valueChanged.connect(lambda:self.SliderDetector(9))
        self.FirstBandSpinBox.valueChanged.connect(lambda:self.SpinDetector(0))
        self.SecondBandSpinBox.valueChanged.connect(lambda:self.SpinDetector(1))
        self.ThirdBandSpinBox.valueChanged.connect(lambda:self.SpinDetector(2))
        self.FourthBandSpinBox.valueChanged.connect(lambda:self.SpinDetector(3))
        self.FifthBandSpinBox.valueChanged.connect(lambda:self.SpinDetector(4))
        self.SixthBandSpinBox.valueChanged.connect(lambda:self.SpinDetector(5))
        self.SeventhBandSpinBox.valueChanged.connect(lambda:self.SpinDetector(6))
        self.EighthBandSpinBox.valueChanged.connect(lambda:self.SpinDetector(7))
        self.NinthBandSpinBox.valueChanged.connect(lambda:self.SpinDetector(8))
        self.TenthBandSpinBox.valueChanged.connect(lambda:self.SpinDetector(9))
        self.NextPushButton.clicked.connect(lambda:self.ApplyChanges(SoundEquilizer))
        

       
    def DrawHalfFourierSignal(self):
        fft_out = fft(self.data)
        self.Magnitude=(np.abs(fft_out))
        self.Phase=(np.angle(fft_out))
        self.Length=len(self.Magnitude)
        if(self.Length % 2 == 0):
            HalfLength=((self.Length)/2)
            j=0
            while(j<HalfLength):
                self.LeftMagnitude.append(self.Magnitude[j])
                j+=1
            j=(self.Length-1)
            self.HalfFourierTransformGraph.plot(self.LeftMagnitude)  #drawing half Fourier transform
            while(j>=HalfLength):
                self.RightMagnitude.append(self.Magnitude[j])
                j-=1
        else:
            HalfLength=(int(self.Length)/2)
            j=0
            while(j<HalfLength):
                self.LeftMagnitude.append(self.Magnitude[j])
                j+=1
            j=(self.Length-1)
            self.HalfFourierTransformGraph.plot(self.LeftMagnitude)  #drawing half Fourier transform
            while(j>HalfLength):
                self.RightMagnitude.append(self.Magnitude[j])
                j-=1
            
        self.SubLength=int(len(self.LeftMagnitude)/10)        
        Bandindex=0
        while(Bandindex<10):
            temp=(Bandindex*self.SubLength)
            Bandindex+=1
            temp2=(Bandindex*self.SubLength)
            self.BandsArray.append([temp,temp2])

 
    def RectWind(self):
        ForCounter=0
        for i in self.SpinArr:
            Gain=i.value()
            Range=self.BandsArray[ForCounter]
            BeginAndEnd=Range[0]
            ForCounter+=1
            while(BeginAndEnd<Range[1]):
                self.LeftMagnitude[BeginAndEnd]=Gain*self.LeftMagnitude[BeginAndEnd]
                self.RightMagnitude[BeginAndEnd]=Gain*self.RightMagnitude[BeginAndEnd]
                BeginAndEnd+=1
        
        self.RightMagnitude=self.RightMagnitude[::-1]
        self.Magnitude=self.LeftMagnitude + self.RightMagnitude

        for i in range (len(self.Magnitude)):
            tx=self.Magnitude[i]*(np.cos(self.Phase[i]))
            ty=self.Magnitude[i]*(np.sin(self.Phase[i]))
            self.output.append(complex(tx,ty))

        self.output=ifft(self.output)
        self.output=np.real(self.output)
            

    def HamWind(self):
        size=(int((self.SubLength)*(100/54)))
        if(size%2==0):
            size=(size-1)

        h_window=hm.hamming(size)
        half_max=0.5*max(h_window)
        half_m = h_window.flat[np.abs(h_window - half_max).argmin()]
        HamArr=[]
        for i in h_window:
            HamArr.append(i)

        flag=0
        DivL=[]
        CloseMax=self.closest(HamArr,1)
        for i in HamArr:
            if(flag==0):
                DivL.append(i)
            if(i==CloseMax):
                break

        CloseHalfMax=self.closest(DivL,half_m)
        HalfMaxIndex=DivL.index(CloseHalfMax)
        SecHalfMaxIndex=((size-HalfMaxIndex)-1)        

        
        ForCounter=0
        for i in self.SpinArr:
            Gain=i.value()
            Range=self.BandsArray[ForCounter]
            BeginAndEnd=Range[0]  
            for i in HamArr:
                i=Gain*i   
            
            temp=HalfMaxIndex
            BWArr=[]
            while(HalfMaxIndex<=SecHalfMaxIndex):
                BWArr.append(HamArr[HalfMaxIndex])
                HalfMaxIndex+=1

            HalfMaxIndex=temp
            BWArrindex=0
            while(BeginAndEnd<Range[1]):
                self.LeftMagnitude[BeginAndEnd]=BWArr[BWArrindex]*self.LeftMagnitude[BeginAndEnd]
                self.RightMagnitude[BeginAndEnd]=BWArr[BWArrindex]*self.RightMagnitude[BeginAndEnd]
                BeginAndEnd+=1    


            LeftArr=[]
            count1=HalfMaxIndex
            if(ForCounter==0):
                pass 
            else:
                for i in range(len(HamArr)):
                    if(i==HalfMaxIndex):
                        break
                    LeftArr.append(HamArr[i])
                
                x=0
                while(count1>0):
                    self.LeftMagnitude[Range[0]-count1]=LeftArr[x]* self.LeftMagnitude[Range[0]-count1]
                    self.RightMagnitude[Range[0]-count1]=LeftArr[x]* self.RightMagnitude[Range[0]-count1]
                    count1-=1
                    x+=1   
            
            RightArr=[]
            count2=SecHalfMaxIndex+1
            if(ForCounter==9):
                pass 
            else:
                while(count2<size):
                    RightArr.append(HamArr[count2])
                    count2+=1
                
                count2=SecHalfMaxIndex+1
                increment=1
                x=0
                while(count2<size):
                    self.LeftMagnitude[Range[1]+increment]=RightArr[x]* self.LeftMagnitude[Range[1]+increment]
                    self.RightMagnitude[Range[1]+increment]=RightArr[x]* self.RightMagnitude[Range[1]+increment]
                    count2+=1
                    increment+=1
                    x+=1 
            
            ForCounter+=1 
        

        self.RightMagnitude=self.RightMagnitude[::-1]
        self.Magnitude=self.LeftMagnitude + self.RightMagnitude

        for i in range (len(self.Magnitude)):
            tx=self.Magnitude[i]*(np.cos(self.Phase[i]))
            ty=self.Magnitude[i]*(np.sin(self.Phase[i]))
            self.output.append(complex(tx,ty))

        self.output=ifft(self.output)
        self.output=np.real(self.output)


    def HanWind(self):
        size=(int((self.SubLength)*(100/50)))
        if(size%2==0):
            size=(size-1)

        h_window=hm.hanning(size)
        half_max=0.5*max(h_window)
        half_m = h_window.flat[np.abs(h_window - half_max).argmin()]
        HamArr=[]
        for i in h_window:
            HamArr.append(i)

        flag=0
        DivL=[]
        CloseMax=self.closest(HamArr,1)
        for i in HamArr:
            if(flag==0):
                DivL.append(i)
            if(i==CloseMax):
                break

        CloseHalfMax=self.closest(DivL,half_m)
        HalfMaxIndex=DivL.index(CloseHalfMax)
        SecHalfMaxIndex=((size-HalfMaxIndex)-1)        

        
        ForCounter=0
        for i in self.SpinArr:
            Gain=i.value()
            Range=self.BandsArray[ForCounter]
            BeginAndEnd=Range[0]  
            for i in HamArr:
                i=Gain*i   
            
            temp=HalfMaxIndex
            BWArr=[]
            while(HalfMaxIndex<=SecHalfMaxIndex):
                BWArr.append(HamArr[HalfMaxIndex])
                HalfMaxIndex+=1

            HalfMaxIndex=temp
            BWArrindex=0
            while(BeginAndEnd<Range[1]):
                self.LeftMagnitude[BeginAndEnd]=BWArr[BWArrindex]*self.LeftMagnitude[BeginAndEnd]
                self.RightMagnitude[BeginAndEnd]=BWArr[BWArrindex]*self.RightMagnitude[BeginAndEnd]
                BeginAndEnd+=1    


            LeftArr=[]
            count1=HalfMaxIndex
            if(ForCounter==0):
                pass 
            else:
                for i in range(len(HamArr)):
                    if(i==HalfMaxIndex):
                        break
                    LeftArr.append(HamArr[i])
                
                x=0
                while(count1>0):
                    self.LeftMagnitude[Range[0]-count1]=LeftArr[x]* self.LeftMagnitude[Range[0]-count1]
                    self.RightMagnitude[Range[0]-count1]=LeftArr[x]* self.RightMagnitude[Range[0]-count1]
                    count1-=1
                    x+=1   
            
            RightArr=[]
            count2=SecHalfMaxIndex+1
            if(ForCounter==9):
                pass 
            else:
                while(count2<size):
                    RightArr.append(HamArr[count2])
                    count2+=1
                
                count2=SecHalfMaxIndex+1
                increment=1
                x=0
                while(count2<size):
                    self.LeftMagnitude[Range[1]+increment]=RightArr[x]* self.LeftMagnitude[Range[1]+increment]
                    self.RightMagnitude[Range[1]+increment]=RightArr[x]* self.RightMagnitude[Range[1]+increment]
                    count2+=1
                    increment+=1
                    x+=1 
            
            ForCounter+=1 
        

        self.RightMagnitude=self.RightMagnitude[::-1]
        self.Magnitude=self.LeftMagnitude + self.RightMagnitude

        for i in range (len(self.Magnitude)):
            tx=self.Magnitude[i]*(np.cos(self.Phase[i]))
            ty=self.Magnitude[i]*(np.sin(self.Phase[i]))
            self.output.append(complex(tx,ty))

        self.output=ifft(self.output)
        self.output=np.real(self.output)

        

    def SliderDetector(self, i):
        val=self.SliderArr[i].value()
        self.SpinArr[i].setValue(val)
                 
    def SpinDetector(self ,i):
        val=self.SpinArr[i].value()
        self.SliderArr[i].setValue(val)
        

    def ApplyChanges(self,SoundEquilizer):
        if(self.RectWindow.isChecked()):
            self.RectWind()
            self.ModifiedSignal(SoundEquilizer)
        elif(self.HamWindow.isChecked()):
            self.HamWind()
            self.ModifiedSignal(SoundEquilizer)
        elif(self.HanWindow.isChecked()):
            self.HanWind()
            self.ModifiedSignal(SoundEquilizer)
        

        
     

    def ModifiedSignal(self , SoundEquilizer):
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_ModifiedSignal(self.data,self.output,self.rate)
        self.ui.setupUi(self.window)
        SoundEquilizer.hide()
        self.window.show()


    
    def closest(self,lst, K):
        lst = np.asarray(lst) 
        idx = (np.abs(lst - K)).argmin() 
        return lst[idx]  
    
     