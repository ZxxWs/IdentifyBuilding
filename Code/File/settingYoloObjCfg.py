'''此类用于处理各个项目的 yolo-obj.cfg设置'''
from Code.File.cfgFile import CfgFile


class SettingYoloObjCfg():

    def __init__(self, projectName):
        cfgFile = CfgFile()
        dic = cfgFile.cfgRead()

        self.filePath = dic["darknet"] + "/projects/" + projectName + "/yolo-obj.cfg"  # 此路径存放的是自己项目的yolo-obj.cfg

    # 获取.cfg中的batch值
    def getBatch(self):
            # dic = self.cfgRead()
            # filePath = dic['cfg']

            batch = -1
            with open(self.filePath, 'r') as file:
                lines = file.readlines()
                for line in lines:
                    if line.find("batch=", 0, 6) != -1:
                        batch = int(line[6:])
                        file.close()
                        return batch

            # 设置.cfg中的batch值

    def setBatch(self, batch):

        with open(self.filePath, 'r') as oldFile:
            lines = oldFile.readlines()
            oldFile.close()
        with open(self.filePath, 'w') as newFile:
            for line in lines:
                if line.find("batch=", 0, 6) != -1:
                    line = "batch=" + batch + "\n"
                    # print(line)
                newFile.write(line)

            newFile.close()

    def setSubdivisions(self):
        pass



    def setBatch(self):
        pass
