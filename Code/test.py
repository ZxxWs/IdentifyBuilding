import os
import time
# from myThreadading import Thread

import PyQt5
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QDialog

from Code.Thread.runCMD import RunCMD
from GUI.Ui_test import Ui_Test

from Code.File.cfgFile import CfgFile


class Test(QDialog, Ui_Test):

    def __init__(self, projectName, parent=None):
        QDialog.__init__(self, parent)
        self.setupUi(self)

        # 获取项目配置信息
        cfgFile = CfgFile()
        self.cfgDic = cfgFile.cfgRead()
        self.projectPath = self.cfgDic['darknet'] + '/projects/' + projectName + '/'  # 项目路径链接

        self.projectName = projectName
        self.weight = ""
        self.__initComboBox()
        self.__initLabel()
        self.__setUIStyle()

    @pyqtSlot()
    def on_pushButtonSelect_clicked(self):

        try:
            self.imageName, self.imgType = QtWidgets.QFileDialog.getOpenFileName(self, "选取文件",
                                                                                 self.projectPath + 'test/',
                                                                                 "*.jpg;;*.png;;All Files(*)")  # 这一行代码是网上找的，并未细看

            self.lineEdit.setText(self.imageName)
            jpg = QtGui.QPixmap(self.imageName)  # 通过文件路径获取图片文件，并设置图片长宽为label控件的长款
            self.labelImage.setPixmap(jpg)  # 在label控件上显示选择的图片
            self.labelImage.setScaledContents(True)

        except:
            self.labelImage.settetxt("文件选取有误")

    @pyqtSlot()
    def on_pushButtonOpenDir_clicked(self):
        fileDir = self.projectPath + 'test/'
        f = str(fileDir).replace("/", '\\')
        if not os.path.exists(f):
            os.makedirs(f)
        os.system("start explorer " + f)

    @pyqtSlot()
    def on_pushButtonWeight_clicked(self):
        self.__lockUI(True)  # 点击按钮后锁住UI
        self.__loadingJPG()
        CMD = self.cfgDic[
                  'darknet'] + "/darknet.exe detector map " + self.projectPath + "obj.data " + self.projectPath + "yolo-obj.cfg " + self.projectPath + "backup/" + self.weight
        print(CMD)

        self.myThread = RunCMD(CMD, -12, -4)
        self.myThread.RunCMDSignal.connect(self.__getWeight)
        self.myThread.start()

    @pyqtSlot()
    def on_pushButtonTest_clicked(self):

        self.__lockUI(True)  # 点击按钮后锁住UI
        try:
            image = str(self.lineEdit.text())
            '''原命令darknet.exe detector test data/obj.data yolo-obj.cfg yolo-obj_8000.weights'''

            '''此处的CMD命令不能是绝对路径，应该先CD一下路径'''
            darknetpath = self.cfgDic['darknet']
            if darknetpath[0] != 'C' or darknetpath[0] != 'c':
                CMD = darknetpath[0] + ":& cd " + darknetpath + " & "
            else:
                CMD = "cd " + darknetpath + ' & '

            CMD += "darknet.exe detector test " + self.projectPath + "obj.data " + self.projectPath + "yolo-obj.cfg " + self.projectPath + "backup/" + self.weight + " " + image

            print(CMD)
            self.myThread = RunCMD(CMD)
            self.myThread.RunCMDSignal.connect(self.__getTest)
            self.myThread.start()
            # time.sleep(5)
            self.__lockUI(False)
        except:
            print("测试错误")
            self.__lockUI(False)

    @pyqtSlot()
    def on_pushButtonBack_clicked(self):
        self.close()

    @pyqtSlot(str)
    def on_comboBoxWeight_currentIndexChanged(self, weight):
        self.weight = weight

    def closeEvent(self, a0: PyQt5.QtGui.QCloseEvent) -> None:

        os.system("taskkill /f /im darknet.exe")
        self.parent().show()


    #初始化下拉列表（权重文件的下拉列表
    def __initComboBox(self):
        weightList = os.listdir(self.projectPath + "backup/")
        #如果没有权重文件，则锁住UI
        if len(weightList)==0:
            self.__lockUI(True)
            txt="未检测到权重文件,请先训练权重或者将权重文件放于"+self.projectPath+"backup/文件夹下再刷新此界面"
            self.labelImage.setText(txt)
            return

        self.comboBoxWeight.addItems(weightList)

    def __initLabel(self):
        txt = "将测试集文件放置于" + self.projectPath + "test/文件夹下"
        self.labelOpenDir.setText(txt)

    # 在执行训练函数后锁定一些UI，禁止点击或改动。如果介绍训练，则可以改动、点击.tag为bool
    def __lockUI(self, tag=True):
        self.pushButtonSelect.setDisabled(tag)
        # self.pushButtonBack.setDisabled(tag)
        self.pushButtonWeight.setDisabled(tag)
        self.pushButtonTest.setDisabled(tag)
        self.pushButtonOpenDir.setDisabled(tag)
        self.lineEdit.setDisabled(tag)
        self.comboBoxWeight.setDisabled(tag)

    def __loadingJPG(self):
        prefix = self.projectPath + "test/"  # 填写的前缀
        with open(self.projectPath + 'test.txt', 'w') as testTXT:
            fileNames = os.listdir(self.projectPath + "test/")
            for fileName in fileNames:
                if fileName[-4:] == ".jpg":
                    testTXT.write(prefix + fileName + "\n")
            testTXT.close()

    # 获取执行CMD后的数据
    def __getWeight(self, content):
        print("线程结束")
        if content == "":
            # 子线程刚执行
            txt = "程序加载中，请稍等......"
            self.labelImage.setText(txt)
        else:
            self.labelImage.setText(content)
            self.__lockUI(False)

    # 获取执行CMD后的数据---------------------------------废弃代码，但不能删除，因为执行test的时候需要主动使用多线程，但却又不能主动返回数据
    def __getTest(self, content):

        if content == "":
            # 子线程刚执行
            # txt = "程序加载中，请稍等......"
            # self.labelImage.setText(txt)
            pass
        else:
            print(content)
            self.__lockUI(False)


    #本页面UI格式控制
    def __setUIStyle(self):

        self.setWindowIcon(QIcon('ArtRes/mark.png'))

        self.setWindowState(Qt.WindowMaximized)
        self.setStyleSheet("QLabel{background-color:rgb(0,0,0,155)}"
                           "QLabel{color:#F5FFFA}"
                           "QLabel{border-radius: 17px}"
                           "QLabel{font-size:25px;font-family:'楷体'}")
        self.label.setStyleSheet("QLabel{background-color:rgb(0,0,0,155)}"
                                 "QLabel{color:#F5FFFA}"
                                 "QLabel{border-radius: 17px}"
                                 "QLabel{font-size:35px;font-family:'楷体'}")
        self.lineEdit.setStyleSheet("QLineEdit{background-color:rgb(0,0,0,155)}"
                                    "QLineEdit{color:#F5FFFA}"
                                    "QLineEdit{border-radius: 17px}"
                                    "QLineEdit{font-size:20px;font-family:'楷体'}")
        self.labelWeight.setStyleSheet("QLabel{background-color:rgb(0,0,0,155)}"
                                       "QLabel{color:#F5FFFA}"
                                       "QLabel{border-radius: 17px}"
                                       "QLabel{font-size:35px;font-family:'楷体'}")
        self.comboBoxWeight.setStyleSheet("QComboBox{border-radius: 4px}"
                                          "QComboBox{font-size:35px;font-family:'楷体'}"
                                          "QComboBox{text-align:centre}"
                                          )
        self.labelImage.setWordWrap(True)
        self.pushButtonTest.setIcon(QIcon("ArtRes/start.png"))
        self.pushButtonSelect.setIcon(QIcon("ArtRes/file.png"))
        self.pushButtonBack.setIcon(QIcon("ArtRes/Cancel.png"))
