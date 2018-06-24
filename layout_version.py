# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'selectversion.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from gw2config import gw2Config
from logo import *

class Ui_Gw2Version(object):    
    def setupUi(self, Gw2Version, MainWindow, ui_main):
        # init ui
        self.MainWindow = MainWindow
        self.VersionWindow = Gw2Version
        self.MainUi = ui_main
        Gw2Version.setObjectName("Gw2Version")
        Gw2Version.resize(310, 190)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/logo/image/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Gw2Version.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(Gw2Version)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.labelSelectVersion = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.labelSelectVersion.setFont(font)
        self.labelSelectVersion.setObjectName("labelSelectVersion")
        self.gridLayout.addWidget(self.labelSelectVersion, 0, 0, 1, 2)
        self.buttonSelectVersionCh = HoverButton(self.centralwidget, "ch")
        self.buttonSelectVersionCh.setMinimumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(15)
        self.buttonSelectVersionCh.setFont(font)
        self.buttonSelectVersionCh.setStyleSheet("QPushButton {border:none}\n"
"QPushButton:focus, QPushButton:pressed {background-color:none}")
        self.buttonSelectVersionCh.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/logo/image/logo_ch_disable.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonSelectVersionCh.setIcon(icon)
        self.buttonSelectVersionCh.setIconSize(QtCore.QSize(128, 150))
        self.buttonSelectVersionCh.setObjectName("buttonSelectVersionCh")
        self.gridLayout.addWidget(self.buttonSelectVersionCh, 1, 0, 1, 1)
        self.buttonSelectVersionEn = HoverButton(self.centralwidget, "en")
        self.buttonSelectVersionEn.setMinimumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(15)
        self.buttonSelectVersionEn.setFont(font)
        self.buttonSelectVersionEn.setStyleSheet("QPushButton {border:none}\n"
"QPushButton:focus, QPushButton:pressed {background-color:none}")
        self.buttonSelectVersionEn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/logo/image/logo_en_disable.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonSelectVersionEn.setIcon(icon1)
        self.buttonSelectVersionEn.setIconSize(QtCore.QSize(150, 150))
        self.buttonSelectVersionEn.setObjectName("buttonSelectVersionEn")
        self.gridLayout.addWidget(self.buttonSelectVersionEn, 1, 1, 1, 1)
        Gw2Version.setCentralWidget(self.centralwidget)

        self.setAction()
        self.retranslateUi(Gw2Version)
        QtCore.QMetaObject.connectSlotsByName(Gw2Version)
        self.centralwidget.setFocus()

    def retranslateUi(self, Gw2Version):
        # init ui text
        _translate = QtCore.QCoreApplication.translate
        Gw2Version.setWindowTitle(_translate("Gw2Version", "激战2双版本启动器 - by bingkong"))
        self.labelSelectVersion.setText(_translate("Gw2Version", "请选择当前游戏版本"))

    def setAction(self):
        # bind ui listener
        self.buttonSelectVersionCh.clicked.connect(self.selectVersionCh)
        self.buttonSelectVersionCh.pressed.connect(self.selectVersionCh_pressed)
        self.buttonSelectVersionCh.released.connect(self.selectVersionCh_released)
        self.buttonSelectVersionEn.clicked.connect(self.selectVersionEn)
        self.buttonSelectVersionEn.pressed.connect(self.selectVersionEn_pressed)
        self.buttonSelectVersionEn.released.connect(self.selectVersionEn_released)
        
    def selectVersionEn(self):
        # 选择当前版本为美服
        current = 'en'
        config = gw2Config()
        config.setCurrent(current)
        self.VersionWindow.hide()
        _translate = QtCore.QCoreApplication.translate
        self.MainUi.labelCurrentVersion.setText(_translate("Gw2Ui", "美服"))
        self.MainWindow.show()
        # 首次使用自动备份
        self.MainUi.firstStart("en")
        
    def selectVersionCh(self):
        # 选择当前版本为国服
        current = 'ch'
        config = gw2Config()
        config.setCurrent(current)
        self.VersionWindow.hide()
        _translate = QtCore.QCoreApplication.translate
        self.MainUi.labelCurrentVersion.setText(_translate("Gw2Ui", "国服"))
        self.MainWindow.show()
        # 首次使用自动备份
        self.MainUi.firstStart("ch")

    def selectVersionCh_pressed(self):
        # 按钮按下动作
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/logo/image/logo_ch_default.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonSelectVersionCh.setIcon(icon)

    def selectVersionCh_released(self):
        # 按钮松开动作
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/logo/image/logo_ch_disable.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonSelectVersionCh.setIcon(icon)

    def selectVersionEn_pressed(self):
        # 按钮按下动作
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/logo/image/logo_en_default.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonSelectVersionEn.setIcon(icon)

    def selectVersionEn_released(self):
        # 按钮松开动作
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/logo/image/logo_en_disable.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonSelectVersionEn.setIcon(icon)

class HoverButton(QtWidgets.QPushButton):
    # 鼠标经过特效
    def __init__(self, parent, lang):
        QtWidgets.QPushButton.__init__(self, parent)
        self.setMouseTracking(True)
        self.lang = lang

    def enterEvent(self, event):
        icon = QtGui.QIcon()
        if self.lang == "en":
            icon.addPixmap(QtGui.QPixmap(":/logo/image/logo_en_default.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        else:
            icon.addPixmap(QtGui.QPixmap(":/logo/image/logo_ch_default.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setIcon(icon)

    def leaveEvent(self, event):
        icon = QtGui.QIcon()
        if self.lang == "en":
            icon.addPixmap(QtGui.QPixmap(":/logo/image/logo_en_disable.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        else:
            icon.addPixmap(QtGui.QPixmap(":/logo/image/logo_ch_disable.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setIcon(icon)
