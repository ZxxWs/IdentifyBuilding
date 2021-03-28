from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QDialog, QHeaderView, QPushButton

from Code.File.cfgFile import CfgFile
from Code.File.projectsManage import ProjectsManage
from Code.MainUI import MainUI
from Code.configurate import Configurate
from Code.confirmAlert import ConfirmAlert
from Code.newProject import NewProject
from GUI.Ui_navigate import Ui_Navigate


class Navigate(QDialog, Ui_Navigate):

    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.setupUi(self)


        self.__cfgIsNoneTag=True
        self.__checkCfg()
        self.initTable(self.__cfgIsNoneTag)
        self.__setUIStyle()

        if not self.__cfgIsNoneTag:
            self.on_pushButtonSetting_clicked()

    #点击新建项目的触发事件
    @pyqtSlot()
    def on_pushButtonNew_clicked(self):
        #先进行配置判断，如果配置有空则打开配置界面
        if not self.__cfgIsNoneTag:
            self.on_pushButtonSetting_clicked()
            return
        self.newProject = NewProject(1)  # 此处传入的参数1，用于接收返回值
        self.newProject.NewProjectSignal.connect(self.getNewProjectSignal)  # 将子界面的信号量和本类中的方法绑定
        self.newProject.show()

    @pyqtSlot()
    def on_pushButtonSetting_clicked(self):
        self.cfg = Configurate(self)
        self.cfg.show()


    #如果整个软件没有配置，则只初始化格式（用tag标记
    def initTable(self,tag):

        #设置表头格式
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeToContents)
        self.tableWidget.verticalHeader().setVisible(False)  # 隐藏垂直表头
        self.tableWidget.horizontalHeader().setVisible(False)  # 隐藏水平表头

        if not tag:
            return

        self.projectsManage = ProjectsManage()
        self.projectList = self.projectsManage.getProjectsList()


        rowCount = len(self.projectList)
        self.tableWidget.setRowCount(rowCount)

        i = 0
        for projectName in self.projectList:
            # 向表格中填充按钮

            buttonOpen = QPushButton(projectName)
            buttonDel = QPushButton()

            buttonDel.setIcon(QIcon("ArtRes/del.png"))
            #按钮逻辑绑定
            buttonOpen.clicked.connect(self.buttonOpen_clicked)
            buttonDel.clicked.connect(self.buttonDel_clicked)
            self.tableWidget.setCellWidget(i, 0, buttonOpen)
            self.tableWidget.setCellWidget(i, 1, buttonDel)
            i += 1

        self.tableWidget.setCurrentCell(-1,0)#不加此行时，表格在初始化的时候第一行会被选中（显示高亮

    # 检测软件是否被配置
    def __checkCfg(self):
        cfgFile = CfgFile()
        dic = cfgFile.cfgRead()
        for key in dic:
            if dic[key] is None:
                self.__cfgIsNoneTag =  False
                return

    def buttonOpen_clicked(self):

        button = self.sender()

        if button:
            #获取被点击的按钮的行数
            row = self.tableWidget.indexAt(button.pos()).row()

        # 此处启动有问题，详情见readme-问题01
        self.MainUi = MainUI(self.projectList[row])
        self.MainUi.show()
        self.close()

    def buttonDel_clicked(self):

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
            self.MainUi = MainUI(name)
            self.MainUi.show()
            self.close()

    def getConfirmAlertSignal(self, tag):  # 返回0，表示取消

        if tag == 1:
            self.tableWidget.removeRow(self.__delRow)
            self.projectsManage.delProject(self.projectList[self.__delRow])
            # 删除项目文件后，需要修改项目列表
            del self.projectList[self.__delRow]

    # 本页面的UI设置
    def __setUIStyle(self):

        self.setWindowIcon(QIcon('ArtRes/start.png'))
        self.setFixedSize(self.width(), self.height())  # 固定界面尺寸
        self.setStyleSheet("QDialog{background-image:url(ArtRes/backgroudBlack.png)}"
                           "QLabel{background-color:rgb(255,255,255,0);border-radius: 9px;font-size:24px}"
                           "QLabel{color:#F5FFFA}"
                           "QLabel{font-size:24px;font-family:'楷体'}"
                           "QPushButton{background:rgb(255,255,255,0);border-radius:5px;}"
                           "QPushButton{font-size:35px;font-family:'楷体'}"
                           "QPushButton:hover{background:#afb4db;}"
                           "QPushButton{text-align:left}"
                           "QPushButton{color:#F5FFFA}"
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
