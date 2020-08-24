# -*- coding:utf-8 -*-

import cv2
import numpy as np
from urllib import request

"""
功能：读取一张图片，显示出来，转化为HSV色彩空间
     并通过滑块调节HSV阈值，实时显示

/usr/local/bin/mjpg_streamer -i "/usr/local/lib/mjpg-streamer/input_uvc.so -d /dev/video2 -n -f 30 -r 320x240" -o "/usr/local/lib/mjpg-streamer/output_http.so -p 8080 -w /usr/local/share/mjpg-streamer/www"
"""

#cv2.imshow("BGR", image) # 显示图片
# Threshold of yellow lane
lower_race = np.array([25, 75, 165])
upper_race = np.array([40, 255, 255])
# Threshold of blue cone
lower_blue = np.array([83, 222, 168])
upper_blue = np.array([102, 255, 255])
# Threshold of red cone
lower_red = np.array([120, 100, 100])
upper_red = np.array([200, 255, 255])
# Threshold of gray ground
lower_hsv = np.array([0,0,140])
upper_hsv = np.array([255,100,255])

# 强光环境下，165改成195
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
    # cv2.show("Binary HSV Outpt:",dst)
    return dst


cv2.namedWindow('image',cv2.WINDOW_FREERATIO)
cv2.createTrackbar('H low', 'image', 0, 179, h_low) 
cv2.createTrackbar('H high', 'image', 0, 179, h_high)
cv2.createTrackbar('S low', 'image', 0, 255, s_low)
cv2.createTrackbar('S high', 'image', 0, 255, s_high)
cv2.createTrackbar('V low', 'image', 0, 255, v_low)
cv2.createTrackbar('V high', 'image', 0, 255, v_high)


url = "http://192.168.0.254:8080/?action=snapshot"  
# url = "http://192.168.0.254:8080/stream.html"
def downloadImg():
    global url
    with request.urlopen(url) as f:
        data = f.read()
        img1 = np.frombuffer(data, np.uint8)
        #print("img1 shape ", img1.shape) # (83653,)
        img_cv = cv2.imdecode(img1, cv2.IMREAD_ANYCOLOR)
        return img_cv

while True:
    # image = downloadImg() 
    image = downloadImg() #cv2.imread('1.jpg') # 根据路径读取一张图片
    cv2.imshow('input', image)
    dst = cv2.cvtColor(image, cv2.COLOR_BGR2HSV) # BGR转HSV
    dst = cv2.inRange(dst, hsv_low, hsv_high) # 通过HSV的高低阈值，提取图像部分区域
    cv2.imshow('output', dst)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cv2.destroyAllWindows()


