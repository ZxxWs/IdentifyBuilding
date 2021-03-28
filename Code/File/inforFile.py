import os

'''
*注意*：infor中的文字

本页代码未用

'''


class InforFile():
    def __init__(self):
        self.__dic = {"mark": "markInfor.txt"}
        self.fileDir = os.getcwd() + "/Data/"
        pass

    def getInfor(self, fileKey):
        with open(self.fileDir + self.__dic[fileKey], 'r', encoding="utf8") as file:
            doc = file.readlines()
            # print(doc)
            return doc
