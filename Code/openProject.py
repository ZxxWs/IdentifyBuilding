from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QDialog, QHeaderView, QPushButton

from Code.File.projectsManage import ProjectsManage
from Code.confirmAlert import ConfirmAlert
from GUI.Ui_openProject import Ui_OpenProject



'''
本类中几乎完全重复写了Navigate类中的代码
原因：原本想：通过主界面使用“打开项目”功能打开Navigate界面，但Navigate界面引入了MainUI类，导致了无法通过主界面调用Navigate类，从而不得不重新写一个界面
'''
class OpenProject(QDialog, Ui_OpenProject):

    OpenProjectSignal = QtCore.pyqtSignal(str)#返回的是打开的项目名

    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.setupUi(self)

        self.initTable()
        self.__setUIStyle()

    def initTable(self):
        # pass
        self.projectsManage = ProjectsManage()
        self.projectList = self.projectsManage.getProjectsList()
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeToContents)
        self.tableWidget.verticalHeader().setVisible(False)  # 隐藏垂直表头
        self.tableWidget.horizontalHeader().setVisible(False)  # 隐藏水平表头
        #
        rowCount = len(self.projectList)
        print(self.projectList)
        self.tableWidget.setRowCount(rowCount)
        #
        i = 0
        for pro in self.projectList:
            # 向表格中填充按钮
            buttonOpen = QPushButton(pro)
            buttonDel = QPushButton()
        #
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
        self.OpenProjectSignal.emit(self.projectList[row])
        self.close()
        # 此处启动有问题，详情见readme-问题01
        # self.MainUi = MainUI(self.projectList[row])
        # self.MainUi.show()
        # self.close()

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


    def getConfirmAlertSignal(self, tag):  # 返回0，表示取消

        if tag == 1:
            self.tableWidget.removeRow(self.__delRow)
            self.projectsManage.delProject(self.projectList[self.__delRow])
            # 删除项目文件后，需要修改项目列表
            del self.projectList[self.__delRow]

    # 本页面的UI设置
    def __setUIStyle(self):
        self.setWindowModality(Qt.ApplicationModal)  # 设置其他界面不可点击
        self.setWindowIcon(QIcon('ArtRes/openProject.png'))
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
        # self.pushButtonNew.setStyleSheet("QPushButton{background:rgb(255,255,255,17);border-radius:5px;}"
        #                                  "QPushButton:hover{background:#9AFF9A;color:black}"
        #                                  "QPushButton{font-size:35px;font-family:'楷体'}"
        #                                  "QPushButton{color:#F5FFFA}"
        #                                  )
        # self.pushButtonSetting.setStyleSheet("QPushButton{background:rgb(255,255,255,17);border-radius:5px;}"
        #                                      "QPushButton:hover{background:#9AFF9A;color:black}"
        #                                      "QPushButton{font-size:15px;font-family:'楷体'}"
        #                                      "QPushButton{color:#F5FFFA}"
        #                                      )

        # self.pushButtonNew.setIcon(QIcon('ArtRes/add.png'))
        # self.pushButtonSetting.setIcon(QIcon('ArtRes/cfg.png'))
