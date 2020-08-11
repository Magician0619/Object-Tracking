# -*- coding:utf-8 -*-

'''
#@Author: Magician
#@Date: 2020-08-07 20:08:41
#@Description: Detect AprilTag and return relevant coordinates infomation

Copyright 2020 by Magician
'''

import pupil_apriltags as apriltag     
import cv2
import numpy as np
import sys

img =cv2.imread("test.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)    # The image must be a grayscale image of type numpy.uint8


# Build a detector for apriltag
tag_detector = apriltag.Detector()  

# Perform apriltag detection to get a list of detected apriltag
tags = tag_detector.detect(gray)

print("%d apriltags have been detected."%len(tags))

for tag in tags:
    cv2.circle(img, tuple(tag.corners[0].astype(int)), 4,(0,0,255), 2) # left-top
    cv2.circle(img, tuple(tag.corners[1].astype(int)), 4,(0,0,255), 2) # right-top
    cv2.circle(img, tuple(tag.corners[2].astype(int)), 4,(0,0,255), 2) # right-bottom
    cv2.circle(img, tuple(tag.corners[3].astype(int)), 4,(0,0,255), 2) # left-bottom
    print("family:",tag.tag_family)
    print("id:", tag.tag_id)
    print("conners:", tag.corners)
    print("homography:", tag.homography)
    

cv2.imshow("apriltag_test",img)
cv2.waitKey()

