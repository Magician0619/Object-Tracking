import cv2
import math
import numpy as np
cap = cv2.VideoCapture(0)
 
def undistort(frame):
    fx = 305.6261999368051
    cx = 169.9830363751688
    fy = 344.2600716547944
    cy = 73.945565684040190
    k1, k2, p1, p2, k3 = -0.435917245316158, 0.206260536218705, 0.0, 0.0, 0.0
 
    # 相机坐标系到像素坐标系的转换矩阵
    k = np.array([
        [fx, 0, cx],
        [0, fy, cy],
        [0, 0, 1]
    ])
    # 畸变系数
    d = np.array([
        k1, k2, p1, p2, k3
    ])
    h, w = frame.shape[:2]
    mapx, mapy = cv2.initUndistortRectifyMap(k, d, None, k, (w, h), 5)
    return cv2.remap(frame, mapx, mapy, cv2.INTER_LINEAR)
 


def solve():

    H = 1.28  #相机安装高度
    erfa = float(3.14*0)/180  #相机安装俯仰角
    yaw = float(7.2*0)/180 #相机安装的偏转角,偏右
    u0 = 780
    v0 = 380
    fx = 1857.481736
    fy = 1872.211946

    u=1616 #像素坐标
    v=520
    #这里把目标看作一个点，该点为其矩形轮廓的最下沿的中心点
    #Y=fy*H/abs(v-v0)#纵向
    Y = float(H) / math.tan(erfa - math.atan(float(v0 - v) / fy))#纵向
    X = float((u0 - u) * H) / (math.sqrt(fx * fx + (v - v0) * (v - v0)) * math.sin(erfa - math.atan(float(v0 - v) / fy)))#横向
    x =  X * math.sin(yaw) + Y * math.cos(yaw) #目标距离相机的横向距离
    y =  X * math.cos(yaw) - Y * math.sin(yaw) #目标距离相机的纵向距离


     
# while(cap.isOpened()):
#     ret, frame = cap.read()
#    # frame =
#     cv2.imshow('frame', undistort(frame))
 
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
# cap.release()
# cv2.destroyAllWindows()
frame = cv2.imread("175.jpg")
cv2.imshow('frame', undistort(frame))
cv2.waitKey(0)
 
