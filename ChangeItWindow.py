# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ChangeItWindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from ModifiedSignal import Ui_ModifiedSignal

class Ui_ChangeItWindow(object):
    def openChangeWindow(self):
        self.window= QtWidgets.QMainWindow()
        self.ui =Ui_ModifiedSignal()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1268, 926)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.HalfFourierTransformGraph = QtWidgets.QGraphicsView(self.centralwidget)
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
        self.FirstBandSlider.setMinimum(-10)
        self.FirstBandSlider.setMaximum(10)
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
        self.SecondBandSlider.setMinimum(-10)
        self.SecondBandSlider.setMaximum(10)
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
        self.ThirdBandSlider.setMinimum(-10)
        self.ThirdBandSlider.setMaximum(10)
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
        self.FourthBandSlider.setMinimum(-10)
        self.FourthBandSlider.setMaximum(10)
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
        self.FifthBandSlider.setMinimum(-10)
        self.FifthBandSlider.setMaximum(10)
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
        self.SixthBandSlider.setMinimum(-10)
        self.SixthBandSlider.setMaximum(10)
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
        self.SeventhBandSlider.setMinimum(-10)
        self.SeventhBandSlider.setMaximum(10)
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
        self.EighthBandSlider.setMinimum(-10)
        self.EighthBandSlider.setMaximum(10)
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
        self.NinthBandSlider.setMinimum(-10)
        self.NinthBandSlider.setMaximum(10)
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
        self.TenthBandSlider.setMinimum(-10)
        self.TenthBandSlider.setMaximum(10)
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
        self.FirstBandSpinBox.setMinimum(-10)
        self.FirstBandSpinBox.setMaximum(10)
        self.FirstBandSpinBox.setObjectName("FirstBandSpinBox")
        self.horizontalLayout_2.addWidget(self.FirstBandSpinBox)
        self.SecondBandSpinBox = QtWidgets.QSpinBox(self.horizontalLayoutWidget_2)
        self.SecondBandSpinBox.setMinimum(-10)
        self.SecondBandSpinBox.setMaximum(10)
        self.SecondBandSpinBox.setObjectName("SecondBandSpinBox")
        self.horizontalLayout_2.addWidget(self.SecondBandSpinBox)
        self.ThirdBandSpinBox = QtWidgets.QSpinBox(self.horizontalLayoutWidget_2)
        self.ThirdBandSpinBox.setMinimum(-10)
        self.ThirdBandSpinBox.setMaximum(10)
        self.ThirdBandSpinBox.setObjectName("ThirdBandSpinBox")
        self.horizontalLayout_2.addWidget(self.ThirdBandSpinBox)
        self.FourthBandSpinBox = QtWidgets.QSpinBox(self.horizontalLayoutWidget_2)
        self.FourthBandSpinBox.setMinimum(-10)
        self.FourthBandSpinBox.setMaximum(10)
        self.FourthBandSpinBox.setObjectName("FourthBandSpinBox")
        self.horizontalLayout_2.addWidget(self.FourthBandSpinBox)
        self.FifthBandSpinBox = QtWidgets.QSpinBox(self.horizontalLayoutWidget_2)
        self.FifthBandSpinBox.setMinimum(-10)
        self.FifthBandSpinBox.setMaximum(10)
        self.FifthBandSpinBox.setObjectName("FifthBandSpinBox")
        self.horizontalLayout_2.addWidget(self.FifthBandSpinBox)
        self.SixthBandSpinBox = QtWidgets.QSpinBox(self.horizontalLayoutWidget_2)
        self.SixthBandSpinBox.setMinimum(-10)
        self.SixthBandSpinBox.setMaximum(10)
        self.SixthBandSpinBox.setObjectName("SixthBandSpinBox")
        self.horizontalLayout_2.addWidget(self.SixthBandSpinBox)
        self.SeventhBandSpinBox = QtWidgets.QSpinBox(self.horizontalLayoutWidget_2)
        self.SeventhBandSpinBox.setMinimum(-10)
        self.SeventhBandSpinBox.setMaximum(10)
        self.SeventhBandSpinBox.setObjectName("SeventhBandSpinBox")
        self.horizontalLayout_2.addWidget(self.SeventhBandSpinBox)
        self.EighthBandSpinBox = QtWidgets.QSpinBox(self.horizontalLayoutWidget_2)
        self.EighthBandSpinBox.setMinimum(-10)
        self.EighthBandSpinBox.setMaximum(10)
        self.EighthBandSpinBox.setObjectName("EighthBandSpinBox")
        self.horizontalLayout_2.addWidget(self.EighthBandSpinBox)
        self.NinthBandSpinBox = QtWidgets.QSpinBox(self.horizontalLayoutWidget_2)
        self.NinthBandSpinBox.setMinimum(-10)
        self.NinthBandSpinBox.setMaximum(10)
        self.NinthBandSpinBox.setObjectName("NinthBandSpinBox")
        self.horizontalLayout_2.addWidget(self.NinthBandSpinBox)
        self.TenthBandSpinBox = QtWidgets.QSpinBox(self.horizontalLayoutWidget_2)
        self.TenthBandSpinBox.setMinimum(-10)
        self.TenthBandSpinBox.setMaximum(10)
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
        self.NextPushButton.clicked.connect(self.openChangeWindow)
        self.gridLayout.addWidget(self.NextPushButton, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1268, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Choose.setText(_translate("MainWindow", "Choose one window"))
        self.RectWindow.setText(_translate("MainWindow", "Rectangular"))
        self.HamWindow.setText(_translate("MainWindow", "Hamming"))
        self.HanWindow.setText(_translate("MainWindow", "Hanning"))
        self.FirstBandLabel.setText(_translate("MainWindow", "First Band"))
        self.SecondBandLabel.setText(_translate("MainWindow", "Second Band"))
        self.ThirdBandLabel.setText(_translate("MainWindow", "Third Band"))
        self.FourthBandLabel.setText(_translate("MainWindow", "Fourth Band"))
        self.FifthBandLabel.setText(_translate("MainWindow", "Fifth Band"))
        self.SixthBandLabel.setText(_translate("MainWindow", "Sixth Band"))
        self.SeventhBandLabel.setText(_translate("MainWindow", "Seventh Band"))
        self.EighthBandLabel.setText(_translate("MainWindow", "Eighth Band"))
        self.NinthBandLabel.setText(_translate("MainWindow", "Ninth Band"))
        self.TenthBandLabel.setText(_translate("MainWindow", "Tenth Band"))
        self.NextPushButton.setText(_translate("MainWindow", "Next"))
        


