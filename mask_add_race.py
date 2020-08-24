import cv2
import numpy as np

img = cv2.imread("img/race2.jpg")
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lower_race1 = np.array([25, 75, 165])
upper_race1 = np.array([80, 255, 255])

lower_race2 = np.array([20, 75, 100])
upper_race2 = np.array([40, 255, 255])

# lower_race2 = np.array([35, 106, 39])
# upper_race2 = np.array([78, 255, 204])


race_mask1 = cv2.inRange(hsv, lower_race1, upper_race1)
race_mask2 = cv2.inRange(hsv, lower_race2, upper_race2)

race_mask = race_mask1 + race_mask2

cv2.imshow("input",img)
cv2.imshow("HSV",hsv)
cv2.imshow("debug1",race_mask1)
cv2.imshow("debug2",race_mask2)
cv2.imshow("output",race_mask)
cv2.waitKey(0)
