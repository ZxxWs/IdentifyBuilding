import os
import PyQt5
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog
from Code.File import File
from GUI.Ui_test import Ui_Test


class Test(QDialog, Ui_Test):

    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.progressBar.hide()

    def __RunTest(self, dic, image):

        '''原命令darknet.exe detector test data/obj.data yolo-obj.cfg yolo-obj_8000.weights'''

        CMD = dic['darknet'] + " detector test " + dic['data'] + " " + dic['cfg'] + " " + dic['weights'] + " " + image

        getOut = os.popen(CMD)

    @pyqtSlot()
    def on_pushButtonSelect_clicked(self):

        # self.progressBar.hide()
        # self.progressBar.setValue(0)
        pass
        try:
            self.imageName, self.imgType = QtWidgets.QFileDialog.getOpenFileName(self, "选取文件", "",
                                                                                 "*.jpg;;*.png;;All Files(*)")  # 这一行代码是网上找的，并未细看

            self.lineEdit.setText(self.imageName)
            jpg = QtGui.QPixmap(self.imageName)  # 通过文件路径获取图片文件，并设置图片长宽为label控件的长款
            self.labelImage.setPixmap(jpg)  # 在label控件上显示选择的图片
            self.labelImage.setScaledContents(True)
        #
        except:
            self.labelImage.settetxt("文件选取有误")

    @pyqtSlot()
    def on_pushButtonTest_clicked(self):

        try:
            image = str(self.lineEdit.text())
            print(image)

            cfgFile = File()
            dic = cfgFile.cfgRead()
            self.__RunTest(dic, image)
        except:
            print("测试错误")

    def closeEvent(self, a0: PyQt5.QtGui.QCloseEvent) -> None:
        self.parent().show()
