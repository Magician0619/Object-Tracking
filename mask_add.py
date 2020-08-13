# -*- coding:utf-8 -*-

'''
#@Author: Magician
#@Date: 2020-08-11 15:54:07
#@Description: Extract specific colors from the race track in HSV color space， and combine them

Copyright 2020 by Magician
'''
import cv2
import numpy as np
import matplotlib.pyplot as plt

def mask_add(frame):
    '''
    img type: narry unit 8 
    '''

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Threshold of yellow lane
    lower_race = np.array([25, 75, 165])
    upper_race = np.array([40, 255, 255])
    
    # Threshold of red cone
    lower_red = np.array([0, 100, 100])
    upper_red = np.array([10, 255, 255])

    # Threshold of blue cone
    lower_blue = np.array([110, 100,100])
    upper_blue = np.array([130, 255, 255])

    race_mask = cv2.inRange(hsv, lower_race, upper_race)
    red_mask = cv2.inRange(hsv, lower_red, upper_red)
    blue_mask = cv2.inRange(hsv, lower_blue, upper_blue)

    race_res = cv2.bitwise_and(frame, frame, mask = race_mask)
    red_res = cv2.bitwise_and(frame, frame, mask = red_mask)
    blue_res = cv2.bitwise_and(frame,frame, mask = blue_mask)

    res = race_res + red_res + blue_res

    # BGR 2 RGB, but use for display!!!
    '''
    frame = frame[:,:,::-1]
    race_res = race_res[:,:,::-1]
    cone_res = cone_res[:,:,::-1]
    res = res[:,:,::-1]
    '''
    return res

def mask_revise(frame):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
       
    # Threshold of yellow lane
    lower_race = np.array([25, 75, 165])
    upper_race = np.array([40, 255, 255])
    # Threshold of red cone
    lower_red = np.array([0, 100, 100])
    upper_red = np.array([20, 255, 255])

    race_mask = cv2.inRange(hsv, lower_race, upper_race)
    red_mask = cv2.inRange(hsv, lower_red, upper_red)
    res_all = race_mask + red_mask
    cv2.imshow("all_add",res_all)


    race_res = cv2.bitwise_and(frame, frame, mask = race_mask)
    red_res = cv2.bitwise_and(frame, frame, mask = red_mask)
    res = race_res + red_res

    return res

if __name__ == '__main__':

    img = cv2.imread('886.jpg')
    res = mask_revise(img)
    cv2.imwrite("maskadd1.jpg",res)
    # plt.figure(figsize=(14,12))
    cv2.imshow("dst",res)
    cv2.waitKey(0)
    '''
    plt.figure(figsize=(14,12))
    plt.subplot(2,2,1),plt.title('original_image'), plt.imshow(res)
    plt.subplot(2,2,2), plt.imshow(blue_mask, cmap = 'gray')
    plt.subplot(2,2,3), plt.imshow(green_mask, cmap= 'gray')
    plt.subplot(2,2,4), plt.imshow(red_mask, cmap= 'gray')
    
    plt.figure(figsize=(14,12))
    plt.subplot(2,2,1), plt.imshow(blue_res)
    plt.subplot(2,2,2), plt.imshow(green_res)
    plt.subplot(2,2,3), plt.imshow(red_res)
    plt.subplot(2,2,4), plt.imshow(res)
    plt.show()
    '''