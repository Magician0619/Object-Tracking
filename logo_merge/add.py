from imutils import *
import cv2
import os 
# os.chdir('logo_merge/')

img1 = cv2.imread('logo_merge/东北大学.jpg')
img2 = cv2.imread('logo_merge/baidu.jpg')
cv2.imshow("1",img1)
cv2.imshow("2",img2)

x = np.uint8([250])
y = np.uint8([10])
print(cv2.add(x,y)) #运行结果为[[255]]
print(x+y) #运行结果为[4]

res = img1 + img2
cv2.imshow("3",res)#显示使用数组加法后的图片
add = cv2.add(img1,img2)
cv2.imshow("4",add)#显示使用OpenCV中add函数的图片
