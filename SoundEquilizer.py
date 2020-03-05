from pygame import mixer
from moviepy.editor import AudioFileClip
from os import path
from pydub import AudioSegment
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
import wave
import matplotlib.pyplot as plt



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.graphicsView = PlotWidget(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(15, 11, 761, 551))
        self.graphicsView.setObjectName("graphicsView")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuOpen = QtWidgets.QMenu(self.menuFile)
        self.menuOpen.setObjectName("menuOpen")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionO = QtWidgets.QAction(MainWindow)
        self.actionO.setObjectName("actionO")
        self.menuOpen.addAction(self.actionO)
        self.menuFile.addAction(self.menuOpen.menuAction())
        self.menubar.addAction(self.menuFile.menuAction())

        self.Xaxis=[]
        self.Yaxis=[]

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuFile.setTitle(_translate("MainWindow", "file"))
        self.menuOpen.setTitle(_translate("MainWindow", "open"))
        self.actionO.setText(_translate("MainWindow", "o"))
        self.menuOpen.triggered.connect(self.Open_Files)






    def Open_Files(self):                                  #open file and read it
        filename=QtWidgets.QFileDialog.getOpenFileName()
        directory=filename[0]
       
        src = directory
        dst = "test.wav"

        # convert wav to mp3                                                            
        sound = AudioSegment.from_mp3(src)
        sound.export(dst, format="wav")

       
        rate, data = wav.read('test.wav')

        

        fft_out = fft(data[:,0])

        # YMax=max(np.abs(fft_out))
        # YMin=min(np.abs(fft_out))
        # XMax=max(data[:,0])
        # XMin=min(data[:,0])
        


        
        # # plt.plot(data[:,0], np.abs(fft_out))
        # # plt.show()

        # self.graphicsView.plotItem.getViewBox().setLimits(yMin=YMin,yMax=YMax)
        # self.graphicsView.plotItem.getViewBox().setLimits(xMin=XMin,xMax=XMax)    
        self.graphicsView.plot(data[:,0], np.abs(fft_out))
        # self.graphicsView.plot(data[:,0])
        
           
    
    
        # mixer.init()
        # mixer.music.load(directory)
        # mixer.music.play()
        # print(directory)

        # c=0
        # for i in data:
        #     c+=1
        # print(rate)
        # print(c)