# from PyQt5 import Qt, QtCore
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtGui import QIcon, QPalette, QColor
from PyQt5.QtWidgets import QMainWindow

from Code.about import About
from Code.configurate import Configurate
from Code.newProject import NewProject
from Code.openProject import OpenProject
from GUI.Ui_Main import Ui_MainWindow
from Code.mark import Mark
from Code.train import Train
from Code.test import Test


class MainUI(QMainWindow, Ui_MainWindow):

    def __init__(self, projectName, parent=None):
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.projectName = projectName
        self.__setUIStyle()



    # 打开新建项目界面
    @pyqtSlot()
    def on_actionNewProject_triggered(self):
        self.newProject = NewProject(2)
        self.newProject.NewProjectSignal.connect(self.getNewProjectSignal)  # 将子界面的信号量和本类中的方法绑定
        self.newProject.show()
        pass

    # 打开打开项目界面
    @pyqtSlot()
    def on_actionOpenProject_triggered(self):
        print("打开项目")
        self.openProject = OpenProject()
        self.openProject.OpenProjectSignal.connect(self.getOpenProjectSignal)  # 将子界面的信号量和本类中的方法绑定
        self.openProject.show()

    # 打开配置界面
    @pyqtSlot()
    def on_actionCfg_triggered(self):
        self.cfgUI = Configurate(self)
        self.cfgUI.show()

    # 打开关于界面
    @pyqtSlot()
    def on_actiongAbout_triggered(self):
        self.about = About(self)
        self.about.show()

    # 打开标注界面
    @pyqtSlot()
    def on_pushButtonMark_clicked(self):
        self.mark = Mark(self.projectName, self)
        self.mark.show()
        self.hide()

    # 打开训练界面
    @pyqtSlot()
    def on_pushButtonTrain_clicked(self):
        self.train = Train(self.projectName, self)
        self.train.show()
        self.hide()

    # 打开测试界面
    @pyqtSlot()
    def on_pushButtonTest_clicked(self):
        self.test = Test(self.projectName, self)
        self.test.show()
        self.hide()

    def getNewProjectSignal(self, tag, name):
        if tag == 2:
            self.projectName = name
            self.setWindowTitle("图像识别系统——" + self.projectName)
            # self.MainUi = MainUI(name)
            # self.MainUi.show()
            # self.close()

    def getOpenProjectSignal(self, name):
        self.projectName = name
        self.setWindowTitle("图像识别系统——" + self.projectName)

    def __setUIStyle(self):
        self.setWindowIcon(QIcon('ArtRes/main.png'))
        self.setWindowTitle("图像识别系统——" + self.projectName)
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
        self.actionNewProject.setIcon(QIcon("ArtRes/newProject.png"))
        self.actionOpenProject.setIcon(QIcon("ArtRes/openProject.png"))
        self.setWindowState(Qt.WindowMaximized)
