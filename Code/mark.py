import os

from PyQt5 import QtGui
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QDialog, QHeaderView, QTableWidgetItem, QPushButton, QTableWidget

from Code.File.cfgFile import CfgFile
from Code.File.inforFile import InforFile
from GUI.Ui_mark import Ui_Mark


class Mark(QDialog, Ui_Mark):

    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.setupUi(self)

        # 获取项目配置信息
        self.__cfgFile = CfgFile()
        self.__cfgDic = self.__cfgFile.cfgRead()
        self.nameSet = self.__cfgFile.getMarkNames()

        self.tableTag = len(self.nameSet)#用于表格初始化的tag，防止初始化时表格变动导致的触发表格变动函数
        self.buttonTag = 0  # tag=0时，表示未运行标注程序

        self.__setUIStyle()
        self.__initTable()
        self.__initLabel()


    #点击“开始标注按钮
    @pyqtSlot()
    def on_pushButton_clicked(self):

        if self.buttonTag == 0:

            # 装载文件

            self.tableWidget.setEditTriggers(QTableWidget.NoEditTriggers)#设置表格禁止编辑，参考见readme

            self.loadingJPG()

            self.buttonTag = 1
            self.pushButton.setText("停止标注")
            self.__runMark()
        elif self.buttonTag == 1:

            self.tableWidget.setEditTriggers(QTableWidget.DoubleClicked)#设置表格编辑状态-双击可编辑
            os.system("taskkill /f /im yolo_mark.exe")
            self.buttonTag = 0
            self.pushButton.setText("开始标注")
            pass

    @pyqtSlot()
    def on_pushButtonBack_clicked(self):
        os.system("taskkill /f /im yolo_mark.exe")
        self.close()

    @pyqtSlot()
    def on_pushButtonOpenImgDir_clicked(self):

        #如果处于标注状态、则不允许按钮点击
        if self.buttonTag==1:
            return

        #打开放置图片的文件夹
        FileDir = self.__cfgDic['Yolo_mark'] + '/data/img/'
        f = str(FileDir).replace("/", '\\')
        if not os.path.exists(f):
            os.makedirs(f)
        os.system("start explorer " + f)

    def __runMark(self):
        # 传过来的参数是mark_cmd
        path = self.__cfgDic['Yolo_mark']
        CMD = ""
        # 如果目录不是C盘，则需要更换盘符
        if path[0] != 'c' or path[0] != 'C':
            CMD = path[0] + ": &"

        CMD += "CD " + path + "&" + " yolo_mark.exe data/img data/train.txt data/obj.names"
        print(CMD)
        os.popen(CMD)

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        self.parent().show()


    #本页面的UI设置
    def __setUIStyle(self):

        self.setWindowIcon(QIcon('ArtRes/mark.png'))

        self.setWindowState(Qt.WindowMaximized)
        self.setStyleSheet("QLabel{background-color:rgb(199,199,199,255);border-radius: 17px;font-size:24px}"
                           "QTableWidget{font-size:19px}"
                           )
        self.pushButtonOpenImgDir.setIcon(QIcon("ArtRes/file.png"))

    # ---------------------------------------------Label--------------------------------------------------

    def __initLabel(self):
        link=  self.__cfgDic['Yolo_mark'] + '/data/img/'#需要在文字中填充的链接
        inforFile=InforFile()

        infor=inforFile.getInfor("mark")
        self.labelOpen.setText(infor[0].replace("%s",link))
        self.labelTable.setText(infor[1].replace("\n",""))
        self.labelOK.setText(infor[2].replace("\n",""))
        pass

    # ---------------------------------------------下面是表格----------------------------------------------------

    def __initTable(self):

        # 初始化表格头格式
        self.tableWidget.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeToContents)

        self.tableWidget.setRowCount(len(self.nameSet) + 1)
        i = 0
        for name in self.nameSet:

            item = QTableWidgetItem(name)
            self.tableWidget.setItem(i, 0, item)

            # 添加按钮
            button = QPushButton('删除')
            button.setIcon(QIcon("ArtRes/del.png"))
            button.clicked.connect(self.button_clicked)
            self.tableWidget.setCellWidget(i, 1, button)
            i += 1

        # 填加最后一行的“添加”按钮
        button = QPushButton("添加标注类型")
        button.setIcon(QIcon("ArtRes/addName.png"))
        button.clicked.connect(self.button_clicked)
        self.tableWidget.setCellWidget(i, 0, button)

    def button_clicked(self):

        #如果处于标注状态、则不允许按钮点击
        if self.buttonTag==1:
            return

        button = self.sender()
        row = -1  # 初始化行数
        if button:
            row = self.tableWidget.indexAt(button.pos()).row()

        # 添加功能
        if row == self.tableWidget.rowCount() - 1:

            print("添加按钮")
            if row > len(self.nameSet):
                print("添加按钮return")
                return
            self.tableWidget.insertRow(row)
            button = QPushButton('删除')
            button.clicked.connect(self.button_clicked)
            self.tableWidget.setCellWidget(row, 1, button)

        # 删除按钮
        else:
            self.tableWidget.removeRow(row)
            self.on_tableWidget_cellChanged()

    @pyqtSlot(int, int)
    def on_tableWidget_cellChanged(self):

        # 此tag用于记录初次表格的初始化，防止初始化时候的改动导致调用此函数
        if self.tableTag > 0:
            self.tableTag -= 1
            return

        # 用于统计当前表格中的元素
        self.nameSet.clear()
        row = self.tableWidget.rowCount()
        for i in range(row - 1):  # 最后一行不参与统计（最后一行为按钮）
            if self.tableWidget.item(i, 0) is not None:
                if self.tableWidget.item(i, 0).text() != "":
                    self.nameSet.add(self.tableWidget.item(i, 0).text())

        # 用于删除多的框
        tag = 0  # tag用于记录空白格子的个数
        cacheSet = set()
        for i in range(row - 1, 0, -1):  # 最后一行不参与统计（最后一行为按钮）
            if self.tableWidget.item(i, 0) is None:
                tag += 1
            elif self.tableWidget.item(i, 0).text() == "":
                tag += 1
            elif self.tableWidget.item(i, 0).text() in cacheSet:
                tag += 1
            else:
                cacheSet.add(self.tableWidget.item(i, 0).text())
            if tag > 1:
                self.tableWidget.removeRow(i)
                tag -= 1
                i -= 1

        self.__cfgFile.setMarkNames(self.nameSet)

    # ---------------------------------------------上面是表格----------------------------------------------------

    # 点击“标注”按钮后触发的，创建并写入train.txt文件
    def loadingJPG(self):

        # 一些冗余代码，防止文件不存在
        Dir = self.__cfgDic['Yolo_mark'] + '/data/img/'
        FileDir = str(Dir).replace("/", '\\')
        if not os.path.exists(FileDir):
            os.makedirs(FileDir)

        prefix = "data/img/"
        with open(self.__cfgDic['Yolo_mark'] + '/data/train.txt', 'w') as trainTXT:
            fileNames = os.listdir(FileDir)
            for fileName in fileNames:
                if fileName[-4:] == ".jpg":
                    trainTXT.write(prefix + fileName + "\n")



