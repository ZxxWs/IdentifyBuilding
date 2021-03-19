# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mark.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Mark(object):
    def setupUi(self, Mark):
        Mark.setObjectName("Mark")
        Mark.resize(746, 574)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(Mark)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Mark)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton = QtWidgets.QPushButton(Mark)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout.setStretch(0, 9)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.retranslateUi(Mark)
        QtCore.QMetaObject.connectSlotsByName(Mark)

    def retranslateUi(self, Mark):
        _translate = QtCore.QCoreApplication.translate
        Mark.setWindowTitle(_translate("Mark", "配置路径"))
        self.label.setText(_translate("Mark", "TextLabel"))
        self.pushButton.setText(_translate("Mark", "PushButton"))

