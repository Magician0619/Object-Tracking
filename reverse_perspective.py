import cv2
import numpy as np
img =cv2.imread('hsv_img/46.jpg')
Y, X= img.shape[:2]
print(X, Y)
list_pst=[]

def on_EVENT_LBUTTONDOWN(event, x, y, flags, param):
    list_xy = []
    if event == cv2.EVENT_LBUTTONDOWN:
        xy = "%d,%d" % (x, y)
        list_xy.append(x)
        list_xy.append(y)
        print(list_xy)
        cv2.circle(img, (x, y), 1, (255, 0, 0), thickness=-1)
        cv2.putText(img, xy, (x, y), cv2.FONT_HERSHEY_PLAIN,
                    1.0, (255, 255, 0), thickness=1)
        cv2.imshow("original_img", img)
        list_pst.append(list_xy)
        if(len(list_pst)==4):
            # 原图中书本的四个角点(左上、右上、左下、右下),与变换后矩阵位置
            pts1 = np.float32(list_pst)
            pts2 = np.float32([[0, 0], [X, 0], [0, Y], [X, Y]])

            # 生成透视变换矩阵；进行透视变换
            M = cv2.getPerspectiveTransform(pts1, pts2)
            dst = cv2.warpPerspective(img, M, (X, Y))

            cv2.imshow("result", dst)


cv2.namedWindow("original_img")
cv2.setMouseCallback("original_img", on_EVENT_LBUTTONDOWN)
cv2.imshow("original_img", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
