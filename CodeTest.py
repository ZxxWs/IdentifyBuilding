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
    detections=[('building', '50.21', (466.1598815917969, 49.43111801147461, 256.301513671875, 49.0711555480957)),
     ('building', '50.62', (361.713623046875, 403.46905517578125, 110.04541015625, 53.88526153564453)),
     ('building', '51.71', (345.97857666015625, 329.8516845703125, 80.8890151977539, 46.48262405395508)),
     ('building', '55.87', (567.646728515625, 285.7109069824219, 135.83140563964844, 97.18938446044922)),
     ('building', '55.92', (140.19558715820312, 363.5030212402344, 64.48302459716797, 69.214599609375)),
     ('building', '67.86', (98.41156005859375, 310.63818359375, 97.57655334472656, 55.23553466796875)),
     ('building', '70.51', (367.7416076660156, 237.09877014160156, 85.7347640991211, 48.692466735839844)),
     ('building', '71.09', (339.1719970703125, 560.0652465820312, 82.9045181274414, 54.08489227294922)),
     ('building', '73.41', (281.9466552734375, 168.34375, 83.21052551269531, 48.9176139831543)),
     ('building', '74.56', (457.1366271972656, 261.7174377441406, 92.8212890625, 93.87470245361328)),
     ('building', '76.57', (277.7534484863281, 259.91650390625, 85.49848937988281, 54.18875503540039)),
     ('building', '77.92', (364.20147705078125, 150.44677734375, 70.82981872558594, 58.28042221069336)),
     ('building', '80.28', (194.5045166015625, 309.729736328125, 86.83853149414062, 61.64683151245117)),
     ('building', '80.64', (278.9126892089844, 78.5654296875, 96.7352294921875, 65.02455139160156)),
     ('building', '81.28', (157.33363342285156, 509.4454650878906, 79.07732391357422, 61.1795768737793)),
     ('building', '83.42', (577.6224365234375, 460.9044189453125, 117.42484283447266, 46.43890380859375)),
     ('building', '83.8', (71.4903335571289, 505.1410827636719, 111.45250701904297, 67.26787567138672)),
     ('building', '85.61', (185.717529296875, 192.633544921875, 92.65449523925781, 57.82155227661133)),
     ('building', '87.43', (269.719970703125, 353.2259826660156, 76.7021255493164, 82.2872543334961)),
     ('building', '87.84', (464.2427062988281, 401.61181640625, 91.3250732421875, 65.00070190429688)),
     ('building', '88.52', (554.59326171875, 186.7732696533203, 115.45945739746094, 48.052127838134766)),
     ('building', '89.07', (244.4369354248047, 519.1323852539062, 105.75701904296875, 64.68701934814453)),
     ('building', '90.14', (165.08506774902344, 82.9571533203125, 129.0557098388672, 57.22163391113281)),
     ('building', '91.02', (578.3577880859375, 553.13037109375, 101.04109954833984, 54.66463851928711)),
     ('building', '92.24', (111.27333068847656, 434.75335693359375, 169.1783905029297, 65.87646484375)),
     ('building', '92.78', (355.53692626953125, 470.81396484375, 89.6877670288086, 57.54628372192383)),
     ('building', '92.85', (467.8472595214844, 489.5347900390625, 77.18204498291016, 46.86838912963867)),
     ('building', '93.01', (64.94979858398438, 577.2606811523438, 92.18939971923828, 67.91141510009766)),
     ('building', '93.03', (231.89706420898438, 573.3495483398438, 107.17538452148438, 61.31240463256836)),
     ('building', '93.11', (554.03515625, 118.01678466796875, 133.16412353515625, 46.166385650634766)),
     ('building', '93.85', (249.10557556152344, 437.3499755859375, 100.62246704101562, 57.253875732421875)),
     ('building', '94.59', (571.5897216796875, 365.8482360839844, 133.35574340820312, 60.28582763671875)),
     ('building', '94.62', (97.38362884521484, 253.3587188720703, 95.88264465332031, 41.62625503540039)),
     ('building', '96.07', (469.24505615234375, 571.9503173828125, 82.29119110107422, 60.21159744262695)),
     ('building', '96.35', (78.92329406738281, 118.54701232910156, 54.71742630004883, 81.73908996582031))]

    # print(detections)
    if detections == "":
        pass
    else:
        objCount = 0
        objNames = set()
        objDict = {}
        for line in detections:
            objCount += 1
            if line[0] not in objNames:
                objNames.add(line[0])
                objDict[line[0]] = 1
            else:
                objDict[line[0]] += 1

        showTxt="图片中共有"+str(objCount)+"个物体\n其中"
        for name  in objDict:
            print(name)
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
