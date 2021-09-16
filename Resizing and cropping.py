#in open cv, x is towards right positive while for y its downwards positive
#frame's origin is taken at the left topmost corner.

import cv2
import numpy as np   #because image is just an array/matrix of pixels and for cropping, we can eliminate few elements

ad = cv2.imread('Resources/audi.png')
print(ad.shape)   #prints in height, width and channels(BGR) format

adResize = cv2.resize(ad,(700,400))   #here width, height format comes.
print(adResize.shape)

adCropped = ad[0:300, 500:910]
cv2.imshow('audi',ad)
#cv2.imshow('audi resized',adResize)       #this print is made silent, getting output for crop only.
cv2.imshow('audi cropped',adCropped)
cv2.waitKey(0)