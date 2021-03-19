from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow

from GUI.Ui_Main import Ui_MainWindow
from Code.configurate import Configurate
from Code.mark import Mark
from Code.train import Train
from Code.test import Test


class MainUI(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.setupUi(self)

    # 打开配置界面
    @pyqtSlot()
    def on_actionCfg_triggered(self):
        self.cfgUI = Configurate()
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
