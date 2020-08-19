import cv2
import numpy as np

img = cv2.imread("C:/Users/Lenovo/Desktop/code/Object-Tracking/img/hsv_img/31.jpg")

img2 = ~img

# cv2.imshow("DEBU",img3)

gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

cv2.imshow("Path Planning",binary)

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))

#菱形结构元素的定义稍麻烦一些
Triangle = cv2.getStructuringElement(cv2.MORPH_RECT,(5, 5))
Triangle[0, 0] = 0
Triangle[0, 1] = 0
Triangle[0, 3] = 0
Triangle[0, 4] = 0
Triangle[1, 0] = 0
Triangle[1, 1] = 0
Triangle[1, 3] = 0
Triangle[1, 4] = 0
Triangle[2, 0] = 0
Triangle[2, 4] = 0
Triangle[3, 4] = 0
Triangle[3, 0] = 0




dilate1 = cv2.erode(binary,kernel,50)
dilate2 = cv2.erode(binary,Triangle,50)

cv2.imshow("DEBUG1",dilate1)
cv2.imshow("DEBUG2",dilate2)

cv2.waitKey(0)
print(binary.shape)