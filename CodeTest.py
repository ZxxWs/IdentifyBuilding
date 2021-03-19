import os
import sys
sys.path.append('../../../../CV/darknet/build/darknet/x64/darknet.py')



from time import sleep

from Code.File import File


def RunDarknet(dic,image):

    a = File()
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
    a = File()
    # dic = a.cfgRead()

    # a=getBatch(dic['cfg'])
    # print(a)
    # RunDarknet(dic,image)

    # dirs=r"C:\Users\zxxw\Desktop\A\\"
    # if not os.path.exists(dirs):
    #     os.makedirs(dirs)

    # with open(filepath,'w') as file:
    #     file.write("sdagag")

    # a=File.getMarkNames("")
    # print(a)
    a=['as']
    # a[1]=234
    # print(a)
    # for i in range(10,0,1)


    pass











