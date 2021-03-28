# from PyQt5.QtCore import pyqtSlot
import re

from PyQt5 import QtCore
from PyQt5.QtGui import QIcon, QColor, QBrush
from PyQt5.QtWidgets import QDialog, QHeaderView, QPushButton, QTableWidgetItem

from PyQt5.QtCore import pyqtSlot, Qt

from Code.File.projectsManage import ProjectsManage
from GUI.Ui_newProject import Ui_NewProject


class NewProject(QDialog, Ui_NewProject):
    # 让多窗口之间传递信号 刷新主窗口信息，int是指哪个界面是父界面，str是新建的项目名
    NewProjectSignal = QtCore.pyqtSignal(int, str)

    def __init__(self, father, parent=None):
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.father = father
        self.__NameList = []  # 标记及识别种类名称
        self.__initTable()
        self.__setUIStyle()

    @pyqtSlot()
    def on_pushButtonOK_clicked(self):

        # 获取用户输入的新建信息
        name = self.lineEdit.text()

        #对输入的项目名正则检测处理
        pattern = re.compile('^[A-Za-z][A-Za-z0-9_]{1,10}$')
        reName=pattern.findall(name)
        if len(reName)==0:
            self.labelAlert.setText("项目命名不规范,以字母命名，后可接字母、数字及下划线,长度最多为10位")
            self.lineEdit.clear()
            return
        projectsManage = ProjectsManage()
        nameSet = projectsManage.getProjectsList()#获取已近存在的项目名
        if name in nameSet:
            self.labelAlert.setText("该项目已存在，请更改项目名称")
            self.lineEdit.clear()
            return
        elif name is None:
            self.labelAlert.setText("请输入项目名")
            self.lineEdit.clear()
            return
        elif name == "":
            self.labelAlert.setText("项目名不能为空")#此行代码有点多余，因为已近有了上面的正则处理
            self.lineEdit.clear()
            return
        elif len(self.__NameList) == 0:
            self.labelAlert.setText("识别及标记种类至少为一个")
            return
        else:
            projectsManage.newProject(name, self.__NameList)
            # 向父界面传递信号，信号值为新建项目名
            self.NewProjectSignal.emit(self.father, name)

        self.close()



    def closeEvent(self, event):
        # self.NewProjectSignal.emit("close")
        pass

    @pyqtSlot()
    def on_pushButtonCancel_clicked(self):

        self.close()


    #初始化UI时初始化表格函数
    def __initTable(self):

        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeToContents)
        self.tableWidget.verticalHeader().setVisible(False)  # 隐藏垂直表头

        self.tableWidget.setRowCount(1)#设置表格行数为1
        # 填加最后一行的“添加”按钮
        button = QPushButton("添加标注类型")
        button.setIcon(QIcon("ArtRes/addName.png"))
        button.clicked.connect(self.Addbutton_clicked)
        self.tableWidget.setCellWidget(0, 0, button)

        self.__flashTableTag = False  # 这个tag是用于刷新表格的死锁tag


    #点击“添加标注种类按钮”
    def Addbutton_clicked(self):

        self.__addItemTag = True#tag用于死锁一些东西（忘了锁的啥

        listLen = len(self.__NameList)
        if listLen + 1 < self.tableWidget.rowCount():
            return
        self.tableWidget.insertRow(listLen)

        # self.tableWidget.item(listLen, 0).setBackground(QBrush(QColor(255, 255, 255, 199)))#不能用
        button = QPushButton()
        button.clicked.connect(self.Delbutton_clicked)
        button.setIcon(QIcon("ArtRes/del.png"))
        button.setStyleSheet("QPushButton{background:rgb(255,255,255,17);border-radius:5px;}"
                             "QPushButton:hover{background:#9AFF9A;color:black}")
        self.tableWidget.setCellWidget(listLen, 1, button)

        self.on_tableWidget_cellChanged()#触发一下表格改变函数进行刷新表格

    def Delbutton_clicked(self):

        button = self.sender()
        if button:
            row = self.tableWidget.indexAt(button.pos()).row()
        # 删除按钮

        self.tableWidget.removeRow(row)#将表格的一行删除（点击的哪行删除哪行
        self.on_tableWidget_cellChanged()#刷新表格

    @pyqtSlot(int, int)
    def on_tableWidget_cellChanged(self):

        if self.__addItemTag:
            self.__addItemTag = False
            return

        if self.__flashTableTag:
            return

        # 用于统计当前表格中的元素
        self.__NameList.clear()
        row = self.tableWidget.rowCount()
        for i in range(row - 1):  # 最后一行不参与统计（最后一行为按钮）
            if self.tableWidget.item(i, 0) is not None:#空的不算
                if self.tableWidget.item(i, 0).text() != "":#空字符不算
                    if self.tableWidget.item(i, 0).text() not in self.__NameList:
                        self.__NameList.append(self.tableWidget.item(i, 0).text())

        self.flashTable()#执行刷新表格函数


    #在table发生改变后执行刷新表格函数（但需要看情况刷新
    def flashTable(self):
        self.__flashTableTag = True
        self.tableWidget.clearContents()#清除表格内容
        self.tableWidget.setRowCount(len(self.__NameList) + 1)

        for i in range(len(self.__NameList)):
            item = QTableWidgetItem(self.__NameList[i])
            self.tableWidget.setItem(i, 0, item)

            self.tableWidget.item(i, 0).setBackground(QBrush(QColor(255, 255, 255, 199)))
            button = QPushButton()
            button.clicked.connect(self.Delbutton_clicked)
            button.setIcon(QIcon("ArtRes/del.png"))
            button.setStyleSheet("QPushButton{background:rgb(255,255,255,17);border-radius:5px;}"
                                 "QPushButton:hover{background:#9AFF9A;color:black}")
            self.tableWidget.setCellWidget(i, 1, button)

        #在将表格填充好后，在最后一行加入添加按钮
        button = QPushButton("添加标注类型")
        button.setIcon(QIcon("ArtRes/addName.png"))
        button.clicked.connect(self.Addbutton_clicked)
        self.tableWidget.setCellWidget(len(self.__NameList), 0, button)

        self.__flashTableTag = False

    def __setUIStyle(self):

        self.setWindowModality(Qt.ApplicationModal)  # 设置其他界面不可点击
        self.setFixedSize(self.width(), self.height())  # 固定界面尺寸
        self.setStyleSheet("QLabel{background-color:rgb(255,255,255,0);border-radius: 9px;}"
                           "QLabel{color:#F5FFFA}"
                           "QLabel{font-size:24px;font-family:'楷体'}"
                           "QPushButton{background:rgb(255,255,255,100);border-radius:5px;}"
                           "QPushButton:hover{background:#9AFF9A;color:black}"
                           "QPushButton{font-size:30px;font-family:'楷体'}"
                           "QPushButton{color:#F5FFFA}"
                           "QPushButton{text-align:center}"
                           "QDialog{background-image:url(ArtRes/backgroudBlack.png)}"
                           "QLineEdit{border-radius:3px;background-color:rgb(255,255,255,199)}"
                           )

        self.tableWidget.setStyleSheet("QTableWidget{background:rgb(100,100,100,0)}"
                                       "QTableWidget{border-style:none}:"
                                       )
        self.pushButtonOK.setStyleSheet("QPushButton{background:rgb(255,255,255,17);border-radius:5px;}"
                                        "QPushButton:hover{background:#9AFF9A;color:black}"
                                        "QPushButton{font-size:35px;font-family:'楷体'}"
                                        "QPushButton{color:#F5FFFA}")
        self.pushButtonCancel.setStyleSheet("QPushButton{background:rgb(255,255,255,17);border-radius:5px;}"
                                            "QPushButton:hover{background:#9AFF9A;color:black}"
                                            "QPushButton{font-size:35px;font-family:'楷体'}"
                                            "QPushButton{color:#F5FFFA}")
        self.setWindowIcon(QIcon('ArtRes/addName.png'))
        self.pushButtonCancel.setIcon(QIcon("ArtRes/Cancel.png"))
        self.pushButtonOK.setIcon(QIcon("ArtRes/OK.png"))
        self.labelAlert.setWordWrap(True)#label根据内容可以换行
        self.pushButtonOK.setFocus()#将初始化后的焦点设置到确认按钮上，如果不设置会导致初始化后输入回车键使得界面关闭（焦点在取消上
