# 写入、读取配置文件
import os
import xml.etree.ElementTree as et


class File():

    def __init__(self):
        self.__xml = {}  # 获取到的xml数据
        self.__path = os.getcwd() + "/Data/cfg.xml"  # 整个软件的配置
        # 此处未设置错误检测，如果文件夹不存在怎么办--------------------------------------------------------

    def cfgRead(self):

        self.__tree = et.parse(self.__path)
        self.__root = self.__tree.getroot()
        for child in self.__root:
            self.__xml[child.tag] = child.text
        return self.__xml

    # 此处的data是个字典
    def cfgWrite(self, data):
        for child in self.__root:
            child.text = data[child.tag]
            print(child.text)
        self.__tree.write(self.__path)

    # 获取.cfg中的batch值
    def getBatch(self):

        dic = self.cfgRead()
        filePath = dic['cfg']

        batch = -1
        with open(filePath, 'r') as file:
            lines = file.readlines()
            for line in lines:
                if line.find("batch=", 0, 6) != -1:
                    batch = int(line[6:])
                    return batch
        file.close()

    def setBatch(self, batch):
        dic = self.cfgRead()
        filePath = dic['cfg']

        with open(filePath, 'r') as oldFile:
            lines = oldFile.readlines()
            oldFile.close()
        with open(filePath, 'w') as newFile:
            for line in lines:
                if line.find("batch=", 0, 6) != -1:
                    line = "batch=" + batch + "\n"
                    print(line)
                newFile.write(line)

        newFile.close()

    def getMarkNames(self):
        nameList = []
        dic = self.cfgRead()
        filePath = dic['Yolo_mark'] + "/data"
        if not os.path.exists(filePath):
            os.makedirs(filePath)

        with open(filePath + "/obj.names", 'r') as file:
            names = file.readlines()

            for name in names:
                nameList.append(name)

        return nameList


    def setMarkNames(self,namelist):

        dic = self.cfgRead()
        filePath = dic['Yolo_mark'] + "/data"

        #需要向两个文件中写入东西
        pass