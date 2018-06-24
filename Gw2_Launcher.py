import re
import os
import configparser
import sys
import subprocess
from shutil import copyfile
from layout_main import Ui_Gw2Ui
from layout_version import Ui_Gw2Version
import qdarkstyle
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import *
from gw2config import gw2Config

def ini_init(inipath):
    # 生成配置信息文件Gw2Config.ini
    with open(inipath, 'w') as f:
        f.write('''[global]
configpath = 
current = 

[en]
game_path = 
backfile_xml = 
backfile_dat = 

[ch]
game_path = 
backfile_xml = 
backfile_dat = ''')


if __name__ == "__main__":
    # init
    app = QApplication(sys.argv)
    ini = os.path.join(os.path.abspath("."), "Gw2Config.ini")
    if not os.path.isfile(ini):
        # 配置信息文件Gw2Config.ini丢失
        error_dialog = QErrorMessage()
        app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
        msgBox = QMessageBox()
        msgBox.setWindowTitle("ERROR")
        msgBox.setTextFormat(QtCore.Qt.RichText)
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("<p>Gw2Config.ini文件缺失</p><p>将为您重新生成配置文件</p>")
        msgBox.setStandardButtons(QMessageBox.Yes)
        buttonY = msgBox.button(QMessageBox.Yes)
        buttonY.setText('  OK  ')
        msgBox.exec_()
        ini_init(ini)
    # 读取配置信息
    config = gw2Config()
    configpath = config.getConfigpath()
    current = config.getCurrent()
    if not configpath:
        # 未设置游戏配置路径，自动设置
        appdata = os.getenv('APPDATA')
        configpath = os.path.join(appdata, 'Guild Wars 2')
        config.setConfigpath(configpath)

    # create the application and the main window
    window_main = QMainWindow()
    ui_main = Ui_Gw2Ui()
    ui_main.setupUi(window_main)
    window_version = QMainWindow()
    ui_version = Ui_Gw2Version()
    ui_version.setupUi(window_version, window_main, ui_main)
    
    # setup stylesheet
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    
    # run
    if not current:
        # 首次使用，选择当前版本
        window_main.hide()
        window_version.show()
    else:
        window_main.show()
        window_version.hide()
    
    app.exec_()

