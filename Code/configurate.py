from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog, QHeaderView, QTableWidgetItem, QPushButton, QFileDialog
from PyQt5.uic.properties import QtWidgets, QtCore

from Code.File import File
from GUI.Ui_configurate import Ui_Configurate

'''
在本页代码中，table的初始化很多都写在代码中，因为如果有变动需求只需要单独修改代码，不需用改写UI，
'''


class Configurate(QDialog, Ui_Configurate):

    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.setupUi(self)

        # 读取文件配置信息
        self.__cfgfile = File()
        self.__dic = self.__cfgfile.cfgRead()
        self.__RowList = ['Yolo_mark', 'conv','darknet', 'data', 'cfg', 'weights']  # 此行代码异常重要,保存的是data\cfg.xml中的键

        self.__fillTable()  # 填充表格内容

    @pyqtSlot()
    def on_pushButtonVerify_clicked(self):

        for i in range(len(self.__RowList)):
            item = self.tableWidget.item(i, 0).text()
            self.__dic[self.__RowList[i]] = item

        self.__cfgfile.cfgWrite(self.__dic)

    @pyqtSlot()
    def on_pushButtonCancel_clicked(self):
        self.close()

    # 填充表格内容
    def __fillTable(self):

        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeToContents)

        self.tableWidget.setRowCount(len(self.__RowList))

        i = 0
        for listItem in self.__RowList:
            # 设置每行的内容
            itemPath = QTableWidgetItem(self.__dic[listItem])
            itemLable = QTableWidgetItem(listItem)
            self.tableWidget.setItem(i, 0, itemPath)
            self.tableWidget.setVerticalHeaderItem(i, itemLable)

            # 添加按钮
            button = QPushButton("-")
            button.clicked.connect(self.button_clicked)
            self.tableWidget.setCellWidget(i, 1, button)
            i += 1

    def button_clicked(self):


        fileDir={0}#有的路径是文件、有的路径是文件夹，其中这个集合中的是文件夹
        button = self.sender()
        row = -1  # 初始化行数
        if button:
            row = self.tableWidget.indexAt(button.pos()).row()

        filePath=None
        if row in fileDir:
            filePath=QFileDialog.getExistingDirectory(self)
            print(filePath)
        else:
            filePath, i = QFileDialog.getOpenFileName(self, "选择文件", "")

        # 防止点击按钮后取消导致配置为空
        if filePath == "":
            return


        item = QTableWidgetItem(str(filePath))
        self.tableWidget.setItem(row, 0, item)
