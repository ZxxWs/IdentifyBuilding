import os

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QDialog
import webbrowser
from PyQt5.QtCore import pyqtSlot, Qt
from GUI.Ui_about import Ui_About


class About(QDialog, Ui_About):

    def __init__(self, tag, parent=None):
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.__initLabel()
        self.__setUIStyle()

    @pyqtSlot()
    def on_commandLinkButton_clicked(self):
        print("open github")
        webbrowser.open("https://github.com/ZxxWs/IdentifyBuilding")  # 打开GitHub网址

    def __initLabel(self):
        inforFile = os.getcwd() + "\\Data\\aboutInfor.txt"
        with open(inforFile, 'r', encoding="utf8") as file:
            infor = file.read()
            self.label.setText(infor)
            file.close()

    def __setUIStyle(self):
        self.setWindowModality(Qt.ApplicationModal)  # 设置其他界面不可点击

        self.setWindowIcon(QIcon('ArtRes/about.png'))
        self.setStyleSheet("QDialog{background-image:url(ArtRes/backgroudBlack.png)}"
                           "QCommandLinkButton{color:#F5FFFA}"
                           "QLabel{background-color:rgb(0,0,0,155)}"
                           "QLabel{font-size:26px}"
                           "QLabel{color:#F5FFFA}"
                           "QLabel{border-radius: 17px}"
                           )
