import cv2
import numpy as np
#now we need to define a color range (hsv range) so that if a color falls in image falls in that range, we can capture it.
#but we donot know the minimum and maximum value we need for that particular color.
#Hence we will introduce trackbars which will help us to play around values in real time so that we can find optimum maximum and minimum value of that color.

def empty(a):
    pass      #this will pretty much do nothing

cv2.namedWindow("TrackBars")  #to introduce track bar, we create a new window
cv2.resizeWindow("TrackBars",640,240)
cv2.createTrackbar("Hue Min","TrackBars",0,179,empty)       #keep track of hue minimum in the trackbar menu. and initial value

#hue has maximum value of 360 but here we only have till 179 (180 values)
#empty function is defined which will run everytime anything changes in trackbar.


img = cv2.imread('Resources/lamb.png')
imgResize = cv2.resize(img,(800,450))

imgHSV = cv2.cvtColor(imgResize,cv2.COLOR_BGR2HSV) #cvt is used to change one format of colour to another.

#HSV is hue saturation value. Where saturation, if high will show the bright color, and if low will show a dull, grayed color.

cv2.imshow('lambo',imgResize)
cv2.imshow('lamboHSV',imgHSV)

cv2.waitKey(0)
