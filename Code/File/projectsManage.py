'''用于处理系统中所有项目列表，参数应该是。。。。我也不知道'''
import csv
import os
import shutil

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
            darknet = self.__darknetDirs + projectName
            mark = self.__markDirs + projectName

            if self.__createFileAndDirs(darknet, mark, projectName):
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

            print("删除项目" + self.__darknetDirs + projectName)

            darknet = self.__darknetDirs + projectName
            mark = self.__markDirs + projectName

            shutil.rmtree(darknet)# darknet项目
            shutil.rmtree(mark) # mark项目

            print("删除项目文件完毕")

            #下面的命令只能删除空文件夹
            # os.rmdir(darknete)  # darknet项目
            # os.rmdir(mark)  # mark项目

            projectlist = self.getProjectsList()

            data = pd.read_csv(self.__filePath)
            data_new = data.drop(projectlist.index(projectName))
            data_new.to_csv(self.__filePath, index=0)

        except:
            print("删除项目出错")



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

    def __createFileAndDirs(self, darknet, mark, projectName):

        try:
            # 新建两个主文件夹
            os.makedirs(darknet)  # darknet项目
            os.makedirs(mark)  # mark项目

            # 新建各个文件和文件夹
            # Darknet-----------------------------------------
            os.makedirs(darknet + '\\test')
            os.makedirs(darknet + '\\backup')
            os.makedirs(darknet + '\\train')

            cfg = os.getcwd() + "/Data/yolo-obj.cfg"  # 整个软件的配置
            shutil.copy(cfg, darknet)  # 添加yolo-obj.cfg文件

            self.__createObjData(darknet, projectName)

            # Mark-----------------------------------------
            os.makedirs(mark + '\\img')

            return True
        except:
            return False

    def __createObjData(self, darknet, projectName):

        txt = ""

        with open(darknet + '/obj.data', 'w') as file:
            file.write("classes=0\n")
            file.write("train=project/" + projectName + "/train.txt\n")
            file.write("valid=project/" + projectName + "/test.txt\n")
            file.write("names= " + darknet + "/obj.names\n")
            file.write("backup=" + darknet + "/backup/")

            pass
