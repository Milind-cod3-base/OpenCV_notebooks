#in open cv, x is towards right positive while for y its downwards positive
#frame's origin is taken at the left topmost corner.

import cv2
import numpy as np

ad = cv2.imread('Resources/audi.png')
print(ad.shape)   #prints in height, width and channels(BGR) format

adResize = cv2.resize(ad,(700,400))   #here width, height format comes.
print(adResize.shape)

cv2.imshow('audi',ad)
cv2.imshow('audi resized',adResize)
cv2.waitKey(0)