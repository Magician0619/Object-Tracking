# -*- coding: UTF-8 -*-
import cv2
import numpy as np

def cross_point(line1, line2):  # 计算交点函数
    #是否存在交点
    point_is_exist=False
    x=0
    y=0
    x1 = line1[0]  # 取四点坐标
    y1 = line1[1]
    x2 = line1[2]
    y2 = line1[3]

    x3 = line2[0]
    y3 = line2[1]
    x4 = line2[2]
    y4 = line2[3]

    if (x2 - x1) == 0:
        k1 = None
    else:
        k1 = (y2 - y1) * 1.0 / (x2 - x1)  # 计算k1,由于点均为整数，需要进行浮点数转化
        b1 = y1 * 1.0 - x1 * k1 * 1.0  # 整型转浮点型是关键

    if (x4 - x3) == 0:  # L2直线斜率不存在操作
        k2 = None
        b2 = 0
    else:
        k2 = (y4 - y3) * 1.0 / (x4 - x3)  # 斜率存在操作
        b2 = y3 * 1.0 - x3 * k2 * 1.0

    if k1 is None:
        if not k2 is None:
            x = x1
            y = k2 * x1 + b2
            point_is_exist=True
    elif k2 is None:
        x=x3
        y=k1*x3+b1
    elif not k2==k1:
        x = (b2 - b1) * 1.0 / (k1 - k2)
        y = k1 * x * 1.0 + b1 * 1.0
        point_is_exist=True
    return point_is_exist,[x, y]

def denoising(img):
    '''
    Only reserve yellow car lines to caculate the cross points
    '''

    lower_hsv = np.array([25, 75, 165])
    upper_hsv = np.array([40, 255, 255])

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lowerb=lower_hsv, upperb=upper_hsv)
    
    race_res = cv2.bitwise_and(img, img, mask = mask)
    race_res = race_res[:,:,::-1]
    # cv2.imshow("HSV",race_res)
    # cv2.imwrite("debug.jpg",race_res)
    return race_res


img = cv2.imread("line.jpg")

hsv = denoising(img)

gray = cv2.cvtColor(hsv,cv2.COLOR_BGR2GRAY)

gray = cv2.GaussianBlur(gray,(3,3),0)

edges = cv2.Canny(gray, 50, 200)
# edges = gray

lines = cv2.HoughLinesP(edges, 10, 5*np.pi / 180, 50, minLineLength=250, maxLineGap=400)
# lines = cv2.HoughLines(edges, 1, np.pi / 180, 25,20)

cv2.imshow("debug",edges)


lines_hough =lines[:, 0, :]# 提取为二维

# print("lines1",lines_hough)
for x1, y1, x2, y2 in lines_hough[:]:
    cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)
    cv2.imshow('Result', img)

for x1, y1, x2, y2 in lines_hough[:]:
    for x3,y3,x4,y4 in lines_hough[:]:
        point_is_exist, [x, y]=cross_point([x1, y1, x2, y2],[x3,y3,x4,y4])
        if point_is_exist:
            cv2.circle(img,(int(x),int(y)),5,(0,0,255),1)
            print("detect points:%d,%d"%(x,y))

            # cv2.putText(img, text = str(x)+','+str(y), org = (int(x),int(y)+50), 
                        # fontFace=cv2.FONT_HERSHEY_TRIPLEX, fontScale = 1, color = (255,0,0))
cv2.imshow('Result', img)
cv2.imwrite("result.jpg",img)

cv2.waitKey (0)
