import os
import sys
import re

from Code.File.projectSetting import ProjectSetting
from Code.File.projectsManage import ProjectsManage
from Code.File.settingYoloObjCfg import SettingYoloObjCfg

sys.path.append('../../../../CV/darknet/build/darknet/x64/darknet.py')

from Code.File.cfgFile import CfgFile


def RunDarknet(dic, image):
    a = CfgFile()
    dic = a.cfgRead()
    image = r'D:\CV\darknet\build\darknet\x64\Zxx\test\000751.jpg'

    '''原命令darknet.exe detector test data/obj.data yolo-obj.cfg yolo-obj_8000.weights'''

    CMD = dic['darknet'] + " detector test " + dic['data'] + " " + dic['cfg'] + " " + dic['weights'] + " " + image

    a = os.popen(CMD)
    # print("111111111111111111111111111111111111111111111111111111111111111111111111111111111\n\n\n")
    # print(a.read())
    # print("\n\n\n111111111111111111111111111111111111111111111111111111111111111111111111111111111")
    # if a!=None:

    # print("\n\n\-----------------------------n\n\n")


def getBatch(path):
    batch = -1
    with open(path, 'r') as file:
        doc = file.readlines()
        for line in doc:
            if line.find("batch=", 0, 6) != -1:
                # print(line)
                batch = int(line[6:])
                return batch


def getNet():
    darknetPath = "D:/CV/darknet/build/darknet/x64"
    sys.path.append(darknetPath)
    import darknet as dr
    # (network, class_names, image, thresh=.5, hier_thresh=.5, nms=.45):

    cfgFile = CfgFile()
    re = cfgFile.cfgRead()
    path = re['darknet'] + '/Zxx/'
    config_file = path + "yolo-obj.cfg"
    data_file = path + "obj.data"
    weights = path + 'backup/yolo-obj_3000.weights'

    config_file = "D:/CV/darknet/build/darknet/x64/projects/Building/yolo-obj.cfg"
    data_file = "D:/CV/darknet/build/darknet/x64/projects/Building/obj.data"
    weights = 'D:/CV/darknet/build/darknet/x64/projects/Building/backup/yolo-obj_1000.weights'

    network, class_names, class_colors = dr.load_network(config_file, data_file, weights)  # 获取到net
    # imagePath = str(path + 'test/000751.jpg').encode("utf-8")  # 不加后边的utf-8会导致程序错误
    print("\n\n\n1111111111111111111111111111111")
    # image = dr.load_image(imagePath, 0, 0)
    # print(imagePath)
    # print(image)
    # detections=dr.detect_image(network, class_names, image)
    # print(class_colors)
    # dr.print_detections(detections)
    # img = cv2.imread(path + 'test/000751.jpg')
    # getImage=dr.draw_boxes(detections, img, class_colors)
    # cv2.imshow("fff", getImage)
    # cv2.waitKey(0)
    pass


# 向LabelShow中写入内容
def printLabelShow():
    'left, top, right, bottom'

    detections = [('building', '54.83', (187.43710327148438, 54.55423355102539, 354.6364440917969, 54.226985931396484)),
                  ('building', '56.12', (296.5267639160156, 452.07427978515625, 85.52815246582031, 468.573486328125)),
                  ('building', '60.1', (45.269962310791016, 501.6891174316406, 37.5923957824707, 91.57903289794922)),
                  ('building', '68.6', (499.6297912597656, 385.7499694824219, 51.30361557006836, 195.7060546875)),
                  ('building', '68.75', (46.710269927978516, 595.5431518554688, 44.073875427246094, 66.75074005126953)),
                  ('building', '73.63', (364.4673156738281, 151.61697387695312, 90.68917846679688, 177.79266357421875)),
                  ('building', '74.44', (173.07843017578125, 538.13916015625, 59.01683044433594, 191.9545135498047)),
                  ('building', '74.58', (618.5853881835938, 109.85498046875, 45.47235870361328, 194.1161651611328)),
                  ('building', '78.26', (620.0382080078125, 382.6069641113281, 59.16907501220703, 278.9908752441406)),
                  ('building', '86.6', (248.9439239501953, 536.101318359375, 65.2662124633789, 208.4380645751953)),
                  ('building', '86.68', (536.396484375, 556.8419189453125, 49.900413513183594, 152.9242706298828)),
                  ('building', '87.0', (95.50930786132812, 540.9893188476562, 56.98250198364258, 142.55625915527344)),
                  ('building', '89.24', (624.2867431640625, 449.7984313964844, 45.34479904174805, 108.99993133544922)),
                  ('building', '89.33', (544.6242065429688, 385.287109375, 63.15155029296875, 223.3192596435547)),
                  ('building', '90.87', (431.75146484375, 457.1698303222656, 133.15432739257812, 310.9854431152344)),
                  ('building', '94.25', (162.76873779296875, 214.8499298095703, 265.9153137207031, 52.24889373779297)),
                  (
                  'building', '94.83', (535.4871826171875, 121.21832275390625, 151.15817260742188, 168.41839599609375))]

    buildingCount = 1
    for label, confidence, bbox in detections:
        pass

    # print(detections)
    # if detections == "":
    #     pass
    # else:
    #     objCount = 0
    #     objNames = set()
    #     objDict = {}
    #     for line in detections:
    #         objCount += 1
    #         if line[0] not in objNames:
    #             objNames.add(line[0])
    #             objDict[line[0]] = 1
    #         else:
    #             objDict[line[0]] += 1
    #
    #     showTxt = "图片中共有" + str(objCount) + "个物体\n其中"
    #     for name in objDict:
    #         print(name)
    # print(key)


if __name__ == '__main__':
    # a = CfgFile()
    # a.getInfor("mark")
    # dic = a.cfgRead()
    # print(dic)
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
    # a=SettingYoloObjCfg("Test")
    # b=a.getSubdivisions()

    # print(b)
    # a.setBatch(64)
    # a.setSubdivisions(8)

    # b = a.getSubdivisions()
    # print(b)

    # a=ProjectSetting("A")
    # b=a.getObjNames()
    # print(b)

    # while True:
    #     get = input("输入字符串")
    #     pattern = re.compile('^[A-Za-z][A-Za-z0-9_]{1,10}$')
    #     rr=pattern.findall(get)
    #     print(rr)
    #
    #     # print(pattern)
    #     # print(re.compile())

    # getNet()
    # a=('building', '53.36', (518.3615112304688, 577.2810668945312, 49.0134391784668, 63.057125091552734))
    # print(type(a))
    printLabelShow()

    pass
