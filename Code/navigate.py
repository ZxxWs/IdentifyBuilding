import sys

from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QDialog, QHeaderView, QPushButton, QApplication

from Code.File.projectsManage import ProjectsManage
# from Code.MainUI import MainUI
from Code.MainUI import MainUI
from Code.configurate import Configurate
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

        newProject = NewProject(self)
        newProject.show()

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

        button = self.sender()

        if button:
            row = self.tableWidget.indexAt(button.pos()).row()
        self.tableWidget.removeRow(row)
        self.projectsManage.delProject(self.projectList[row])

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
        self.pushButtonNew.setStyleSheet("QPushButton{background:rgb(255,255,255,0);border-radius:5px;}"
                                         "QPushButton:hover{background:#afb4db;}"
                                         "QPushButton{color:#F5FFFA}"
                                         )
        self.pushButtonSetting.setStyleSheet("QPushButton{background:rgb(255,255,255,0);border-radius:5px;}"
                                             "QPushButton:hover{background:#afb4db;}"
                                             "QPushButton{color:#F5FFFA}"
                                             "QPushButton{font-size:15px;font-family:'楷体'}"
                                             )

        self.pushButtonNew.setIcon(QIcon('ArtRes/add.png'))
        self.pushButtonSetting.setIcon(QIcon('ArtRes/cfg.png'))
        # self.pushButtonOpenImgDir.setIcon(QIcon("ArtRes/file.png"))

    def closeSelf(self):
        self.close()


