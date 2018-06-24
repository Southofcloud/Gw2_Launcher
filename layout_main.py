# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from gw2config import gw2Config
import re
import os
import configparser
import sys
import subprocess
from shutil import copyfile
from logo import *

class Ui_Gw2Ui(object):
    def setupUi(self, Gw2Ui):
        # init ui
        self.MainWindow = Gw2Ui
        config = gw2Config()
        Gw2Ui.setObjectName("Gw2Ui")
        Gw2Ui.resize(370, 324)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/logo/image/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Gw2Ui.setWindowIcon(icon)
        Gw2Ui.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.mainWidget = QtWidgets.QWidget(Gw2Ui)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.mainWidget.sizePolicy().hasHeightForWidth())
        self.mainWidget.setSizePolicy(sizePolicy)
        self.mainWidget.setObjectName("mainWidget")
        self.gridLayout_ui = QtWidgets.QGridLayout(self.mainWidget)
        self.gridLayout_ui.setObjectName("gridLayout_ui")
        self.frameMain = QtWidgets.QFrame(self.mainWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frameMain.sizePolicy().hasHeightForWidth())
        self.frameMain.setSizePolicy(sizePolicy)
        self.frameMain.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.frameMain.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frameMain.setAutoFillBackground(True)
        self.frameMain.setStyleSheet("")
        self.frameMain.setObjectName("frameMain")
        self.gridLayout_main = QtWidgets.QGridLayout(self.frameMain)
        self.gridLayout_main.setObjectName("gridLayout_main")
        self.buttonResetChFile = QtWidgets.QPushButton(self.frameMain)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonResetChFile.sizePolicy().hasHeightForWidth())
        self.buttonResetChFile.setSizePolicy(sizePolicy)
        self.buttonResetChFile.setObjectName("buttonResetChFile")
        self.gridLayout_main.addWidget(self.buttonResetChFile, 4, 0, 1, 3)
        self.buttonConfig = QtWidgets.QPushButton(self.frameMain)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonConfig.sizePolicy().hasHeightForWidth())
        self.buttonConfig.setSizePolicy(sizePolicy)
        self.buttonConfig.setObjectName("buttonConfig")
        self.gridLayout_main.addWidget(self.buttonConfig, 5, 0, 1, 2)
        self.buttonExit = QtWidgets.QPushButton(self.frameMain)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonExit.sizePolicy().hasHeightForWidth())
        self.buttonExit.setSizePolicy(sizePolicy)
        self.buttonExit.setMinimumSize(QtCore.QSize(70, 0))
        self.buttonExit.setObjectName("buttonExit")
        self.gridLayout_main.addWidget(self.buttonExit, 5, 2, 1, 1)
        self.buttonResetEnFile = QtWidgets.QPushButton(self.frameMain)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonResetEnFile.sizePolicy().hasHeightForWidth())
        self.buttonResetEnFile.setSizePolicy(sizePolicy)
        self.buttonResetEnFile.setObjectName("buttonResetEnFile")
        self.gridLayout_main.addWidget(self.buttonResetEnFile, 4, 3, 1, 1)
        self.buttonBackEnFile = QtWidgets.QPushButton(self.frameMain)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonBackEnFile.sizePolicy().hasHeightForWidth())
        self.buttonBackEnFile.setSizePolicy(sizePolicy)
        self.buttonBackEnFile.setObjectName("buttonBackEnFile")
        self.gridLayout_main.addWidget(self.buttonBackEnFile, 3, 3, 1, 1)
        self.buttonRunCh = HoverButton(self.frameMain, "ch")
        self.buttonRunCh.setMinimumSize(QtCore.QSize(128, 150))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonRunCh.sizePolicy().hasHeightForWidth())
        self.buttonRunCh.setSizePolicy(sizePolicy)
        self.buttonRunCh.setAutoFillBackground(False)
        self.buttonRunCh.setStyleSheet("QPushButton {border:none;}\n"
"QPushButton:focus, QPushButton:pressed {background-color:none}")
        self.buttonRunCh.setText("")
        icon_ch = QtGui.QIcon()
        icon_ch.addPixmap(QtGui.QPixmap(getDefaultIcon("ch")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonRunCh.setIcon(icon_ch)
        self.buttonRunCh.setIconSize(QtCore.QSize(128, 150))
        self.buttonRunCh.setAutoDefault(False)
        self.buttonRunCh.setObjectName("buttonRunCh")
        self.gridLayout_main.addWidget(self.buttonRunCh, 1, 0, 1, 3)
        self.buttonRunEn = HoverButton(self.frameMain, "en")
        self.buttonRunEn.setMinimumSize(QtCore.QSize(150, 150))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonRunEn.sizePolicy().hasHeightForWidth())
        self.buttonRunEn.setSizePolicy(sizePolicy)
        self.buttonRunEn.setAutoFillBackground(False)
        self.buttonRunEn.setStyleSheet("QPushButton {border:none}\n"
"QPushButton:focus, QPushButton:pressed {background-color:none}")
        self.buttonRunEn.setText("")
        icon_en = QtGui.QIcon()
        icon_en.addPixmap(QtGui.QPixmap(getDefaultIcon("en")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonRunEn.setIcon(icon_en)
        self.buttonRunEn.setIconSize(QtCore.QSize(150, 150))
        self.buttonRunEn.setObjectName("buttonRunEn")
        self.gridLayout_main.addWidget(self.buttonRunEn, 1, 3, 1, 1)
        self.buttonSetChGamePath = QtWidgets.QPushButton(self.frameMain)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonSetChGamePath.sizePolicy().hasHeightForWidth())
        self.buttonSetChGamePath.setSizePolicy(sizePolicy)
        self.buttonSetChGamePath.setObjectName("buttonSetChGamePath")
        self.gridLayout_main.addWidget(self.buttonSetChGamePath, 2, 0, 1, 3)
        self.buttonSetEnGamePath = QtWidgets.QPushButton(self.frameMain)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonSetEnGamePath.sizePolicy().hasHeightForWidth())
        self.buttonSetEnGamePath.setSizePolicy(sizePolicy)
        self.buttonSetEnGamePath.setObjectName("buttonSetEnGamePath")
        self.gridLayout_main.addWidget(self.buttonSetEnGamePath, 2, 3, 1, 1)
        self.labelCurrentVersionTag = QtWidgets.QLabel(self.frameMain)
        self.labelCurrentVersionTag.setObjectName("labelCurrentVersionTag")
        self.gridLayout_main.addWidget(self.labelCurrentVersionTag, 0, 0, 1, 1)
        self.labelCurrentVersion = QtWidgets.QLabel(self.frameMain)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.labelCurrentVersion.setFont(font)
        self.labelCurrentVersion.setObjectName("labelCurrentVersion")
        self.gridLayout_main.addWidget(self.labelCurrentVersion, 0, 1, 1, 2)
        self.buttonBackChFile = QtWidgets.QPushButton(self.frameMain)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonBackChFile.sizePolicy().hasHeightForWidth())
        self.buttonBackChFile.setSizePolicy(sizePolicy)
        self.buttonBackChFile.setObjectName("buttonBackChFile")
        self.gridLayout_main.addWidget(self.buttonBackChFile, 3, 0, 1, 3)
        self.gridLayout_ui.addWidget(self.frameMain, 0, 0, 1, 1)
        self.frameConfig = QtWidgets.QFrame(self.mainWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frameConfig.sizePolicy().hasHeightForWidth())
        self.frameConfig.setSizePolicy(sizePolicy)
        self.frameConfig.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frameConfig.setAutoFillBackground(True)
        self.frameConfig.setStyleSheet("")
        self.frameConfig.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frameConfig.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frameConfig.setObjectName("frameConfig")
        self.gridLayout_config = QtWidgets.QGridLayout(self.frameConfig)
        self.gridLayout_config.setObjectName("gridLayout_config")
        self.labelChDATBackFile = QtWidgets.QLabel(self.frameConfig)
        self.labelChDATBackFile.setObjectName("labelChDATBackFile")
        self.gridLayout_config.addWidget(self.labelChDATBackFile, 10, 0, 1, 1)
        self.textChXMLBackFile = QtWidgets.QLineEdit(self.frameConfig)
        self.textChXMLBackFile.setReadOnly(True)
        self.textChXMLBackFile.setObjectName("textChXMLBackFile")
        self.gridLayout_config.addWidget(self.textChXMLBackFile, 9, 1, 1, 1)
        self.textChDATBackFile = QtWidgets.QLineEdit(self.frameConfig)
        self.textChDATBackFile.setReadOnly(True)
        self.textChDATBackFile.setObjectName("textChDATBackFile")
        self.gridLayout_config.addWidget(self.textChDATBackFile, 10, 1, 1, 1)
        self.labenCh = QtWidgets.QLabel(self.frameConfig)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labenCh.setFont(font)
        self.labenCh.setObjectName("labenCh")
        self.gridLayout_config.addWidget(self.labenCh, 7, 0, 1, 1)
        self.labelChGamePath = QtWidgets.QLabel(self.frameConfig)
        self.labelChGamePath.setObjectName("labelChGamePath")
        self.gridLayout_config.addWidget(self.labelChGamePath, 8, 0, 1, 1)
        self.labenChXMLBackFile = QtWidgets.QLabel(self.frameConfig)
        self.labenChXMLBackFile.setObjectName("labenChXMLBackFile")
        self.gridLayout_config.addWidget(self.labenChXMLBackFile, 9, 0, 1, 1)
        self.labelGlobalCurrent = QtWidgets.QLabel(self.frameConfig)
        self.labelGlobalCurrent.setObjectName("labelGlobalCurrent")
        self.gridLayout_config.addWidget(self.labelGlobalCurrent, 2, 0, 1, 1)
        self.labelGlobal = QtWidgets.QLabel(self.frameConfig)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelGlobal.setFont(font)
        self.labelGlobal.setObjectName("labelGlobal")
        self.gridLayout_config.addWidget(self.labelGlobal, 0, 0, 1, 1)
        self.textGlobalConfigPath = QtWidgets.QLineEdit(self.frameConfig)
        self.textGlobalConfigPath.setReadOnly(True)
        self.textGlobalConfigPath.setObjectName("textGlobalConfigPath")
        self.gridLayout_config.addWidget(self.textGlobalConfigPath, 1, 1, 1, 1)
        self.labelGlobalConfigPath = QtWidgets.QLabel(self.frameConfig)
        self.labelGlobalConfigPath.setObjectName("labelGlobalConfigPath")
        self.gridLayout_config.addWidget(self.labelGlobalConfigPath, 1, 0, 1, 1)
        self.labelEn = QtWidgets.QLabel(self.frameConfig)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelEn.setFont(font)
        self.labelEn.setObjectName("labelEn")
        self.gridLayout_config.addWidget(self.labelEn, 3, 0, 1, 1)
        self.labelEnGamePath = QtWidgets.QLabel(self.frameConfig)
        self.labelEnGamePath.setObjectName("labelEnGamePath")
        self.gridLayout_config.addWidget(self.labelEnGamePath, 4, 0, 1, 1)
        self.labelEnDATBackFile = QtWidgets.QLabel(self.frameConfig)
        self.labelEnDATBackFile.setObjectName("labelEnDATBackFile")
        self.gridLayout_config.addWidget(self.labelEnDATBackFile, 6, 0, 1, 1)
        self.textEnDATBackFile = QtWidgets.QLineEdit(self.frameConfig)
        self.textEnDATBackFile.setReadOnly(True)
        self.textEnDATBackFile.setObjectName("textEnDATBackFile")
        self.gridLayout_config.addWidget(self.textEnDATBackFile, 6, 1, 1, 1)
        self.textChGamePath = QtWidgets.QLineEdit(self.frameConfig)
        self.textChGamePath.setReadOnly(True)
        self.textChGamePath.setObjectName("textChGamePath")
        self.gridLayout_config.addWidget(self.textChGamePath, 8, 1, 1, 1)
        self.textEnGamePath = QtWidgets.QLineEdit(self.frameConfig)
        self.textEnGamePath.setReadOnly(True)
        self.textEnGamePath.setObjectName("textEnGamePath")
        self.gridLayout_config.addWidget(self.textEnGamePath, 4, 1, 1, 1)
        self.textGlobalCurrent = QtWidgets.QLineEdit(self.frameConfig)
        self.textGlobalCurrent.setReadOnly(True)
        self.textGlobalCurrent.setObjectName("textGlobalCurrent")
        self.gridLayout_config.addWidget(self.textGlobalCurrent, 2, 1, 1, 1)
        self.labelEnXMLBackFile = QtWidgets.QLabel(self.frameConfig)
        self.labelEnXMLBackFile.setObjectName("labelEnXMLBackFile")
        self.gridLayout_config.addWidget(self.labelEnXMLBackFile, 5, 0, 1, 1)
        self.textEnXMLBackFile = QtWidgets.QLineEdit(self.frameConfig)
        self.textEnXMLBackFile.setReadOnly(True)
        self.textEnXMLBackFile.setObjectName("textEnXMLBackFile")
        self.gridLayout_config.addWidget(self.textEnXMLBackFile, 5, 1, 1, 1)
        self.buttonConfigReturn = QtWidgets.QPushButton(self.frameConfig)
        self.buttonConfigReturn.setObjectName("buttonConfigReturn")
        self.gridLayout_config.addWidget(self.buttonConfigReturn, 11, 0, 1, 1)
        Gw2Ui.setCentralWidget(self.mainWidget)

        self.gridLayout_ui.addWidget(self.frameConfig, 0, 0, 1, 1)
        self.setAction()
        self.retranslateUi(Gw2Ui)
        QtCore.QMetaObject.connectSlotsByName(Gw2Ui)
        self.frameMain.show()
        self.frameConfig.hide()
        self.mainWidget.setFocus()

    def retranslateUi(self, Gw2Ui):
        # init ui text
        _translate = QtCore.QCoreApplication.translate
        Gw2Ui.setWindowTitle(_translate("Gw2Ui", "激战2双版本启动器 - by bingkong"))
        self.labelCurrentVersionTag.setText(_translate("Gw2Ui", "当前版本："))
        self.buttonSetEnGamePath.setText(_translate("Gw2Ui", "设置路径"))
        self.buttonBackEnFile.setText(_translate("Gw2Ui", "备份美服"))
        self.buttonResetChFile.setText(_translate("Gw2Ui", "恢复国服"))
        self.buttonExit.setText(_translate("Gw2Ui", "退出"))
        self.buttonBackChFile.setText(_translate("Gw2Ui", "备份国服"))
        self.buttonConfig.setText(_translate("Gw2Ui", "当前配置"))
        self.buttonResetEnFile.setText(_translate("Gw2Ui", "恢复美服"))
        self.buttonSetChGamePath.setText(_translate("Gw2Ui", "设置路径"))
        # 显示当前版本
        config = gw2Config()
        current = config.getCurrent()
        if current == 'ch':
            current = "国服"
        elif current == 'en':
            current = '美服'
        else:
            current = 'NULL'
        self.labelCurrentVersion.setText(_translate("Gw2Ui", current))

    def retranslateConfig(self, Gw2Ui):
        # init ui text
        _translate = QtCore.QCoreApplication.translate
        config = gw2Config()
        Gw2Ui.setWindowTitle(_translate("Gw2Ui", "激战2双版本启动器 - by bingkong"))
        self.labelGlobal.setText(_translate("Gw2Ui", "全局配置"))
        self.labelGlobalConfigPath.setText(_translate("Gw2Ui", "配置文件目录"))
        self.textGlobalConfigPath.setText(_translate("Gw2Ui", config.getConfigpath()))
        self.textGlobalConfigPath.setCursorPosition(0)
        self.labelGlobalCurrent.setText(_translate("Gw2Ui", "当前配置版本"))
        self.textGlobalCurrent.setText(_translate("Gw2Ui", config.getCurrent()))
        self.textGlobalCurrent.setCursorPosition(0)
        self.labelEn.setText(_translate("Gw2Ui", "美服"))
        (en_game_path, en_backfile_xml, en_backfile_dat) = config.getEnConfig()
        self.labelEnGamePath.setText(_translate("Gw2Ui", "游戏路径"))
        self.textEnGamePath.setText(_translate("Gw2Ui", en_game_path))
        self.textEnGamePath.setCursorPosition(0)
        self.labelEnXMLBackFile.setText(_translate("Gw2Ui", "XML备份文件"))
        self.textEnXMLBackFile.setText(_translate("Gw2Ui", en_backfile_xml))
        self.textEnXMLBackFile.setCursorPosition(0)
        self.labelEnDATBackFile.setText(_translate("Gw2Ui", "DAT备份文件"))
        self.textEnDATBackFile.setText(_translate("Gw2Ui", en_backfile_dat))
        self.textEnDATBackFile.setCursorPosition(0)
        self.labenCh.setText(_translate("Gw2Ui", "国服"))
        (ch_game_path, ch_backfile_xml, ch_backfile_dat) = config.getChConfig()
        self.labelChGamePath.setText(_translate("Gw2Ui", "游戏路径"))
        self.textChGamePath.setText(_translate("Gw2Ui", ch_game_path))
        self.textChGamePath.setCursorPosition(0)
        self.labenChXMLBackFile.setText(_translate("Gw2Ui", "XML备份文件"))
        self.textChXMLBackFile.setText(_translate("Gw2Ui", ch_backfile_xml))
        self.textChXMLBackFile.setCursorPosition(0)
        self.labelChDATBackFile.setText(_translate("Gw2Ui", "DAT备份文件"))
        self.textChDATBackFile.setText(_translate("Gw2Ui", ch_backfile_dat))
        self.textChDATBackFile.setCursorPosition(0)
        self.buttonConfigReturn.setText(_translate("Gw2Ui", "返回"))

    def setAction(self):
        # bind ui listener
        self.buttonSetChGamePath.clicked.connect(self.setChGamePath)
        self.buttonSetEnGamePath.clicked.connect(self.setEnGamePath)
        self.buttonRunEn.clicked.connect(self.runEnGame)
        self.buttonRunEn.pressed.connect(self.runEnGame_pressed)
        self.buttonRunEn.released.connect(self.runChGame_released)
        self.buttonRunCh.clicked.connect(self.runChGame)
        self.buttonRunCh.pressed.connect(self.runChGame_pressed)
        self.buttonRunCh.released.connect(self.runChGame_released)
        self.buttonBackChFile.clicked.connect(self.backChFile)
        self.buttonBackEnFile.clicked.connect(self.backEnFile)
        self.buttonResetChFile.clicked.connect(self.resetChFile)
        self.buttonResetEnFile.clicked.connect(self.resetEnFile)
        self.buttonExit.clicked.connect(self.exitsoft)
        self.buttonConfig.clicked.connect(self.showConfig)
        self.buttonConfig.clicked.connect(self.showConfig)
        self.buttonConfigReturn.clicked.connect(self.configReturnBack)

    def setChGamePath(self):
        # 设置国服路径动作
        # 打开文件选择框
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(
            self.MainWindow, "请选择国服Gw2-64.exe", "", "EXE Files (*.exe)")
        if fileName:
            # 判断文件
            fileName = os.path.normpath(fileName)
            if not fileName.endswith('Gw2-64.exe'):
                self.showMsgBox("ERROR", "请选择Gw2-64.exe文件")
                return
            # 保存配置
            config = gw2Config()
            config.setChGamePath(fileName)
            icon_ch = QtGui.QIcon()
            icon_ch.addPixmap(QtGui.QPixmap(getDefaultIcon("ch")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.buttonRunCh.setIcon(icon_ch)
            self.showMsgBox("SUCCESS", "国服游戏路径配置成功")

    def setEnGamePath(self):
        # 设置美服路径动作
        # 打开文件选择框
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(
            self.MainWindow, "请选择美服Gw2-64.exe", "", "EXE Files (*.exe)")
        if fileName:
            # 判断文件
            fileName = os.path.normpath(fileName)
            if not fileName.endswith('Gw2-64.exe'):
                self.showMsgBox("ERROR", "请选择Gw2-64.exe文件")
                return
            # 保存配置
            config = gw2Config()
            config.setEnGamePath(fileName)
            icon_en = QtGui.QIcon()
            icon_en.addPixmap(QtGui.QPixmap(getDefaultIcon("en")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.buttonRunEn.setIcon(icon_en)
            self.showMsgBox("SUCCESS", "美服游戏路径配置成功")

    def runChGame(self):
        # 启动国服游戏动作
        # 获取配置信息
        config = gw2Config()
        (en_game_path, en_backfile_xml, en_backfile_dat) = config.getEnConfig()
        (ch_game_path, ch_backfile_xml, ch_backfile_dat) = config.getChConfig()
        if not ch_game_path or not os.path.isfile(ch_game_path):
            # 未设置国服游戏路径
            self.showMsgBox("ERROR", '请先设置国服游戏路径!')
        else:
            runflag = True
            if config.getCurrent() == 'en' and (not en_backfile_xml or not en_backfile_dat):
                # 备份提醒
                reply = self.showChoseMsgBox("备份提醒", "您还未对当前版本进行备份，并正在尝试运行不同版本的客户端，确认运行将会重置当前配置文件")
                if reply == QtWidgets.QMessageBox.No:
                    runflag = False
            if runflag == True:
                # 启动游戏
                status, error = config.runChGame()
                if status == False:
                    self.showMsgBox("ERROR", "<p>启动失败</p><p>" + error + "</p>")
                subprocess.Popen([ch_game_path])
                sys.exit()
            

    def runChGame_pressed(self):
        # 按钮按下动作
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/logo/image/logo_ch_focus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonRunCh.setIcon(icon)

    def runChGame_released(self):
        # 按钮释放动作
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(getDefaultIcon("ch")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonRunCh.setIcon(icon)

    def runEnGame(self):
        # 启动美服游戏动作
        # 获取配置信息
        config = gw2Config()
        (en_game_path, en_backfile_xml, en_backfile_dat) = config.getEnConfig()
        (ch_game_path, ch_backfile_xml, ch_backfile_dat) = config.getChConfig()
        if not en_game_path or not os.path.isfile(en_game_path):
            # 未设置国服游戏路径
            self.showMsgBox("ERROR", '请先设置美服游戏路径!')
        else:
            runflag = True
            if config.getCurrent() == 'ch' and (not ch_backfile_xml or not ch_backfile_dat):
                # 备份提醒
                reply = self.showChoseMsgBox( "备份提醒", "您还未对当前版本进行备份，并正在尝试运行不同版本的客户端，确认运行将会重置当前配置文件")
                if reply == QtWidgets.QMessageBox.No:
                    runflag = False
            if runflag == True:
                # 启动游戏
                status, error = config.runEnGame()
                if status == False:
                    self.showMsgBox("ERROR", "<p>启动失败</p><p>" + error + "</p>")
                subprocess.Popen([en_game_path])
                sys.exit()

    def runEnGame_pressed(self):
        # 按钮按下动作
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/logo/image/logo_en_focus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonRunEn.setIcon(icon)

    def runEnGame_released(self):
        # 按钮释放动作
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(getDefaultIcon("en")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonRunEn.setIcon(icon)

    def backChFile(self):
        # 备份国服配置文件动作
        config = gw2Config()
        status, error = config.backupChFile()
        if status == True:
            # 备份成功
            _translate = QtCore.QCoreApplication.translate
            self.labelCurrentVersion.setText(_translate("Gw2Ui", "国服"))
            self.showMsgBox("SUCCESS", "国服配置文件备份成功")
        else:
            self.showMsgBox("ERROR", "<p>备份失败</p><p>" + error + "</p>")

    def backEnFile(self):
        # 备份美服配置文件动作
        config = gw2Config()
        status, error = config.backupEnFile()
        if status == True:
            # 备份成功
            _translate = QtCore.QCoreApplication.translate
            self.labelCurrentVersion.setText(_translate("Gw2Ui", "美服"))
            self.showMsgBox("SUCCESS", "美服配置文件备份成功")
        else:
            self.showMsgBox("ERROR", "<p>备份失败</p><p>" + error + "</p>")

    def resetChFile(self):
        # 恢复国服配置文件动作
        config = gw2Config()
        status, info, error = config.resetChFile()
        if status == True:
            # 恢复成功
            _translate = QtCore.QCoreApplication.translate
            self.labelCurrentVersion.setText(_translate("Gw2Ui", "国服"))
            self.showMsgBox("SUCCESS", info)
        else:
            self.showMsgBox("ERROR", "<p>" + info + "</p><p>" + error + "</p>")
    
    def resetEnFile(self):
        # 恢复美服配置文件动作
        config = gw2Config()
        status, info, error = config.resetEnFile()
        if status == True:
            # 恢复成功
            _translate = QtCore.QCoreApplication.translate
            self.labelCurrentVersion.setText(_translate("Gw2Ui", "美服"))
            self.showMsgBox("SUCCESS", info)
        else:
            self.showMsgBox("ERROR", "<p>" + info + "</p><p>" + error + "</p>")

    def showConfig(self):
        # 显示当前配置面板
        self.retranslateConfig(self.MainWindow)
        self.frameMain.hide()
        self.frameConfig.show()

    def configReturnBack(self):
        # 返回主界面动作
        self.frameMain.show()
        self.frameConfig.hide()
        self.mainWidget.setFocus()

    def exitsoft(self):
        # 退出程序动作
        sys.exit()

    def showMsgBox(self, status, msg):
        # 弹出消息提示框
        msgBox = QtWidgets.QMessageBox()
        msgBox.setWindowTitle(status)
        msgBox.setTextFormat(QtCore.Qt.RichText)
        if status == 'ERROR':
            msgBox.setIcon(QtWidgets.QMessageBox.Warning)
        elif status == 'SUCCESS':
            msgBox.setIcon(QtWidgets.QMessageBox.Information)
        msgBox.setText(msg)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Yes)
        buttonY = msgBox.button(QtWidgets.QMessageBox.Yes)
        buttonY.setText('  OK  ')
        msgBox.exec_()

    def showChoseMsgBox(self, title, msg):
        # 弹出选择提示框
        msgBox = QtWidgets.QMessageBox(self.MainWindow)
        msgBox.setWindowTitle(title)
        msgBox.setTextFormat(QtCore.Qt.RichText)
        msgBox.setIcon(QtWidgets.QMessageBox.Question)
        msgBox.setText(msg)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Yes|QtWidgets.QMessageBox.No)
        buttonY = msgBox.button(QtWidgets.QMessageBox.Yes)
        buttonY.setText('确定运行')
        buttonN = msgBox.button(QtWidgets.QMessageBox.No)
        buttonN.setText('返回备份')
        buttonN.setFocus()
        reply = msgBox.exec_()
        return reply
    
    def firstStart(self, lang):
        # 首次使用自动备份
        config = gw2Config()
        if lang == 'ch':
            status, error = config.backupChFile()
        else:
            status, error = config.backupEnFile()
        if status == True:
            self.showMsgBox("SUCCESS", "<p>已为您自动备份当前版本配置文件，请配置游戏路径</p><p>建议您在配置完路径后启动另一个版本的游戏，登录游戏设置完成后重新打开本软件并进行备份</p>")
        else:
            self.showMsgBox("ERROR", "<p>备份失败</p><p>" + error + "</p>")
        

class HoverButton(QtWidgets.QPushButton):
    # 鼠标经过特效
    def __init__(self, parent, lang):
        QtWidgets.QPushButton.__init__(self, parent)
        self.setMouseTracking(True)
        self.lang = lang

    def enterEvent(self, event):
        icon = QtGui.QIcon()
        if self.lang == "en":
            icon.addPixmap(QtGui.QPixmap(":/logo/image/logo_en_focus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        else:
            icon.addPixmap(QtGui.QPixmap(":/logo/image/logo_ch_focus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setIcon(icon)

    def leaveEvent(self, event):
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(getDefaultIcon(self.lang)), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setIcon(icon)

def getDefaultIcon(lang):
    # 动态获取LOGO
    config = gw2Config()
    if lang == 'ch':
        (ch_game_path, ch_backfile_xml, ch_backfile_dat) = config.getChConfig()
        if not ch_game_path or not os.path.isfile(ch_game_path):
            return ":/logo/image/logo_ch_disable.png"
        else:
            return ":/logo/image/logo_ch_default.png"
    else:
        (en_game_path, en_backfile_xml, en_backfile_dat) = config.getEnConfig()
        if not en_game_path or not os.path.isfile(en_game_path):
            return ":/logo/image/logo_en_disable.png"
        else:
            return ":/logo/image/logo_en_default.png"