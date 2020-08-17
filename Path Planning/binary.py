import cv2

img = cv2.imread("C:/Users/Lenovo/Desktop/code/Object-Tracking/img/hsv_img/31.jpg")

img2 = ~img

cv2.imshow("DEBU",img2)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

cv2.imshow("Path Planning/00.jpg",binary)

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (10, 10))
cv2.MORPH_TOPHAT

dilate = cv2.dilate(binary,kernel)

cv2.imshow("DEBUG",dilate)

cv2.waitKey(0)
print(binary.shape)