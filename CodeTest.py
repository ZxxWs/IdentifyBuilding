import os
import sys

from Code.File.projectsManage import ProjectsManage
from Code.File.settingYoloObjCfg import SettingYoloObjCfg

sys.path.append('../../../../CV/darknet/build/darknet/x64/darknet.py')

from Code.File.cfgFile import CfgFile


def RunDarknet(dic,image):

    a = CfgFile()
    dic = a.cfgRead()
    image = r'D:\CV\darknet\build\darknet\x64\Zxx\test\000751.jpg'

    '''原命令darknet.exe detector test data/obj.data yolo-obj.cfg yolo-obj_8000.weights'''



    CMD = dic['darknet'] + " detector test " + dic['data'] + " " + dic['cfg'] + " " + dic['weights'] + " " + image

    a = os.popen(CMD)
    print("111111111111111111111111111111111111111111111111111111111111111111111111111111111\n\n\n")
    # print(a.read())
    print("\n\n\n111111111111111111111111111111111111111111111111111111111111111111111111111111111")
    # if a!=None:

        # print("\n\n\-----------------------------n\n\n")

def getBatch(path):
    batch = -1
    with open(path, 'r') as file:
        doc=file.readlines()
        for line in doc:
            if line.find("batch=", 0, 6)!=-1:
                print(line)
                batch=int(line[6:])
                return batch


if __name__ == '__main__':
    # a = CfgFile()
    # # a.getInfor("mark")
    # dic = a.cfgRead()
    # FileDir = dic['Yolo_mark'] + '/data/img/'
    # f=str(FileDir).replace("/",'\\')
    # print(f)
    # os.system("start explorer "+f)

    # a=getBatch(dic['cfg'])
    # print(a)
    # RunDarknet(dic,image)

    # dirs=r"C:\Users\zxxw\Desktop\aa.txt"
    # if not os.path.exists(dirs):
    #     os.makedirs(dirs)

    # with open(filepath,'w') as file:
    #     file.write("sdagag")

    # b=a.getMarkNames()

    # print(b)
    # q={'C','d','y','y'}

    # print(q[0])
    # a.setMarkNames(q)
    # a=['as']
    # a[1]=234
    # print(a)
    # for i in range(10,0,1)
    # with open(dirs,'+') as file:
        # a=file.readlines()
        # print(a)

    # a=ProjectsManage()
    # a.delProject("aaa")
    # a.newProject("aaa")
    # a=ProjectSetting("A")
    a=SettingYoloObjCfg("Test")
    b=a.getSubdivisions()

    print(b)
    # a.setBatch(64)
    a.setSubdivisions(8)

    b = a.getSubdivisions()
    print(b)
    pass











