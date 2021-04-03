from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import  Qt
from GUI.Ui_showImage import Ui_ShowImage

'''未被使用的'''


class ShowImage(QDialog, Ui_ShowImage):

    def __init__(self, image, parent=None):
        QDialog.__init__(self, parent)
        self.setupUi(self)

        # 使用label进行显示
        self.label.setPixmap(image)
        self.__setUIStyle()

    def __setUIStyle(self):
        self.label.setScaledContents(True)

        self.setWindowModality(Qt.ApplicationModal)#设置其他界面不可点击

        self.setWindowIcon(QIcon('ArtRes/showImage.png'))
        self.setStyleSheet("QLabel{background-color:rgb(255,255,255,0);border-radius: 3px;}"
                           "QLabel{color:#F5FFFA}"
                           "QLabel{font-size:24px;font-family:'楷体'}"
                           "QDialog{background-image:url(ArtRes/backgroudBlack.png)}"
                           )