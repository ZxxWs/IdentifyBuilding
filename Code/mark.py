import os

from PyQt5 import QtGui
from PyQt5.QtCore import pyqtSlot, Qt, QStringListModel
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QDialog, QAbstractItemView

from Code.File.cfgFile import CfgFile
from Code.File.projectSetting import ProjectSetting
from GUI.Ui_mark import Ui_Mark


class Mark(QDialog, Ui_Mark):

    def __init__(self, projectName, parent=None):
        QDialog.__init__(self, parent)
        self.setupUi(self)

        # 获取项目配置信息
        cfgFile = CfgFile()
        self.__cfgDic =  cfgFile.cfgRead()
        self.projectPath = self.__cfgDic['Yolo_mark'] + '/projects/' + projectName + '/'  # 项目路径链接
        self.projectName = projectName

        self.runTag = 0  # tag=0时，表示未运行标注程序

        self.__setUIStyle()
        self.__initListView()
        self.__initLabel()

    # 点击“开始标注按钮
    @pyqtSlot()
    def on_pushButton_clicked(self):

        if self.runTag == 0:

            self.loadingJPG()
            self.runTag = 1
            self.pushButton.setText("停止标注")
            self.__runMark()
        elif self.runTag == 1:

            os.system("taskkill /f /im yolo_mark.exe")
            self.runTag = 0
            self.pushButton.setText("开始标注")

    @pyqtSlot()
    def on_pushButtonBack_clicked(self):
        os.system("taskkill /f /im yolo_mark.exe")
        self.close()

    @pyqtSlot()
    def on_pushButtonOpenImgDirs_clicked(self):

        # 如果处于标注状态、则不允许按钮点击
        if self.runTag == 1:
            return

        # 打开放置图片的文件夹
        FileDir = self.projectPath + 'img/'
        f = str(FileDir).replace("/", '\\')
        if not os.path.exists(f):
            os.makedirs(f)
        os.system("start explorer " + f)

    def __runMark(self):

        path = self.__cfgDic['Yolo_mark']  # mark文件路径
        CMD = path + "/yolo_mark.exe " + self.projectPath + "img " + self.projectPath + "train.txt " + self.projectPath + "obj.names"

        print(CMD)
        os.popen(CMD)

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        self.parent().show()

    def __initLabel(self):
        txt = "请在" + self.projectPath + "img/文件夹下放置需要标记的图片"
        self.labelOpen.setText(txt)
        self.labelOpen.setWordWrap(True)

    def __initListView(self):

        self.listView.setEditTriggers(QAbstractItemView.NoEditTriggers)  # 列表不可点击

        projectSetting = ProjectSetting(self.projectName)
        objNames = projectSetting.getObjNames()
        slm = QStringListModel()  # 创建mode
        slm.setStringList(objNames)  # 将数据设置到model
        self.listView.setModel(slm)  ##绑定 listView 和 model


        # self.listView.setItemAlignment(Qt.AlignRight)
        self.listView.setItemAlignment(Qt.AlignCenter)  # 此行需要在PyQt5.12上运行
        print(objNames)

    # 点击“标注”按钮后触发的，创建并写入train.txt文件

    def loadingJPG(self):

        prefix = "projects/" + self.projectName + "/img/"
        with open(self.projectPath + 'train.txt', 'w') as trainTXT:
            fileNames = os.listdir(self.projectPath + "img/")
            # print(fileNames)
            for fileName in fileNames:
                if fileName[-4:] == ".jpg":
                    # print(fileName)
                    trainTXT.write(prefix + fileName + "\n")
            trainTXT.close()

    # 本页面的UI设置
    def __setUIStyle(self):

        self.setWindowIcon(QIcon('ArtRes/mark.png'))

        self.setWindowState(Qt.WindowMaximized)
        self.labelOpen.setStyleSheet("QLabel{background-color:rgb(0,0,0,155)}"
                                     "QLabel{color:#F5FFFA}"
                                     "QLabel{border-radius: 17px}"
                                     "QLabel{font-size:35px;font-family:'楷体'}"
                                     )
        self.labelList.setStyleSheet("QLabel{background-color:rgb(0,0,0,26)}"
                                     "QLabel{color:#F5FFFA}")
        self.listView.setStyleSheet("QListView{background-color:rgb(200,200,200,155)}"
                                    "QListView{border-radius: 17px}"
                                    "QListView{font-size:35px}"
                                    "QListView{text-align:right}" 
                                    "QListView{border-style:none}:"
                                    )
        self.pushButtonOpenImgDirs.setIcon(QIcon("ArtRes/file.png"))
        self.pushButton.setIcon(QIcon("ArtRes/start.png"))
        self.pushButtonBack.setIcon(QIcon("ArtRes/Cancel.png"))
