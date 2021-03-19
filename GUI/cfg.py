from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog, QFileDialog
from qtpy import QtWidgets

from Code.File import File
from GUI.Ui_cfg import Ui_Cfg


class Cfg(QDialog, Ui_Cfg):

    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.setupUi(self)

        self.__cfgfile = File()
        self.__dic =self.__cfgfile.cfgRead()
        self.lineEdit.setText(self.__dic['darknet'])
        self.lineEdit_2.setText(self.__dic["data"])
        self.lineEdit_3.setText(self.__dic["cfg"])
        self.lineEdit_4.setText(self.__dic["weights"])

    @pyqtSlot()
    def on_pushButton_clicked(self):
        self.darknet ,i= QFileDialog.getOpenFileName(self, "选择文件","", "exe Files (*.exe)")
        self.lineEdit.setText(self.darknet)

    @pyqtSlot()
    def on_pushButton_2_clicked(self):
        self.data,i= QFileDialog.getOpenFileName(self, "选择文件","", "data Files (*.data)")
        self.lineEdit_2.setText(self.data)

    @pyqtSlot()
    def on_pushButton_3_clicked(self):
        self.cfg ,i= QFileDialog.getOpenFileName(self, "选择文件","", "cfg Files (*.cfg)")
        self.lineEdit_3.setText(self.cfg)

    @pyqtSlot()
    def on_pushButton_4_clicked(self):
        self.weights ,i= QFileDialog.getOpenFileName(self, "选择文件","", "weights Files (*.weights)")
        self.lineEdit_4.setText(self.weights)

    @pyqtSlot()
    def on_pushButton_5_clicked(self):
        self.__dic["darknet"]=self.lineEdit.text()
        self.__dic["data"]=self.lineEdit_2.text()
        self.__dic["cfg"]=self.lineEdit_3.text()
        self.__dic["weights"]=self.lineEdit_4.text()
        self.__cfgfile.cfgWrite(self.__dic)
