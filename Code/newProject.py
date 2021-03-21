# from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QDialog

from PyQt5.QtCore import pyqtSlot, Qt

from Code.File.projectsManage import ProjectsManage
from Code.MainUI import MainUI
from GUI.Ui_newProject import Ui_NewProject


class NewProject(QDialog, Ui_NewProject):

    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.__setUIStyle()

        # self.p=parent


    @pyqtSlot()
    def on_pushButtonOK_clicked(self):


        #--------------------------------------------此处未做输入验证——————————————————————————

        name = self.lineEdit.text()
        projectsManage=ProjectsManage()
        nameSet=projectsManage.getProjectsList()
        if name in nameSet:
            self.labelAlert.setText("该项目已存在，请更改项目名称")
            self.lineEdit.clear()

            return
        else:

            projectsManage.newProject(name)

            self.project=MainUI(name)
            self.project.show()

            self.parent().close()


            #-----------此处可以设置为打开新的项目

        #--------------------------------------------此处未做输入验证——————————————————————————


        self.close()



    @pyqtSlot()
    def on_pushButtonCancel_clicked(self):

        self.close()
        pass

        # 本页面的UI设置

    def __setUIStyle(self):

        self.setWindowModality(Qt.ApplicationModal)#设置其他界面不可点击
        self.setFixedSize(self.width(),self.height())#固定界面尺寸

        self.setStyleSheet("QLabel{background-color:rgb(255,255,255,0);border-radius: 9px;}"
                           "QLabel{color:#F5FFFA}"
                           "QLabel{font-size:24px;font-family:'楷体'}"
                           "QPushButton{background:#afb4db;border-radius:5px;}QPushButton:hover{background:#9AFF9A;}"
                           "QPushButton{font-size:35px;font-family:'楷体'}"
                           "QDialog{background-image:url(ArtRes/backgroudBlack.png)}"
                           "QLineEdit{border-radius:3px}"
                           )
        self.setWindowIcon(QIcon('ArtRes/addName.png'))
        self.pushButtonCancel.setIcon(QIcon("ArtRes/Cancel.png"))
        self.pushButtonOK.setIcon(QIcon("ArtRes/OK.png"))