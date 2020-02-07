import cv2

from matplotlib import pyplot as plt

import numpy as np
img1 = cv2.imread('/home/weng/Documents/paper4.jpg')
img2 = cv2.imread('/home/weng/Documents/paper4.jpg')

img2 = img2[1:300, 1:300]

img3 = img1
img_out = '/home/weng/Documents/paper1_2.jpg'
gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
sift = cv2.xfeatures2d.SIFT_create()
# kp = sift.detect(gray, None)
kp1, des1 = sift.detectAndCompute(gray1,None)
kp2, des2 = sift.detectAndCompute(gray2,None)
# cv2.drawKeypoints(gray, kp, img)
# cv2.imwrite(img_out, img)


# BFMatcher with default params
bf = cv2.BFMatcher()
matches = bf.knnMatch(des1,des2, k=2)

# Apply ratio test
good = []
for m,n in matches:
    if m.distance < 0.75*n.distance:
        good.append([m])

# cv2.drawMatchesKnn expects list of lists as matches.
img3 = cv2.drawMatchesKnn(img1,kp1,img2,kp2,good,img3, flags=2)


plt.imshow(img3)
plt.show()