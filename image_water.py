#shape detection

import cv2
import numpy as np

img = cv2.imread("C:\\Users\\Arpita Singh\\PycharmProjects\\resource\\flower.jpg")

#resize
img = cv2.resize(img, None, None, fx=0.25, fy=0.25)
img_copy= img.copy()
#remove noice from the image
img = cv2.GaussianBlur(img,(9,9),0,None,0)

#use bilateral bluring for water image

img = cv2.bilateralFilter(img,3,5,10)
for i in range(2):
    img = cv2.bilateralFilter(img, 3, 10, 20)
for i in range(4):
    img = cv2.bilateralFilter(img, 3, 15, 30)

#sharping of image using addwaeighteed

gaussian = cv2.GaussianBlur(img,(3,3),0)
img = cv2.addWeighted(img,1.5,gaussian,-0.5,0)
for i in range(3):
    img = cv2.addWeighted(img, 2.5, gaussian, -1.5, 0)
img = cv2.bilateralFilter(img,3,5,10)
for i in range(2):
    img = cv2.bilateralFilter(img, 3, 10, 20)

# remove of noice for making image smooth 
gaussian = cv2.GaussianBlur(img, (3, 3), 0)
img = cv2.addWeighted(img, 1.5, gaussian, -0.5, 0)

#remove noice
img = cv2.medianBlur(img,3,None)
img = cv2.medianBlur(img,3,None)



cv2.imshow('original',img_copy)
cv2.imshow('water image ',img)
cv2.waitKey(0)