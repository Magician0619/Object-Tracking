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


imgPath="line.jpg"
img=cv2.imread(imgPath)
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# Gaussian Blur
gray=cv2.GaussianBlur(gray,(1,1),0)
# Canny 
edges = cv2.Canny(gray, 50, 200)
# Hough detect
lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 25, minLineLength=250, maxLineGap=400)
# lines = cv2.HoughLines(edges, 1, np.pi / 180, 25,20)

cv2.imshow("debug",edges)


lines1 =lines[:, 0, :]# 提取为二维
print("lines",lines)
print("lines1",lines1)
for x1, y1, x2, y2 in lines1[:]:
    cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)

for x1, y1, x2, y2 in lines1[:]:
    for x3,y3,x4,y4 in lines1[:]:
        point_is_exist, [x, y]=cross_point([x1, y1, x2, y2],[x3,y3,x4,y4])
        if point_is_exist:
            cv2.circle(img,(int(x),int(y)),5,(0,0,255),1)
cv2.imshow('Result', img)
cv2.waitKey (0)
