import os
import sys
from time import sleep

from PyQt5 import QtCore

from PyQt5.QtCore import QThread

'''
识别单个图片的线程 
'''


class GetWeightsFile(QThread):
    GetWeightsFileSignal = QtCore.pyqtSignal(int)  # 返回的数据args:  int 0表示无

    def __init__(self, weightsPath, parent=None):
        ''''
        args:
        '''
        super().__init__(parent)
        self.weightsPath = weightsPath

    def run(self):
        print("\nGetWeights线程执行\n")

        while True:
            weightList = os.listdir(self.weightsPath)
            if len(weightList)==0:
                sleep(10)
            else:
                self.GetWeightsFileSignal.emit(1)
                break

        print("\nGetWeights线程执行完毕\n")
