# -*- coding:utf-8 -*-

'''
#@Author: Magician
#@Date: 2020-08-07 20:08:41
#@Description: Detect AprilTag and return relevant coordinates infomation

Copyright 2020 by Magician
'''

import pupil_apriltags as apriltag     # for windows
import cv2
import numpy as np
import sys


def degrees(radians):
    '''

    '''
    return (180 * radians) / math.pi

def tag(img_tag):
    '''
    img type: narry unit 8 

    '''

    img_tag = cv2.cvtColor(img_tag, cv2.COLOR_BGR2GRAY)

    tag_detector = apriltag.Detector()
    tags = tag_detector.detect(img_tag) # The image must be a grayscale image of type numpy.uint8

    # for tag in img.find_apriltags(fx=f_x, fy=f_y, cx=c_x, cy=c_y): # default family "TAG36H11"
    for tag in tags:
        
        cv2.circle(img, tuple(tag.corners[0].astype(int)), 4,(0,0,255), 2) # left-top
        cv2.circle(img, tuple(tag.corners[1].astype(int)), 4,(0,0,255), 2) # right-top
        cv2.circle(img, tuple(tag.corners[2].astype(int)), 4,(0,0,255), 2) # right-bottom
        cv2.circle(img, tuple(tag.corners[3].astype(int)), 4,(0,0,255), 2) # left-bottom
        
  
if __name__ == '__main__':
    img = cv2.imread("test.jpg")
    tag(img)
    cv2.imshow("dst", img)
    cv2.waitKey()




