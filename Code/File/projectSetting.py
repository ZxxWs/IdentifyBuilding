from Code.File.cfgFile import CfgFile

'''
对于单独一个项目数据内容管理
'''


class ProjectSetting():

    def __init__(self, projectName):
        self.__projectName = projectName
        cfgFile = CfgFile()
        cfg = cfgFile.cfgRead()
        self.__filePath = cfg['darknet'] + "/projects/" + projectName + "/obj.names"

    def getObjNames(self):
        with open(self.__filePath, 'r') as file:
            nameList = file.readlines()

        return nameList
