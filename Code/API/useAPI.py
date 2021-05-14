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
    i=1
    for label, confidence, bbox in detections:
        left, top, right, bottom = bbox2points(bbox)
        cv2.rectangle(image, (left, top), (right, bottom), colors[label], 1)
        cv2.putText(image, "{} ".format(label+str(i)),
                    (left, top - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                    colors[label], 2)
        i+=1
    return image

