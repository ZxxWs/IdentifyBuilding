import os
import sys

import PyQt5
import cv2
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import pyqtSlot, Qt, QEvent
from PyQt5.QtGui import QIcon, QImage, QPixmap
from PyQt5.QtWidgets import QDialog, QWidget

from Code.File.cfgFile import CfgFile
from Code.API import useAPI as UseAPI
from Code.Thread.detectImage import DetectImage
from Code.Thread.getWeightsFile import GetWeightsFile
from Code.Thread.runCMD import RunCMD
from Code.showImage import ShowImage

from GUI.Ui_test import Ui_Test


class Test(QDialog, Ui_Test):

    def __init__(self, projectName, parent=None):
        QDialog.__init__(self, parent)
        self.setupUi(self)

        # 获取项目配置信息
        cfgFile = CfgFile()
        self.cfgDic = cfgFile.cfgRead()

        #属性初始化
        self.projectPath = self.cfgDic['darknet'] + '/projects/' + projectName + '/'  # 项目路径链接
        self.darknetPath = self.cfgDic['darknet']
        self.projectName = projectName
        self.weightName = ""
        self.__pushButtonWeightTag = 0  # 按钮功能tag，0:可以执行检测权重、1：没有权重文件、2：需要刷新权重
        self.__childImage = None    #给子界面传递的图片

        # 初始化方法
        self.__initComboBox()
        self.__initUI()
        self.__setUIStyle()

        sys.path.append(self.darknetPath)
        import darknet

    @pyqtSlot()
    def on_pushButtonSelect_clicked(self):

        try:
            imageName, imgType = QtWidgets.QFileDialog.getOpenFileName(self, "选取文件", self.projectPath + 'test/',
                                                                       "*.jpg;;*.png;;All Files(*)")  # 这一行代码是网上找的，并未细看

            self.lineEdit.setText(imageName)
            jpg = QtGui.QPixmap(imageName)  # 通过文件路径获取图片文件，并设置图片长宽为label控件的长款
            self.labelImage.setPixmap(jpg)  # 在label控件上显示选择的图片
            self.labelImage.setScaledContents(True)


        except:
            self.labelImage.settetxt("文件选取有误")

    @pyqtSlot()
    def on_pushButtonOpenDir_clicked(self):
        fileDir = self.projectPath + 'test/'
        f = str(fileDir).replace("/", '\\')
        if not os.path.exists(f):
            os.makedirs(f)
        os.system("start explorer " + f)

    @pyqtSlot()
    def on_pushButtonWeight_clicked(self):

        if self.__pushButtonWeightTag == 0:
            self.__lockUI(True)  # 点击按钮后锁住UI
            self.__loadingJPG()
            CMD = self.darknetPath + "/darknet.exe detector map " + self.projectPath + "obj.data " + self.projectPath + "yolo-obj.cfg " + self.projectPath + "backup/" + self.weightName
            print(CMD)

            self.myThread = RunCMD(CMD, -12, -4)
            self.myThread.RunCMDSignal.connect(self.__getWeight)
            self.myThread.start()

        elif self.__pushButtonWeightTag == 1:
            fileDir = self.projectPath + 'backup/'
            f = str(fileDir).replace("/", '\\')
            if not os.path.exists(f):
                os.makedirs(f)
            os.system("start explorer " + f)

        elif self.__pushButtonWeightTag == 2:
            self.__pushButtonWeightTag = 0
            self.pushButtonWeight.setText("检测权重")
            self.__initComboBox()

    @pyqtSlot()
    def on_pushButtonTest_clicked(self):

        self.__lockUI(True)  # 点击按钮后锁住UI

        try:
            self.imageName = str(self.lineEdit.text())

            if self.imageName is None or self.imageName == "":
                self.labelImage.setText("请选择图片")
                self.__lockUI(False)
                return
            self.detectImage = DetectImage(self)
            self.detectImage.DetectImageSignal.connect(self.__getDetectImage)
            self.detectImage.start()
        except:
            self.labelImage.setText("检测错误")
            self.__lockUI(False)

    @pyqtSlot()
    def on_pushButtonBack_clicked(self):
        self.close()


    # 定义鼠标指向、离开控件的事件
    def eventFilter(self, object, event):

        if object == self.pushButtonShow:
            if event.type() == QEvent.Enter:
                self.labelShow.show()
            if event.type() == QEvent.Leave:
                self.labelShow.hide()

        if object == self.labelImage:
            if self.__childImage is None:
                # print("labelImage为空")
                pass
            else:
                if event.type() == QEvent.MouseButtonPress:

                    print("鼠标触发label")
                    #！！此处不能用self.showIamge，否则子界面关闭会导致父界面的关闭。（原因未知
                    showImage = ShowImage(self.__childImage,self)
                    showImage.show()

        return QWidget.eventFilter(self, object, event)

    @pyqtSlot(str)
    def on_comboBoxWeight_currentIndexChanged(self, weightName):
        self.weightName = weightName

    def closeEvent(self, a0: PyQt5.QtGui.QCloseEvent) -> None:

        os.system("taskkill /f /im darknet.exe")
        self.parent().show()

    # 初始化下拉列表（权重文件的下拉列表
    def __initComboBox(self):
        weightList = os.listdir(self.projectPath + "backup/")

        # 如果没有权重文件，则锁住UI
        if len(weightList) == 0:
            self.__lockUI(True)
            txt = "未检测到权重文件,请先训练权重或者将权重文件放于" + self.projectPath + "backup/文件夹下再刷新此界面"
            self.labelImage.setText(txt)
            self.pushButtonWeight.setDisabled(False)
            self.__pushButtonWeightTag = 1  # 表示没有权重文件
            self.pushButtonWeight.setText("打开权重文件夹")

            self.getWeightsFile = GetWeightsFile(self.projectPath + "backup/")

            self.getWeightsFile.GetWeightsFileSignal.connect(self.__getWeightFile)
            self.getWeightsFile.start()
            return

        self.__lockUI(False)
        self.comboBoxWeight.clear()
        self.comboBoxWeight.addItems(weightList)

    # 对于UI的初始化
    def __initUI(self):
        txt = "将测试集文件放置于" + self.projectPath + "test/文件夹下"
        self.labelOpenDir.setText(txt)
        self.pushButtonShow.hide()
        self.pushButtonShow.installEventFilter(self)  # 给按钮添加事件过滤器
        self.labelImage.installEventFilter(self)
        # self.labelImage.installEventFilter(self)  # 给label添加事件过滤器
        self.pushButtonShow.setToolTip("识别后的信息")
        self.labelShow.hide()

    # 在执行训练函数后锁定一些UI，禁止点击或改动。如果介绍训练，则可以改动、点击.tag为bool
    def __lockUI(self, tag=True):
        self.pushButtonSelect.setDisabled(tag)
        # self.pushButtonBack.setDisabled(tag)
        self.pushButtonWeight.setDisabled(tag)
        self.pushButtonTest.setDisabled(tag)
        self.pushButtonOpenDir.setDisabled(tag)
        self.lineEdit.setDisabled(tag)
        self.comboBoxWeight.setDisabled(tag)
        if tag:
            self.pushButtonShow.hide()
            self.__childImage = None

    def __loadingJPG(self):
        prefix = self.projectPath + "test/"  # 填写的前缀
        with open(self.projectPath + 'test.txt', 'w') as testTXT:
            fileNames = os.listdir(self.projectPath + "test/")
            for fileName in fileNames:
                if fileName[-4:] == ".jpg":
                    testTXT.write(prefix + fileName + "\n")
            testTXT.close()

    # 获取执行RunCMD线程后的数据
    def __getWeight(self, content):
        print("线程结束")
        if content == "":
            # 子线程刚执行
            txt = "程序加载中，请稍等......"
            self.labelImage.setText(txt)
        else:
            self.labelImage.setText(content)
            self.__lockUI(False)

    # 执行多DetectImage线程后的结果获取
    def __getDetectImage(self, tag, detections, class_colors):

        if tag == 0:
            self.labelImage.setText("开始加载网络")
        elif tag == 1:
            self.labelImage.setText("网络加载完成\n开始加载图片")
        elif tag == 2:
            self.labelImage.setText("网络加载完成\n图片加载完成\n开始检测图片")
        elif tag == 3:

            # print(detections)
            # print(class_colors)
            cvImage = cv2.imread(self.imageName)
            image = UseAPI.draw_boxes(detections, cvImage, class_colors)

            # 将图片转换为QImage
            qImage = QImage(image[:], image.shape[1], image.shape[0], image.shape[1] * 3, QImage.Format_RGB888)
            # 将图片转换为QPixmap方便显示
            pixmap_image = QPixmap.fromImage(qImage)
            self.__childImage = pixmap_image  # 此值用于给子界面传递
            # 使用label进行显示
            self.labelImage.setPixmap(pixmap_image)

            # imagePath = str(self.image).encode("utf-8")  # 不加后边的utf-8会导致程序错误
            # print(self.image)
            # self.getImage=GetImage(self.image)
            # self.getImage.start()
            # return
            # print(type(imagePath))
            # darknet.load_image(imagePath, 0, 0)
            # print(imagePath)

            # detections=darknet.detect_image(network, class_names, image)
            import darknet
            # image = cv2.imread(self.imageName)
            # getImage=darknet.draw_boxes(detections, img, class_colors)

            #
            # cv2.imshow("fff", getImage)
            # cv2.waitKey(0)

            self.__printLabelShow(detections)
            self.__lockUI(False)
            self.pushButtonShow.show()
            print("__getTest子线程执行完毕")
        else:
            pass

    '''
    执行多GetWeightsFile线程后的结果获取
    这里有个BUG：在子线程执行完毕后，会返回一个tag，标志权重文件夹下有文件，但如果当时正在移动文件会导致此处代码只能读取到部分文件。
    '''

    # 废弃代码-可删除
    def __getWeightFile(self, tag):
        if tag == 1:
            self.__pushButtonWeightTag = 2  # 表示有权重文件
            self.pushButtonWeight.setText("刷新权重")
            self.labelImage.clear()

    # 向LabelShow中写入内容
    def __printLabelShow(self, detections):
        # print(detections)
        if detections == "":
            self.labelShow.clear()
        else:
            objCount = 0
            objNames = set()
            objDict = {}
            for line in detections:
                objCount += 1
                if line[0] not in objNames:
                    objNames.add(line[0])
                    objDict[line[0]] = 1
                else:
                    objDict[line[0]] += 1
            showTxt = "图片中共有" + str(objCount) + "个物体\n其中"
            for name in objDict:
                showTxt += name
                showTxt += "共"
                showTxt += str(objDict[name])
                showTxt += "个\n"

            self.labelShow.setText(showTxt)

    # 本页面UI格式控制
    def __setUIStyle(self):

        self.setWindowIcon(QIcon('ArtRes/mark.png'))

        self.setWindowState(Qt.WindowMaximized)
        self.setStyleSheet("QLabel{background-color:rgb(0,0,0,155)}"
                           "QLabel{color:#F5FFFA}"
                           "QLabel{border-radius: 17px}"
                           "QLabel{font-size:25px;font-family:'楷体'}")
        self.label.setStyleSheet("QLabel{background-color:rgb(0,0,0,155)}"
                                 "QLabel{color:#F5FFFA}"
                                 "QLabel{border-radius: 17px}"
                                 "QLabel{font-size:35px;font-family:'楷体'}")
        self.lineEdit.setStyleSheet("QLineEdit{background-color:rgb(0,0,0,155)}"
                                    "QLineEdit{color:#F5FFFA}"
                                    "QLineEdit{border-radius: 17px}"
                                    "QLineEdit{font-size:20px;font-family:'楷体'}")
        self.labelWeight.setStyleSheet("QLabel{background-color:rgb(0,0,0,155)}"
                                       "QLabel{color:#F5FFFA}"
                                       "QLabel{border-radius: 17px}"
                                       "QLabel{font-size:35px;font-family:'楷体'}")
        self.comboBoxWeight.setStyleSheet("QComboBox{border-radius: 4px}"
                                          "QComboBox{font-size:35px;font-family:'楷体'}"
                                          "QComboBox{text-align:centre}"
                                          )
        self.labelImage.setWordWrap(True)
        self.pushButtonTest.setIcon(QIcon("ArtRes/start.png"))
        self.pushButtonSelect.setIcon(QIcon("ArtRes/file.png"))
        self.pushButtonBack.setIcon(QIcon("ArtRes/Cancel.png"))
