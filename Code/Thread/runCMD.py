import os
from PyQt5 import QtCore
from PyQt5.QtCore import QThread

'''
此类执行一些需要开辟线程的cmd命令
'''


class RunCMD(QThread):

    RunCMDSignal = QtCore.pyqtSignal(str)  # 返回的数据

    # 参数CMD是执行的命令，head，end是cmd执行后的输出内容列表化的头尾
    def __init__(self, CMD, head=0, end=-1, parent=None):
        super().__init__(parent)
        self.CMD = CMD
        self.head = head
        self.end = end

    def run(self):
        print("\nRunCMD线程执行\n")
        self.RunCMDSignal.emit("")
        output = os.popen(self.CMD)
        content = output.readlines()
        txt = ""
        for i in range(self.head, self.end, 1):
            txt += content[i]
        self.RunCMDSignal.emit(txt)
