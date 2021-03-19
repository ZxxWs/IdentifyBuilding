import os

from PyQt5 import QtGui
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QDialog, QHeaderView, QTableWidgetItem, QPushButton

from Code.File import File
from GUI.Ui_mark import Ui_Mark


class Mark(QDialog, Ui_Mark):

    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.setupUi(self)

        # 获取项目配置信息
        self.__cfgFile = File()
        self.__dic = self.__cfgFile.cfgRead()

        self.buttonTag = 0  # tag=0时，表示未运行标注程序
        self.__initTable()
        self.__setUIStyle()

    @pyqtSlot()
    def on_pushButton_clicked(self):

        if self.buttonTag == 0:
            self.__runMark()
            self.buttonTag = 1
            self.pushButton.setText("停止标注")
        elif self.buttonTag == 1:
            os.system("taskkill /f /im yolo_mark.exe")
            self.buttonTag = 0
            self.pushButton.setText("开始标注")
            pass

    @pyqtSlot()
    def on_pushButtonBack_clicked(self):

        os.system("taskkill /f /im yolo_mark.exe")
        self.close()

    def __runMark(self):
        # 传过来的参数是mark_cmd
        path = self.__dic['Yolo_mark']
        CMD = ""
        # 如果目录不是C盘，则需要更换盘符
        if path[0] != 'c' or path[0] != 'C':
            CMD = path[0] + ": &"

        CMD += "CD " + path + "&" + " yolo_mark.exe data/img data/train.txt data/obj.names"
        print(CMD)
        os.popen(CMD)

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        self.parent().show()

    def __initTable(self):

        # 初始化表格头格式
        self.tableWidget.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeToContents)

        self.nameList = self.__cfgFile.getMarkNames()

        self.tableWidget.setRowCount(len(self.nameList) + 1)

        i = 0
        for name in self.nameList:
            item = QTableWidgetItem(name)
            self.tableWidget.setItem(i, 0, item)

            # 添加按钮
            button = QPushButton('删除')

            # button.setIcon(QIcon("ArtRes/file.png"))
            button.clicked.connect(self.button_clicked)
            self.tableWidget.setCellWidget(i, 1, button)
            i += 1

        # 填加最后一行的“添加”按钮
        button = QPushButton("添加标注类型")
        button.setIcon(QIcon("ArtRes/addName.png"))
        button.clicked.connect(self.button_clicked)
        self.tableWidget.setCellWidget(i, 0, button)

    def __setUIStyle(self):

        self.setWindowIcon(QIcon('ArtRes/mark.png'))

        self.setWindowState(Qt.WindowMaximized)
        self.setStyleSheet("QLabel{background-color:rgb(199,199,199,255);border-radius: 17px}"
                           "QTableWidget{font-size:19px}"
                           )

    def button_clicked(self):

        button = self.sender()
        row = -1  # 初始化行数
        if button:
            row = self.tableWidget.indexAt(button.pos()).row()

        # 添加功能
        if row == self.tableWidget.rowCount() - 1:


            if row > len(self.nameList):
                return
            self.tableWidget.insertRow(row)
            button = QPushButton('删除')
            button.clicked.connect(self.button_clicked)
            self.tableWidget.setCellWidget(row, 1, button)

        # 删除按钮
        else:
            self.tableWidget.removeRow(row)


    @pyqtSlot(int, int)
    def on_tableWidget_cellChanged(self):

        #用于统计当前表格中的元素
        self.nameList.clear()
        row = self.tableWidget.rowCount()

        for i in range(row - 1):  # 最后一行不参与统计（最后一行为按钮）
            if self.tableWidget.item(i, 0) is not None:
                if self.tableWidget.item(i, 0).text() != "":
                    self.nameList.append(self.tableWidget.item(i, 0).text())

        # 用于删除多的框
        tag = 0  # tag用于记录空白格子的个数
        for i in range(row - 1, 0, -1):  # 最后一行不参与统计（最后一行为按钮）
            if self.tableWidget.item(i, 0) is None:
                tag += 1
            elif self.tableWidget.item(i, 0).text() == "":
                tag += 1
            else:
                continue
            if tag > 1:
                self.tableWidget.removeRow(i)
                tag -= 1
                i -= 1

        # self.__getTableItems()

        # self.__cfgFile.setMarkNames(self.nameList)
        # print("内容改变")
