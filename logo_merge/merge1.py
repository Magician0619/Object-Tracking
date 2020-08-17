import cv2
import numpy as np
import matplotlib.pyplot as plt
import os 
# os.chdir('C:/Users/lenovo/Desktop/')

bear = cv2.imread('logo_merge/baidu.jpg')
sky = cv2.imread('logo_merge/neuq.jpg')

rows, cols = sky.shape[:2] #获取sky的高度、宽度
#print(sky.shape[:2]) #(800, 1200)
#print(bear.shape[:2]) #(224, 224)
bear_dst = cv2.resize(bear,(cols,rows),interpolation=cv2.INTER_CUBIC) #放大图像
add_img = cv2.addWeighted(bear_dst,0.6,sky,0.4,0) #图像融合

# 显示图片
titles = ['BearBrown','Sky','add_img']
imgs = [bear,sky,add_img]
for i in range(len(imgs)):
    plt.subplot(2,3,i+1)
    imgs[i]=cv2.cvtColor(imgs[i],cv2.COLOR_BGR2RGB)
    plt.imshow(imgs[i],'gray')
    plt.title(titles[i])
    plt.axis('off')
plt.show()
