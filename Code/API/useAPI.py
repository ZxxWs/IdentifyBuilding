import cv2

'''

对darknet的API的使用
使用的代码均为darknet原生

'''


def bbox2points(bbox):
    """
    From bounding box yolo format
    to corner points cv2 rectangle
    """
    x, y, w, h = bbox
    xmin = int(round(x - (w / 2)))
    xmax = int(round(x + (w / 2)))
    ymin = int(round(y - (h / 2)))
    ymax = int(round(y + (h / 2)))
    return xmin, ymin, xmax, ymax

def draw_boxes(detections, image, colors):
    '''
    在传入的图片中绘制框
    agrs:
        detections是detect_image的返回值
        image是cv2类型的图片
        colors是load_network返回的颜色
    return：
        传入的图片参数
    '''

    for label, confidence, bbox in detections:
        left, top, right, bottom = bbox2points(bbox)
        cv2.rectangle(image, (left, top), (right, bottom), colors[label], 1)
        cv2.putText(image, "{} [{:.2f}]".format(label, float(confidence)),
                    (left, top - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                    colors[label], 2)
    return image


#废弃代码，可删除
# if __name__ == '__main__':
#
#     darknetPath="D:/CV/darknet/build/darknet/x64"
#     sys.path.append(darknetPath)
#     import darknet as dr
#     #(network, class_names, image, thresh=.5, hier_thresh=.5, nms=.45):
#
#     cfgFile=CfgFile()
#     re=cfgFile.cfgRead()
#     path=re['darknet']+'/Zxx/'
#     config_file=path+"yolo-obj.cfg"
#     data_file=path+"obj.data"
#     weights=path+'backup/yolo-obj_3000.weights'
#     # network,class_names,class_colors=dr.load_network(config_file, data_file, weights)#获取到net
#     imagePath= str(path + 'test/000751.jpg').encode("utf-8")#不加后边的utf-8会导致程序错误
#     # print("\n\n\n1111111111111111111111111111111")
#     image=dr.load_image(imagePath,0,0)
#     print(image)
#     # print(image)
#     # detections=dr.detect_image(network, class_names, image)
#     # print(class_colors)
#     # dr.print_detections(detections)
#     # img = cv2.imread(path + 'test/000751.jpg')
#     # getImage=dr.draw_boxes(detections, img, class_colors)
#     # cv2.imshow("fff", getImage)
#     # cv2.waitKey(0)
#     pass
