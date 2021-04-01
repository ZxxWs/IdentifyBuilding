import os
import shutil

from PyQt5 import QtGui
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QDialog

from Code.File.cfgFile import CfgFile
from Code.File.settingYoloObjCfg import SettingYoloObjCfg
from GUI.Ui_train import Ui_Train


class Train(QDialog, Ui_Train):

    def __init__(self, projectName, parent=None):
        QDialog.__init__(self, parent)
        self.setupUi(self)

        # 获取项目配置信息
        cfgFile = CfgFile()
        self.cfgDic = cfgFile.cfgRead()
        self.projectPath = self.cfgDic['darknet'] + '/projects/' + projectName + '/'  # 项目路径链接
        self.markPath = self.cfgDic['Yolo_mark'] + '/projects/' + projectName + '/img/'  # 用于转存文件的mark项目路径
        self.settingYoloObjCfg = SettingYoloObjCfg(projectName)
        self.projectName = projectName
        self.__isTrainTag = False  # 0表示未训练
        self.__initTag = True  # 此tag为真时表示界面是初始化，comboBox不调用

        self.__initUIData()
        self.__setUIStyle()

    @pyqtSlot()
    def on_pushButtonTrain_clicked(self):

        if self.__isTrainTag:
            self.pushButtonTrain.setText("开始训练")
            os.system("taskkill /f /im darknet.exe")
            self.__lockUI(False)
            self.__isTrainTag = False
        else:
            self.pushButtonTrain.setText("停止训练")
            self.__lockUI(True)
            self.__loadingJPG()
            self.__runTrain()
            self.__isTrainTag = True

    @pyqtSlot()
    def on_pushButtonBack_clicked(self):
        os.system("taskkill /f /im darknet.exe")
        self.close()

    @pyqtSlot()
    def on_pushButtonOpenDir_clicked(self):

        fileDir = self.projectPath + 'train/'
        f = str(fileDir).replace("/", '\\')
        if not os.path.exists(f):
            os.makedirs(f)
        os.system("start explorer " + f)

    @pyqtSlot()
    # 此处文件转存方式太低级
    def on_pushButtonMove_clicked(self):

        fileList = os.listdir(self.markPath)
        for file in fileList:
            shutil.copy(self.markPath + file, self.projectPath + "train")
        print("转存完成")
        self.loadingJPG()

    def __runTrain(self):
        CMD = self.cfgDic[
                  "darknet"] + "/darknet.exe detector train " + self.projectPath + "obj.data " + self.projectPath + "yolo-obj.cfg " + \
              self.cfgDic["conv"]

        os.popen(CMD)

    @pyqtSlot(str)
    def on_comboBoxBatch_currentIndexChanged(self, batch):
        if self.__initTag:
            return
        self.settingYoloObjCfg.setBatch(batch)

    @pyqtSlot(str)
    def on_comboBoxSubdivision_currentIndexChanged(self, subdivision):
        if self.__initTag:
            return

        self.settingYoloObjCfg.setSubdivisions(int(subdivision))

    # 退出界面触发的事件
    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        os.system("taskkill /f /im darknet.exe")
        self.parent().show()

    def __loadingJPG(self):
        prefix = self.projectPath + "train/"  # 填写的前缀
        with open(self.projectPath + 'train.txt', 'w') as trainTXT:
            fileNames = os.listdir(self.projectPath + "train/")

            for fileName in fileNames:
                if fileName[-4:] == ".jpg":
                    trainTXT.write(prefix + fileName + "\n")
            trainTXT.close()

    def __initUIData(self):

        txt = "请在" + self.projectPath + "train/文件夹下放置训练集"
        self.labelOpen.setText(txt)
        self.labelOpen.setWordWrap(True)

        batch = self.settingYoloObjCfg.getBatch()
        subdivisions = self.settingYoloObjCfg.getSubdivisions()

        self.comboBoxBatch.setCurrentText(str(batch))
        self.comboBoxSubdivision.setCurrentText(str(subdivisions))

        self.__initTag = False

    # 在执行训练函数后锁定一些UI，禁止点击或改动。如果介绍训练，则可以改动、点击.tag为bool
    def __lockUI(self, tag=True):

        self.pushButtonOpenDir.setDisabled(tag)
        self.pushButtonMove.setDisabled(tag)
        self.comboBoxBatch.setDisabled(tag)
        self.comboBoxSubdivision.setDisabled(tag)

    def __setUIStyle(self):

        self.setWindowIcon(QIcon('ArtRes/mark.png'))

        self.setWindowState(Qt.WindowMaximized)
        self.setStyleSheet("QLabel{background-color:rgb(0,0,0,155)}"
                           "QLabel{color:#F5FFFA}"
                           "QLabel{border-radius: 17px}"
                           "QLabel{font-size:35px;font-family:'楷体'}"
                           "QComboBox{border-radius:17px}"
                           )
        self.pushButtonTrain.setIcon(QIcon("ArtRes/start.png"))
        self.pushButtonOpenDir.setIcon(QIcon("ArtRes/file.png"))
        self.pushButtonBack.setIcon(QIcon("ArtRes/Cancel.png"))
        self.pushButtonMove.setIcon(QIcon("ArtRes/move.png"))
        self.pushButtonMove.setToolTip("将标注好的文件转移到此文件夹下")