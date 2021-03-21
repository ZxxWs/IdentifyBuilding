# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'configurate.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Configurate(object):
    def setupUi(self, Configurate):
        Configurate.setObjectName("Configurate")
        Configurate.resize(780, 273)
        Configurate.setAcceptDrops(False)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Configurate)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.tableWidget = QtWidgets.QTableWidget(Configurate)
        self.tableWidget.setGridStyle(QtCore.Qt.CustomDashLine)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(150)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(True)
        self.tableWidget.verticalHeader().setVisible(True)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setSortIndicatorShown(True)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.verticalLayout_2.addWidget(self.tableWidget)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.pushButtonCancel = QtWidgets.QPushButton(Configurate)
        self.pushButtonCancel.setObjectName("pushButtonCancel")
        self.horizontalLayout.addWidget(self.pushButtonCancel)
        self.pushButtonVerify = QtWidgets.QPushButton(Configurate)
        self.pushButtonVerify.setObjectName("pushButtonVerify")
        self.horizontalLayout.addWidget(self.pushButtonVerify)
        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.retranslateUi(Configurate)
        QtCore.QMetaObject.connectSlotsByName(Configurate)

    def retranslateUi(self, Configurate):
        _translate = QtCore.QCoreApplication.translate
        Configurate.setWindowTitle(_translate("Configurate", "项目配置"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Configurate", "配置"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Configurate", "选择"))
        self.pushButtonCancel.setText(_translate("Configurate", "取消"))
        self.pushButtonVerify.setText(_translate("Configurate", "确认"))

