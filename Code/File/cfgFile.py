# 写入、读取配置文件
import os
import xml.etree.ElementTree as et


class CfgFile():

    def __init__(self):
        self.__xml = {}  # 获取到的xml数据
        self.__path = os.getcwd() + "/Data/cfg.xml"  # 整个软件的配置
        # self.__path =  "../../Data/cfg.xml"  # 整个软件的配置
        # 此处未设置错误检测，如果文件夹不存在怎么办--------------------------------------------------------
        self.__tree=None
        self.__root=None

        #错误检测
        if not os.path.exists(self.__path):
            with open(self.__path, mode="w", encoding="utf-8") as f:  # 写文件,当文件不存在时,就直接创建此文件
                f.close()

                root = et.Element('MyAppCfg')
                # # 添加子节点SubElement(父节点Element对象， Tag字符串格式， Attribute字典格式)
                child1 = et.SubElement(root, 'Yolo_mark',{})
                child2 = et.SubElement(root, 'darknet',{})
                child3 = et.SubElement(root, 'conv',{})
                tree = et.ElementTree(root)
                # 在终端显示整个xml内容
                et.dump(root)
                # 写入xml文件
                tree.write(self.__path, encoding="utf-8", xml_declaration=True)


                pass
           # txt=


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
    # def getBatch(self):
    #
    #     dic = self.cfgRead()
    #     filePath = dic['cfg']
    #
    #     batch = -1
    #     with open(filePath, 'r') as file:
    #         lines = file.readlines()
    #         for line in lines:
    #             if line.find("batch=", 0, 6) != -1:
    #                 batch = int(line[6:])
    #                 return batch
    #     file.close()

    # # 设置.cfg中的batch值
    # def setBatch(self, batch):
    #     dic = self.cfgRead()
    #     filePath = dic['cfg']
    #
    #     with open(filePath, 'r') as oldFile:
    #         lines = oldFile.readlines()
    #         oldFile.close()
    #     with open(filePath, 'w') as newFile:
    #         for line in lines:
    #             if line.find("batch=", 0, 6) != -1:
    #                 line = "batch=" + batch + "\n"
    #                 print(line)
    #             newFile.write(line)
    #
    #     newFile.close()

    # # 获取mark中的obj.names的数据
    # def getMarkNames(self):
    #
    #     nameSet = set()  # 需要返回的名字集合
    #     dic = self.cfgRead()
    #     filePath = dic['Yolo_mark'] + "/data"
    #
    #     # 需要检测是否有此文件夹
    #     if not os.path.exists(filePath):
    #         os.makedirs(filePath)
    #
    #     # 通过try来防止文件不存在
    #     try:
    #         file = open(filePath + "/obj.names", 'r')
    #         names = file.readlines()
    #         for name in names:
    #             nameSet.add(name.replace("\n", ""))
    #         file.close()
    #     except IOError:
    #         file = open(filePath + "/obj.names", 'w')
    #         file.close()
    #
    #     return nameSet

    # 设置mark中的obj.names的数据
    # def setMarkNames(self, nameSet):
    #
    #     dic = self.cfgRead()
    #     filePath = dic['Yolo_mark'] + "/data"
    #
    #     # 需要向两个文件中写入东西
    #     with open(filePath + "/obj.names", 'w') as namesFile:
    #         for i in nameSet:
    #             namesFile.write(i + "\n")
    #         namesFile.close()
    #
    #     with open(filePath + "/obj.data", 'w') as dataFile:
    #         classes = "classes=" + str(len(nameSet)) + "\n"
    #         doc = '''train  = data/train.txt\nvalid  = data/train.txt\nnames = data/obj.names\nbackup = backup/'''
    #
    #         dataFile.write(classes + doc)
    #         dataFile.close()
