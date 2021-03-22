# from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QDialog

from PyQt5.QtCore import pyqtSlot, Qt

from Code.File.projectsManage import ProjectsManage
# from Code.MainUI import MainUI
from Code.MainUI import MainUI
from GUI.Ui_newProject import Ui_NewProject


class NewProject(QDialog, Ui_NewProject):

    # 让多窗口之间传递信号 刷新主窗口信息，int是指哪个界面是父界面，str是新建的项目名
    NewProjectSignal = QtCore.pyqtSignal(int,str)

    def __init__(self, father,parent=None):
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.father=father
        self.__setUIStyle()


    @pyqtSlot()
    def on_pushButtonOK_clicked(self):

        # --------------------------------------------此处未做输入验证——————————————————————————
        #获取用户输入的新建信息
        name = self.lineEdit.text()
        projectsManage = ProjectsManage()
        nameSet = projectsManage.getProjectsList()
        if name in nameSet:
            self.labelAlert.setText("该项目已存在，请更改项目名称")
            self.lineEdit.clear()
            return
        elif name is None:
            self.labelAlert.setText("请输入项目名")
            self.lineEdit.clear()
            return
        elif name=="":
            self.labelAlert.setText("项目名不能为空")
            self.lineEdit.clear()
            return
        else:
            projectsManage.newProject(name)
            #向父界面传递信号
            self.NewProjectSignal.emit(self.father,name)

            # self.project=MainUI(name)
            # self.project.show()

            # self.parent().close()

            # -----------此处可以设置为打开新的项目

        # --------------------------------------------此处未做输入验证——————————————————————————

        self.close()

    def closeEvent(self, event):

        # self.NewProjectSignal.emit("close")
        pass

    @pyqtSlot()
    def on_pushButtonCancel_clicked(self):

        self.close()
        pass

        # 本页面的UI设置

    def __setUIStyle(self):

        self.setWindowModality(Qt.ApplicationModal)  # 设置其他界面不可点击
        self.setFixedSize(self.width(), self.height())  # 固定界面尺寸

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
