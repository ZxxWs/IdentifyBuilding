'''用于处理系统中所有项目列表，参数应该是。。。。我也不知道'''
import csv
import os
import pandas as pd

from Code.File.cfgFile import CfgFile


class ProjectsManage():

    def __init__(self):

        self.returnTag = ""

        # 检测是否存在项目名单路径
        self.__filePath = os.getcwd() + "/Data/projects.csv"  # 项目列表
        if not os.path.exists(self.__filePath):
            file = open(self.__filePath, 'w')
            file.close()

            with open(self.__filePath, mode="a", newline="") as file:
                row = ["ProjectNames"]
                write = csv.writer(file)
                write.writerow(row)

        # 检测是否存在项目路径
        cfgFile = CfgFile()
        dic = cfgFile.cfgRead()

        self.__darknetDirs = dic["darknet"] + "/projects/"  # 此路径存放的是自己的项目
        if not os.path.exists(self.__darknetDirs):
            os.makedirs(self.__darknetDirs)

        self.__markDirs = dic["Yolo_mark"] + "/projects/"  # 此路径存放的是自己的项目
        if not os.path.exists(self.__markDirs):
            os.makedirs(self.__markDirs)

    def newProject(self, projectName):

        try:
            os.makedirs(self.__darknetDirs + "\\" + projectName)  # darknet项目
            os.makedirs(self.__markDirs + "\\" + projectName)  # mark项目
            with open(self.__filePath, mode="a", newline="") as file:

                row = [projectName]
                write = csv.writer(file)
                write.writerow(row)

            self.returnTag = "新建项目成功"
        except:
            print("新建项目出错")
            pass

    def delProject(self, projectName):

        try:
            os.rmdir(self.__darknetDirs + "\\" + projectName)  # darknet项目
            os.rmdir(self.__markDirs + "\\" + projectName)  # mark项目

            list=self.getProjectsList()

            data = pd.read_csv(self.__filePath)

            data_new = data.drop(list.index(projectName))  # 删除128，129，130行数据
            data_new.to_csv(self.__filePath, index=0)

        except:
            print("删除项目出错")

        pass

    def getProjectsList(self):

        # 项目列表
        projectsList = []

        with open(self.__filePath, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row is not None:
                    if row != "":
                        projectsList.append(row[0])

        return projectsList[1:]  # 返回表头
