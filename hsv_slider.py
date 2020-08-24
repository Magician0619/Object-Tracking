# -*- coding:utf-8 -*-

import cv2
import numpy as np

"""
功能：读取一张图片，显示出来，转化为HSV色彩空间
     并通过滑块调节HSV阈值，实时显示
"""

image = cv2.imread('img/race2.jpg') # 根据路径读取一张图片
cv2.imshow("BGR", image) # 显示图片

hsv_low = np.array([25, 75, 165])
hsv_high = np.array([40, 255, 255])

def h_low(value):
    hsv_low[0] = value
    pass

def h_high(value):
    hsv_high[0] = value
    pass

def s_low(value):
    hsv_low[1] = value
    pass

def s_high(value):
    hsv_high[1] = value
    pass

def v_low(value):
    hsv_low[2] = value
    pass

def v_high(value):
    hsv_high[2] = value
    pass

def binary_HSV(img):
    hsv_low = np.array([25, 75, 165])
    hsv_high = np.array([40, 255, 255])
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV) # BGR转HSV
    dst = cv2.inRange(hsv, hsv_low, hsv_high) # 通过HSV的高低阈值，提取图像部分区域
    cv2.show("Binary HSV Outpt:",dst)
    return dst


cv2.namedWindow('image',cv2.WINDOW_NORMAL)
cv2.createTrackbar('H low', 'image', 0, 179, h_low) 
cv2.createTrackbar('H high', 'image', 0, 179, h_high)
cv2.createTrackbar('S low', 'image', 0, 255, s_low)
cv2.createTrackbar('S high', 'image', 0, 255, s_high)
cv2.createTrackbar('V low', 'image', 0, 255, v_low)
cv2.createTrackbar('V high', 'image', 0, 255, v_high)

while True:
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV) # BGR转HSV
    cv2.imshow('HSV', hsv)
    dst = cv2.inRange(hsv, hsv_low, hsv_high) # 通过HSV的高低阈值，提取图像部分区域
    cv2.imshow('output', dst)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()

