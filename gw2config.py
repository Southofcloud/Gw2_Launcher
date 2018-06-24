import re
import os
import configparser
import sys
import subprocess
from shutil import copyfile

class gw2Config:
    def __init__(self):
        self.cp = configparser.ConfigParser()
        self.ini = os.path.join(os.path.abspath("."), "Gw2Config.ini")
        self.cp.read(self.ini)
        # read global config
        self.configpath = self.cp.get('global', 'configpath') # 游戏配置路径
        self.current = self.cp.get('global', 'current') # 当前版本
        # read en config
        self.en_game_path = self.cp.get('en', 'game_path') # 美服游戏路径
        self.en_backfile_xml = self.cp.get('en', 'backfile_xml') # 美服XML备份文件
        self.en_backfile_dat = self.cp.get('en', 'backfile_dat') # 美服DAT备份文件
        # read ch config
        self.ch_game_path = self.cp.get('ch', 'game_path') # 国服游戏路径
        self.ch_backfile_xml = self.cp.get('ch', 'backfile_xml') # 国服XML备份文件
        self.ch_backfile_dat = self.cp.get('ch', 'backfile_dat') # 国服DAT备份文件
        # get game config
        self.xmlpath = os.path.join(self.configpath, "GFXSettings.Gw2-64.exe.xml") # 游戏XML配置文件
        self.datpath = os.path.join(self.configpath, "Local.dat") # 游戏DAT配置文件

    def getConfigpath(self):
        # 获取游戏配置路径
        return self.configpath

    def setConfigpath(self, configpath):
        # 设置游戏配置路径
        self.configpath = configpath
        self.cp.set("global", "configpath", configpath)
        self.save()

    def getCurrent(self):
        # 获取当前版本
        return self.current

    def setCurrent(self, current):
        # 设置当前版本
        self.current = current
        self.cp.set("global", "current", current)
        self.save()

    def getEnConfig(self):
        # 获取美服配置信息
        return (self.en_game_path, self.en_backfile_xml, self.en_backfile_dat)

    def setEnGamePath(self, en_game_path):
        # 设置美服游戏路径
        self.en_game_path = en_game_path
        self.cp.set("en", "game_path", en_game_path)
        self.save()

    def backupEnFile(self):
        # 备份美服配置文件
        try:
            # 默认备份路径
            if not self.en_backfile_xml:
                self.en_backfile_xml = os.path.join(self.configpath, "Gw2_Launcher_En.GFXSettings.Gw2-64.exe.xml")
            if not self.en_backfile_dat:
                self.en_backfile_dat = os.path.join(self.configpath, "Gw2_Launcher_En.Local.dat")
            # 拷贝配置文件
            copyfile(self.xmlpath, self.en_backfile_xml)
            copyfile(self.datpath, self.en_backfile_dat)
            # 保存配置信息
            self.cp.set("en", "backfile_xml", self.en_backfile_xml)
            self.cp.set("en", "backfile_dat", self.en_backfile_dat)
            self.save()
            # 设置当前版本
            self.setCurrent('en')
            return True, None
        except Exception as e:
            return False, str(e)


    def resetEnFile(self):
        # 恢复美服配置文件
        try:
            # 未备份,还原失败
            if not self.en_backfile_xml or not self.en_backfile_dat or not os.path.isfile(self.en_backfile_xml) or not os.path.isfile(self.en_backfile_dat):
                return False, "配置文件还原失败", "未备份美服配置文件，请先启动游戏并备份配置文件"
            # 拷贝配置文件
            copyfile(self.en_backfile_xml, self.xmlpath)
            copyfile(self.en_backfile_dat, self.datpath)
            # 设置当前版本
            self.setCurrent('en')
            return True, "配置文件还原成功", None
        except Exception as e:
            return False, "配置文件还原失败", str(e)

    def runEnGame(self):
        # 启动美服游戏
        try:
            # 版本不同时自动恢复配置文件并切换版本信息
            if self.current != 'en':
                if self.en_backfile_xml and self.en_backfile_dat and os.path.isfile(self.en_backfile_xml) and os.path.isfile(self.en_backfile_dat):
                    copyfile(self.en_backfile_xml, self.xmlpath)
                    copyfile(self.en_backfile_dat, self.datpath)
                self.setCurrent('en')
            return True, None
        except Exception as e:
            return False, str(e)

    def getChConfig(self):
        # 获取国服配置信息
        return (self.ch_game_path, self.ch_backfile_xml, self.ch_backfile_dat)

    def setChGamePath(self, ch_game_path):
        # 设置国服游戏路径
        self.ch_game_path = ch_game_path
        self.cp.set("ch", "game_path", ch_game_path)
        self.save()

    def backupChFile(self):
        # 备份国服配置文件
        try:
            # 默认备份路径
            if not self.ch_backfile_xml:
                self.ch_backfile_xml = os.path.join(self.configpath, "Gw2_Launcher_Ch.GFXSettings.Gw2-64.exe.xml")
            if not self.ch_backfile_dat:
                self.ch_backfile_dat = os.path.join(self.configpath, "Gw2_Launcher_Ch.Local.dat")
            # 拷贝配置文件
            copyfile(self.xmlpath, self.ch_backfile_xml)
            copyfile(self.datpath, self.ch_backfile_dat)
            # 保存配置信息
            self.cp.set("ch", "backfile_xml", self.ch_backfile_xml)
            self.cp.set("ch", "backfile_dat", self.ch_backfile_dat)
            self.save()
            # 设置当前版本
            self.setCurrent('ch')
            return True, None
        except Exception as e:
            return False, str(e)

    def resetChFile(self):
        # 恢复国服配置文件
        try:
            # 未备份,还原失败
            if not self.ch_backfile_xml or not self.ch_backfile_dat or not os.path.isfile(self.ch_backfile_xml) or not os.path.isfile(self.ch_backfile_dat):
                return False, "配置文件还原失败", "未备份国服配置文件，请先启动游戏并备份配置文件"
            # 拷贝配置文件
            copyfile(self.ch_backfile_xml, self.xmlpath)
            copyfile(self.ch_backfile_dat, self.datpath)
            # 设置当前版本
            self.setCurrent('ch')
            return True, "配置文件还原成功", None
        except Exception as e:
            return False, "配置文件还原失败", str(e)

    def runChGame(self):
        # 启动美服游戏
        try:
            # 版本不同时自动恢复配置文件并切换版本信息
            if self.current != 'ch':
                if self.ch_backfile_xml and self.ch_backfile_dat and os.path.isfile(self.ch_backfile_xml) and os.path.isfile(self.ch_backfile_dat):
                    copyfile(self.ch_backfile_xml, self.xmlpath)
                    copyfile(self.ch_backfile_dat, self.datpath)
                self.setCurrent('ch')
            return True, None
        except Exception as e:
            return False, str(e)
    
    def save(self):
        # 保存配置信息
        self.cp.write(open(self.ini, "w"))