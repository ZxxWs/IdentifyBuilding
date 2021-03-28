from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QDialog, QHeaderView, QTableWidgetItem, QPushButton, QFileDialog
from Code.File.cfgFile import CfgFile
from GUI.Ui_configurate import Ui_Configurate

'''
在本页代码中，table的初始化很多都写在代码中，因为如果有变动需求只需要单独修改代码，不需用改写UI，
'''


class Configurate(QDialog, Ui_Configurate):

    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.__setUIStyle()

        # 读取文件配置信息
        self.__cfgfile = CfgFile()
        self.__dic = self.__cfgfile.cfgRead()
        # self.__RowList = ['Yolo_mark', 'conv','darknet', 'data', 'cfg', 'weights']  # 此行代码异常重要,保存的是data\cfg.xml中的键
        self.__RowList = ['Yolo_mark', 'darknet', 'conv']  # 此行代码异常重要,保存的是data\cfg.xml中的键

        self.__fillTable()  # 填充表格内容

    # 点击确认按钮后的触发事件
    @pyqtSlot()
    def on_pushButtonVerify_clicked(self):

        for i in range(len(self.__RowList)):
            item = self.tableWidget.item(i, 0).text()
            self.__dic[self.__RowList[i]] = item

        self.__cfgfile.cfgWrite(self.__dic)
        self.close()

    @pyqtSlot()
    def on_pushButtonCancel_clicked(self):
        self.close()

    # 填充表格内容
    def __fillTable(self):

        self.tableWidget.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
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
            button = QPushButton()
            # 按钮逻辑绑定、图标设置
            button.setIcon(QIcon("ArtRes/file.png"))
            button.clicked.connect(self.button_clicked)
            self.tableWidget.setCellWidget(i, 1, button)
            i += 1

    def button_clicked(self):

        fileDir = {0, 1}  # 有的路径是文件、有的路径是文件夹，其中这个集合中的是文件夹
        button = self.sender()
        row = -1  # 初始化行数
        if button:
            row = self.tableWidget.indexAt(button.pos()).row()

            filePath = None
            if row in fileDir:
                filePath = QFileDialog.getExistingDirectory(self)
                print(filePath)
            else:
                filePath, i = QFileDialog.getOpenFileName(self, "选择文件", "")

            # 防止点击按钮后取消导致配置为空（？？？？几天后没看懂
            if filePath == "":
                return

            item = QTableWidgetItem(str(filePath))
            self.tableWidget.setItem(row, 0, item)

    def __setUIStyle(self):

        self.setWindowModality(Qt.ApplicationModal)  # 设置其他界面不可点击

        self.setWindowIcon(QIcon('ArtRes/setting.png'))
        self.setStyleSheet("QDialog{background-image:url(ArtRes/backgroudBlack.png)}"
                           "QPushButton{background:rgb(255,255,255,26);border-radius:5px;}"
                           "QPushButton:hover{background:green;}"
                           "QPushButton{color:#F5FFFA}"
                           )
