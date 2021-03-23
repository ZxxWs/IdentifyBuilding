# from PyQt5.QtCore import pyqtSlot
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

        # --------------------------------------------此处未做输入验证——————————————————————————
        # 获取用户输入的新建信息
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
        elif name == "":
            self.labelAlert.setText("项目名不能为空")
            self.lineEdit.clear()
            return
        elif len(self.__NameList) == 0:
            self.labelAlert.setText("识别及标记种类至少为一个")
            # self.lineEdit.clear()
            return
        else:
            projectsManage.newProject(name, self.__NameList)
            # 向父界面传递信号
            self.NewProjectSignal.emit(self.father, name)
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

    def __initTable(self):

        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeToContents)
        self.tableWidget.verticalHeader().setVisible(False)  # 隐藏垂直表头

        self.tableWidget.setRowCount(1)
        # 填加最后一行的“添加”按钮
        button = QPushButton("添加标注类型")
        button.setIcon(QIcon("ArtRes/addName.png"))
        button.clicked.connect(self.Addbutton_clicked)
        self.tableWidget.setCellWidget(0, 0, button)

        self.__flashTableTag = False  # 这个tag是用于刷新表格的死锁tag

    def Addbutton_clicked(self):

        self.__addItemTag = True
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

        self.on_tableWidget_cellChanged()

    def Delbutton_clicked(self):

        button = self.sender()
        if button:
            row = self.tableWidget.indexAt(button.pos()).row()
        # 删除按钮

        self.tableWidget.removeRow(row)
        self.on_tableWidget_cellChanged()

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
            if self.tableWidget.item(i, 0) is not None:
                if self.tableWidget.item(i, 0).text() != "":
                    if self.tableWidget.item(i, 0).text() not in self.__NameList:
                        self.__NameList.append(self.tableWidget.item(i, 0).text())

        self.flashTable()

    def flashTable(self):
        self.__flashTableTag = True
        self.tableWidget.clearContents()

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
