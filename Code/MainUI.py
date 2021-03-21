# from PyQt5 import Qt, QtCore
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtGui import QIcon, QPalette, QColor
from PyQt5.QtWidgets import QMainWindow


from GUI.Ui_Main import Ui_MainWindow
from Code.configurate import Configurate
from Code.mark import Mark
from Code.train import Train
from Code.test import Test


class MainUI(QMainWindow, Ui_MainWindow):

    def __init__(self,projectName,parent=None):
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.projectName=projectName
        self.__setUIStyle()

    # 打开配置界面
    @pyqtSlot()
    def on_actionCfg_triggered(self):
        self.cfgUI = Configurate(self)
        self.cfgUI.show()


    # 打开标注界面
    @pyqtSlot()
    def on_pushButtonMark_clicked(self):
        self.mark = Mark(self)
        self.mark.show()
        self.hide()

    # 打开训练界面
    @pyqtSlot()
    def on_pushButtonTrain_clicked(self):
        self.train = Train(self)
        self.train.show()
        self.hide()

    # 打开测试界面
    @pyqtSlot()
    def on_pushButtonTest_clicked(self):
        self.test = Test(self)
        self.test.show()
        self.hide()


    def __setUIStyle(self):


        self.setWindowIcon(QIcon('ArtRes/main.png'))
        self.setWindowTitle("图像识别系统——"+self.projectName)
        self.setStyleSheet("QMainWindow{background-image:url(ArtRes/backgroud.jpg)}"
                            "QDialog{background-image:url(ArtRes/backgroud.jpg)}"
                            "QPushButton{background:#afb4db;border-radius:5px;}QPushButton:hover{background:#9AFF9A;}" 
                            "QPushButton{font-size:35px;font-family:'楷体'}"
                            "QTableWidget{background:#C4C4C4}"
                           )

        self.pushButtonMark.setIcon(QIcon("ArtRes/mark.png"))
        self.pushButtonTrain.setIcon(QIcon("ArtRes/train.png"))
        self.pushButtonTest.setIcon(QIcon("ArtRes/test.png"))
        self.actionCfg.setIcon(QIcon("ArtRes/setting.png"))
        self.actiongAbout.setIcon(QIcon("ArtRes/about.png"))
        self.setWindowState(Qt.WindowMaximized)