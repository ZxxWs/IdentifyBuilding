import os
import sys
from PyQt5 import QtCore

from PyQt5.QtCore import QThread

'''
识别单个图片的线程 
'''


class DetectImage(QThread):
    DetectImageSignal = QtCore.pyqtSignal(int,list, dict)  # 返回的数据args:

    def __init__(self, parent=None):
        super().__init__(parent)
        self.projectPath = parent.projectPath
        self.weight = parent.weightName
        self.imageName = parent.imageName

    def run(self):
        print("\nDetectImage线程执行\n")
        import darknet
        config_file = self.projectPath + "yolo-obj.cfg"
        data_file = self.projectPath + "obj.data"
        weights = self.projectPath + 'backup/' + self.weight

        print(config_file)
        print(data_file)
        print(weights)
        print(self.imageName)

        print("\nnet装载\n")

        self.DetectImageSignal.emit(0,[0], {"0":0})
        network, class_names, class_colors = darknet.load_network(config_file, data_file, weights)  # 获取到net

        self.DetectImageSignal.emit(1,[0], {"0":0})

        image = darknet.load_image(self.imageName.encode("utf-8"), 0, 0)

        self.DetectImageSignal.emit(2,[0], {"0":0})
        detections = darknet.detect_image(network, class_names, image)
        # del darknet

        self.DetectImageSignal.emit(3,detections, class_colors)

        print("\nDetectImage线程执行完毕\n")
