# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'train.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Train(object):
    def setupUi(self, Train):
        Train.setObjectName("Train")
        Train.resize(1000, 800)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(Train)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_1 = QtWidgets.QLabel(Train)
        self.label_1.setObjectName("label_1")
        self.verticalLayout_5.addWidget(self.label_1)
        self.horizontalLayout_4.addLayout(self.verticalLayout_5)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.pushButton_3 = QtWidgets.QPushButton(Train)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_6.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(Train)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_6.addWidget(self.pushButton_4)
        self.horizontalLayout_4.addLayout(self.verticalLayout_6)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(Train)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.comboBox = QtWidgets.QComboBox(Train)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout_2.addWidget(self.comboBox)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_2 = QtWidgets.QPushButton(Train)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_3.addWidget(self.pushButton_2)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem3)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.pushButton = QtWidgets.QPushButton(Train)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_5.addWidget(self.pushButton)
        self.pushButtonBack = QtWidgets.QPushButton(Train)
        self.pushButtonBack.setObjectName("pushButtonBack")
        self.horizontalLayout_5.addWidget(self.pushButtonBack)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.verticalLayout_2.setStretch(0, 4)
        self.verticalLayout_2.setStretch(1, 1)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        spacerItem4 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.horizontalLayout.setStretch(1, 3)
        self.horizontalLayout.setStretch(3, 2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem5)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.retranslateUi(Train)
        QtCore.QMetaObject.connectSlotsByName(Train)

    def retranslateUi(self, Train):
        _translate = QtCore.QCoreApplication.translate
        Train.setWindowTitle(_translate("Train", "训练模型"))
        self.label_1.setText(_translate("Train", "TextLabel"))
        self.pushButton_3.setText(_translate("Train", "PushButton"))
        self.pushButton_4.setText(_translate("Train", "PushButton"))
        self.label_2.setText(_translate("Train", "Batch:"))
        self.comboBox.setItemText(0, _translate("Train", "1"))
        self.comboBox.setItemText(1, _translate("Train", "2"))
        self.comboBox.setItemText(2, _translate("Train", "4"))
        self.comboBox.setItemText(3, _translate("Train", "6"))
        self.comboBox.setItemText(4, _translate("Train", "8"))
        self.comboBox.setItemText(5, _translate("Train", "16"))
        self.comboBox.setItemText(6, _translate("Train", "32"))
        self.comboBox.setItemText(7, _translate("Train", "64"))
        self.pushButton_2.setText(_translate("Train", "PushButton"))
        self.pushButton.setText(_translate("Train", "开始训练"))
        self.pushButtonBack.setText(_translate("Train", "返回"))

