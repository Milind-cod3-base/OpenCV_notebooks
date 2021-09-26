import cv2
import numpy as np

img = cv2.imread('Resources/lamb.png')
imgResize = cv2.resize(img,(800,450))

imgHSV = cv2.cvtColor(imgResize,cv2.COLOR_BGR2HSV) #cvt is used to change one format of colour to another.
#HSV is hue saturation value. Where saturation, if high will show the bright color, and if low will show a dull, grayed color.

cv2.imshow('lambo',imgResize)
cv2.imshow('lamboHSV',imgHSV)

cv2.waitKey(0)
