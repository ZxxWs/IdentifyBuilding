import os

from PyQt5 import QtGui
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog

from Code.File import File
from GUI.Ui_train import Ui_Train
# from warning import Warning

class Train(QDialog, Ui_Train):

    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.setupUi(self)

        #获取项目配置信息
        self.__cfgFile = File()
        self.__dic = self.__cfgFile.cfgRead()

        self.__buttonTag=0#0表示未训练

        self.__initUI()

    @pyqtSlot()
    def on_pushButton_clicked(self):
        if self.__buttonTag==0:
            self.pushButton.setText("停止训练")
            self.__runTrain()
            self.__buttonTag=1
        else:
            self.pushButton.setText("开始训练")
            os.system("taskkill /f /im darknet.exe")
            self.__buttonTag=0


    def __runTrain(self):
       # darknet.exe  detector  train  data / obj.data  yolo - obj.cfg  yolov4.conv .137
        CMD = self.__dic['darknet'] + " detector train " + self.__dic['data'] + " " + self.__dic['cfg'] + " " + self.__dic['conv']
        print(CMD)

        os.popen(CMD)


    #退出界面触发的事件
    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        self.parent().show()

    def __initUI(self):
        batch=self.__cfgFile.getBatch()
        if batch!=-1:
            self.comboBox.setCurrentText(str(batch))
        else:
            self.__warning=Warning("batch错误",self)
            self.__warning.show()
            return

    @pyqtSlot(str)
    def on_comboBox_currentIndexChanged(self):
        batch = self.comboBox.currentText()

        self.__cfgFile.setBatch(batch)



