from Code.File.cfgFile import CfgFile

'''此类用于处理各个项目的 yolo-obj.cfg设置'''


class SettingYoloObjCfg():

    def __init__(self, projectName):
        cfgFile = CfgFile()
        dic = cfgFile.cfgRead()
        self.filePath = dic["darknet"] + "/projects/" + projectName + "/yolo-obj.cfg"  # 此路径存放的是自己项目的yolo-obj.cfg

    # 获取.cfg中的batch值
    def getBatch(self):
        batch = -1
        with open(self.filePath, 'r') as file:
            lines = file.readlines()
            for line in lines:
                if line.find("batch=", 0, 6) != -1:
                    batch = int(line[6:])
                    file.close()
                    return batch

    # 设置.cfg中的batch值,此处的Batch是int类型
    def setBatch(self, batch):
        with open(self.filePath, 'r') as oldFile:
            lines = oldFile.readlines()
            oldFile.close()
        with open(self.filePath, 'w') as newFile:
            for line in lines:
                if line.find("batch=", 0, 6) != -1:
                    line = "batch=" + str(batch) + "\n"
                newFile.write(line)
            newFile.close()

    # 设置.cfg中的subdivisions值,此处的subdivisions是int类型
    def setSubdivisions(self, subdivisions):
        with open(self.filePath, 'r') as oldFile:
            lines = oldFile.readlines()
            oldFile.close()
        with open(self.filePath, 'w') as newFile:
            for line in lines:
                if line.find("subdivisions=", 0, 13) != -1:
                    line = "subdivisions=" + str(subdivisions) + "\n"
                newFile.write(line)
            newFile.close()

    def getSubdivisions(self):
        subdivisions = -1
        with open(self.filePath, 'r') as file:
            lines = file.readlines()
            for line in lines:
                if line.find("subdivisions=", 0, 13) != -1:
                    subdivisions = int(line[13:-1])
                    file.close()
                    return subdivisions

    '''
    本方法用于处理和classes有关的数据
    1.max_batches=classes*2000(but不少于训练图片数量、不少于6000
    2.steps to 80% and 90% of max_batches
    4.classes=xx
    change [filters=255] to filters=(classes + 5)x3 in the 3 [convolutional] before each [yolo] layer, keep in mind that it only has to be the last [convolutional] before each of the [yolo] layers.
    '''
    def setAboutClasses(self, classes=1):

        # 获取旧文件内容
        with open(self.filePath, 'r') as oldFile:
            lines = oldFile.readlines()
            oldFile.close()

        lineClasses = "classes=" + str(classes) + "\n"
        if classes >= 3:
            max_batches = classes * 2000
        else:
            max_batches = 6000
        lineMax_batche = "max_batches=" + str(max_batches) + '\n'
        lineSteps = "steps=" + str(int(max_batches * 0.8)) + "," + str(int(max_batches * 0.9)) + "\n"
        lineFilters = "filters=" + str((classes + 5) * 3) + "\n"

        with open(self.filePath, 'w') as newFile:

            lines[19] = lineMax_batche
            lines[21] = lineSteps
            lines[969] = lineClasses
            lines[1057] = lineClasses
            lines[1145] = lineClasses
            lines[962] = lineFilters
            lines[1050] = lineFilters
            lines[1138] = lineFilters

            for line in lines:
                newFile.write(line)
            newFile.close()


