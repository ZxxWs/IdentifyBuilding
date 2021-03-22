import sys

from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QDialog, QHeaderView, QPushButton, QApplication

from Code.File.projectsManage import ProjectsManage
# from Code.MainUI import MainUI
from Code.MainUI import MainUI
from Code.configurate import Configurate
from Code.confirmAlert import ConfirmAlert
from Code.newProject import NewProject
from GUI.Ui_navigate import Ui_Navigate


# import main as mainCode


# from warning import Warning

class Navigate(QDialog, Ui_Navigate):

    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.projectsManage = ProjectsManage()
        self.projectList = self.projectsManage.getProjectsList()

        self.initTable()
        self.__setUIStyle()

    @pyqtSlot()
    def on_pushButtonNew_clicked(self):

        self.newProject = NewProject(1, self)  # 此处传入的参数1，用于接收返回值
        self.newProject.NewProjectSignal.connect(self.getNewProjectSignal)  # 将子界面的信号量和本类中的方法绑定
        self.newProject.show()

    @pyqtSlot()
    def on_pushButtonSetting_clicked(self):

        Cfg = Configurate(self)
        Cfg.show()

    def initTable(self):

        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeToContents)
        self.tableWidget.verticalHeader().setVisible(False)  # 隐藏垂直表头
        self.tableWidget.horizontalHeader().setVisible(False)  # 隐藏水平表头

        rowCount = len(self.projectList)
        self.tableWidget.setRowCount(rowCount)

        i = 0
        for pro in self.projectList:
            # 向表格中填充按钮
            buttonOpen = QPushButton(pro)
            buttonDel = QPushButton()

            buttonDel.setIcon(QIcon("ArtRes/del.png"))
            buttonOpen.clicked.connect(self.buttonOpen_clicked)
            buttonDel.clicked.connect(self.buttonDel_clicked)
            self.tableWidget.setCellWidget(i, 0, buttonOpen)
            self.tableWidget.setCellWidget(i, 1, buttonDel)
            i += 1

    def buttonOpen_clicked(self):

        button = self.sender()

        if button:
            row = self.tableWidget.indexAt(button.pos()).row()

        # 此处启动有问题，详情见readme-问题01
        self.MainUi = MainUI(self.projectList[row])
        self.MainUi.show()
        self.close()

    def buttonDel_clicked(self):

        global row
        button = self.sender()
        if button:
            row = self.tableWidget.indexAt(button.pos()).row()

        self.__delRow = row

        # 删除弹框--------------------------------------
        tag = "确认删除" + self.projectList[row] + "项目？"
        self.confirmAlert = ConfirmAlert(tag)  # 此处传入的参数1，用于接收返回值
        self.confirmAlert.ConfirmAlertSignal.connect(self.getConfirmAlertSignal)
        self.confirmAlert.show()

    def getNewProjectSignal(self, tag, name):

        if tag == 1:
            print(name)

            # print(self.newProject.NewProjectSignal.__repr__())
            print("子界面被关闭")

    def getConfirmAlertSignal(self, tag):  # 返回0，表示取消

        if tag == 1:
            self.tableWidget.removeRow(self.__delRow)
            self.projectsManage.delProject(self.projectList[self.__delRow])

            # 删除项目文件后，需要修改项目列表
            del self.projectList[self.__delRow]
        pass

    # 本页面的UI设置
    def __setUIStyle(self):

        self.setWindowIcon(QIcon('ArtRes/start.png'))
        self.setFixedSize(self.width(), self.height())  # 固定界面尺寸
        self.setStyleSheet(

            "QLabel{background-color:rgb(255,255,255,0);border-radius: 9px;;font-size:24px}"
            "QLabel{color:#F5FFFA}"
            "QLabel{font-size:24px;font-family:'楷体'}"

            "QPushButton{font-size:35px;font-family:'楷体'}"
            "QDialog{background-image:url(ArtRes/backgroudBlack.png)}"

            "QPushButton{background:rgb(255,255,255,0);border-radius:5px;}"
            "QPushButton:hover{background:#afb4db;}"
            "QPushButton{color:#F5FFFA}"
            "QPushButton{text-align:left}"

        )

        self.tableWidget.setStyleSheet("QTableWidget{background:rgb(100,100,100,0)}"
                                       "QTableWidget{border-style:none}:"
                                       )
        self.pushButtonNew.setStyleSheet("QPushButton{background:rgb(255,255,255,17);border-radius:5px;}"
                                         "QPushButton:hover{background:#9AFF9A;color:black}"
                                         "QPushButton{font-size:35px;font-family:'楷体'}"
                                         "QPushButton{color:#F5FFFA}"
                                         )
        self.pushButtonSetting.setStyleSheet("QPushButton{background:rgb(255,255,255,17);border-radius:5px;}"
                                             "QPushButton:hover{background:#9AFF9A;color:black}"
                                             "QPushButton{font-size:15px;font-family:'楷体'}"
                                             "QPushButton{color:#F5FFFA}"
                                             )

        self.pushButtonNew.setIcon(QIcon('ArtRes/add.png'))
        self.pushButtonSetting.setIcon(QIcon('ArtRes/cfg.png'))
