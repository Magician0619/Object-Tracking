import cv2
import numpy as np

# mask = np.zeros((240,320,3), np.uint8)
img = cv2.imread("175.jpg")
mask = np.zeros([240,320],dtype=np.uint8)

mask[0:120,0:320] = 255
# cv2.imshow("Debug",mask)

image = cv2.add(img, np.zeros(np.shape(img), dtype=np.uint8), mask=mask)



 
cv2.imshow('res',image)


cv2.waitKey(0)
