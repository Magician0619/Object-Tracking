import cv2
import numpy as np

img = cv2.imread("114.jpg")

lower_race = np.array([25, 75, 165])
upper_race = np.array([40, 255, 255])


race_mask = cv2.inRange(img, lower_race, upper_race)

cv2.imshow("debug",race_mask)
cv2.waitKey(0)