# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'alert.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Alert(object):
    def setupUi(self, Alert):
        Alert.setObjectName("Alert")
        Alert.resize(830, 289)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Alert)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Alert)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.pushButton = QtWidgets.QPushButton(Alert)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Alert)
        QtCore.QMetaObject.connectSlotsByName(Alert)

    def retranslateUi(self, Alert):
        _translate = QtCore.QCoreApplication.translate
        Alert.setWindowTitle(_translate("Alert", "警告"))
        self.label.setText(_translate("Alert", "TextLabel"))
        self.pushButton.setText(_translate("Alert", "PushButton"))

