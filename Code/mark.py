import os

from PyQt5 import QtGui
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog

from Code.File import File
from GUI.Ui_mark import Ui_Mark


class Mark(QDialog, Ui_Mark):

    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.setupUi(self)

        #获取项目配置信息
        self.__cfgFile = File()
        self.__dic = self.__cfgFile.cfgRead()

        self.buttonTag=0#tag=0时，表示未运行标注程序


    @pyqtSlot()
    def on_pushButton_clicked(self):

        if self.buttonTag==0:
            self.__runMark()
            self.buttonTag=1
            self.pushButton.setText("停止标注")
        elif self.buttonTag==1:
            os.system("taskkill /f /im yolo_mark.exe")
            self.buttonTag=0
            self.pushButton.setText("开始标注")
            pass


    def __runMark(self):
        # 传过来的参数是mark_cmd
        path = self.__dic['Yolo_mark']
        CMD = ""
        # 如果目录不是C盘，则需要更换盘符
        if path[0] != 'c' or path[0] != 'C':
            CMD = path[0] + ": &"

        CMD += "CD " + path + "&" + " yolo_mark.exe data/img data/train.txt data/obj.names"
        print(CMD)
        os.popen(CMD)


    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        self.parent().show()

