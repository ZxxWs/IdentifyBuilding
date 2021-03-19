# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Test(object):
    def setupUi(self, Test):
        Test.setObjectName("Test")
        Test.resize(1000, 800)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(Test)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(Test)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(Test)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_3.addWidget(self.lineEdit)
        self.pushButtonSelect = QtWidgets.QPushButton(Test)
        self.pushButtonSelect.setObjectName("pushButtonSelect")
        self.horizontalLayout_3.addWidget(self.pushButtonSelect)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.labelImage = QtWidgets.QLabel(Test)
        self.labelImage.setText("")
        self.labelImage.setObjectName("labelImage")
        self.horizontalLayout_5.addWidget(self.labelImage)
        spacerItem = QtWidgets.QSpacerItem(10, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_5.addItem(spacerItem)
        self.horizontalLayout_5.setStretch(0, 6)
        self.horizontalLayout_5.setStretch(1, 1)
        self.verticalLayout_5.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_6.addItem(spacerItem1)
        self.progressBar = QtWidgets.QProgressBar(Test)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout_6.addWidget(self.progressBar)
        self.horizontalLayout_6.addLayout(self.verticalLayout_6)
        self.pushButtonTest = QtWidgets.QPushButton(Test)
        self.pushButtonTest.setObjectName("pushButtonTest")
        self.horizontalLayout_6.addWidget(self.pushButtonTest)
        self.horizontalLayout_6.setStretch(0, 5)
        self.horizontalLayout_6.setStretch(1, 1)
        self.verticalLayout_5.addLayout(self.horizontalLayout_6)
        self.verticalLayout_7.addLayout(self.verticalLayout_5)

        self.retranslateUi(Test)
        QtCore.QMetaObject.connectSlotsByName(Test)

    def retranslateUi(self, Test):
        _translate = QtCore.QCoreApplication.translate
        Test.setWindowTitle(_translate("Test", "测试模型"))
        self.label.setText(_translate("Test", "选择文件："))
        self.pushButtonSelect.setText(_translate("Test", "选择路径"))
        self.pushButtonTest.setText(_translate("Test", "开始识别"))

