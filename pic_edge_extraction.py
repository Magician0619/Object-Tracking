
import cv2
import numpy as np

color1 = 'red'
color2 = 'light_red'

color_dist = {'red': {'Lower': np.array([0, 25, 138]), 'Upper': np.array([19, 255, 255])},
              'light_red': {'Lower': np.array([178, 100, 136]), 'Upper': np.array([255, 255, 255])},
              'blue': {'Lower': np.array([100, 80, 46]), 'Upper': np.array([124, 255, 255])},
              'green': {'Lower': np.array([35, 43, 35]), 'Upper': np.array([90, 255, 255])},
              'yellow': {'Lower': np.array([26, 43, 46]), 'Upper': np.array([34, 255, 255])},
              }

#cap = cv2.VideoCapture(0)
cv2.namedWindow('camera', cv2.WINDOW_AUTOSIZE)

while True:
    frame = cv2.imread("105.jpg")

    gs_frame = cv2.GaussianBlur(frame, (5, 5), 0)                     # 高斯模糊
    hsv = cv2.cvtColor(gs_frame, cv2.COLOR_BGR2HSV)                 # 转化成HSV图像
    cv2.imshow("hsv", hsv)
    #erode_hsv = cv2.erode(hsv, None, iterations=2)                   # 腐蚀 粗的变细
    inRange_hsv1 = cv2.inRange(hsv, color_dist[color1]['Lower'], color_dist[color1]['Upper'])
    inRange_hsv2 = cv2.inRange(hsv, color_dist[color2]['Lower'], color_dist[color2]['Upper'])
    inRange_hsv = cv2.add(inRange_hsv1, inRange_hsv2)
    cv2.imshow("inRange_hsv", inRange_hsv)
    #print(inRange_hsv)
    '''
    cv2.imshow(inRange_hsv)
    gray = cv2.cvtColor(inRange_hsv, cv2.COLOR_BGR2GRAY)
    ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    print("阈值：", ret)
    cv2.imshow("binary", binary)
    '''
    cnts = cv2.findContours(inRange_hsv.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
    c = max(cnts, key=cv2.contourArea)
    rect = cv2.minAreaRect(c)
    box = cv2.boxPoints(rect)
    box_list = box.tolist()
    red_line_y = int(box_list[0][1])

    
    cv2.drawContours(frame, [np.int0(box)], -1, (0, 255, 255), 2)

    cv2.imshow('camera', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("box_list:", box_list)
        print("red_line_y", red_line_y)
        break
            
cv2.destroyAllWindows()