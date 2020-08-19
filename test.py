import cv2
import numpy as np
# np.squeeze
resize_size = 128

img = cv2.imread("00.jpg")
img = cv2.resize(img,(resize_size, resize_size))
img = np.transpose(img,[2,0,1])
img = img[np.newaxis, :]

# img6 = img1[np.newaxis, :]

# img2 = np.expand_dims(img1,0)

# img3 = np.squeeze(img2)

# img4 = np.transpose(img1,[2,1,0])

# img5 = img1[:,:,1]

print(img.shape)
# print(img2.shape)
# print(img3.shape)
# print(img4.shape)
# print(img6.shape)
# print("1:",img1)
# print("6",img6)

# cv2.imshow("test",img5)
# cv2.waitKey(0)
