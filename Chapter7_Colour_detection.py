import cv2
import numpy as np

#now we need to define a color range (hsv range) so that if a color falls in image falls in that range, we can capture it.
#but we donot know the minimum and maximum value we need for that particular color.
#Hence we will introduce trackbars which will help us to play around values in real time so that we can find optimum maximum and minimum value of that color.

def empty(a):
    pass                 #this will pretty much do nothing

def stackImages(scale, imgArray):              #stacking function
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range(0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape[:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]),
                                                None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y] = cv2.cvtColor(imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank] * rows
        hor_con = [imageBlank] * rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None, scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor = np.hstack(imgArray)
        ver = hor
    return ver



cv2.namedWindow("TrackBars")  #to introduce track bar, we create a new window
cv2.resizeWindow("TrackBars",640,240)
cv2.createTrackbar("Hue Min","TrackBars",0,179,empty)       #keep track of hue minimum in the trackbar menu. and initial value

#hue has maximum value of 360 but here we only have till 179 (180 values)
#empty function is defined which will run everytime anything changes in trackbar.

cv2.createTrackbar("Hue Max","TrackBars",43,179,empty)  #for maximum, set both value to max in all, here 179
cv2.createTrackbar("Sat Min","TrackBars",65,255,empty)
cv2.createTrackbar("Sat Max","TrackBars",255,255,empty)   #sat and value goes upto 255 but hue here, goes till 179
cv2.createTrackbar("Val Min","TrackBars",150,255,empty)
cv2.createTrackbar("Val Max","TrackBars",255,255,empty)     #values are tweaked to perfection by toggling the parameters in trackbars

while True:
    #I need to run this in a loop to get it as a video
    img = cv2.imread('Resources/yes.jpg')
    imgResize = cv2.resize(img,(800,450))
    imgHSV = cv2.cvtColor(imgResize,cv2.COLOR_BGR2HSV) #cvt is used to change one format of colour to another.

#HSV is hue saturation value. Where saturation, if high will show the bright color, and if low will show a dull, grayed color.

#now we are goint to read these trackbar values so that we can apply on our image, hence we gettrackbar function to get the values

    h_min = cv2.getTrackbarPos("Hue Min", "TrackBars")    #first is which value we are talking about. then to which trackbar window doest it belong
    h_max = cv2.getTrackbarPos("Hue Max", "TrackBars")
    s_min = cv2.getTrackbarPos("Sat Min", "TrackBars")
    s_max = cv2.getTrackbarPos("Sat Max", "TrackBars")
    v_min = cv2.getTrackbarPos("Val Min", "TrackBars")
    v_max = cv2.getTrackbarPos("Val Max", "TrackBars")

    print( h_min, h_max,s_min,s_max,v_min,v_max)

    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])
    mask = cv2.inRange(imgHSV,lower,upper) #this will filter out and will give us the filtered out image of that color
    #after toggling with the mask - values of the range has been optimised.

    imgResult = cv2.bitwise_and(imgResize,imgResize,mask=mask)     #bitwise_add takes two images and whatever the color common in them it says yes and stores that color into a new image
   #our new image will be like original image but with a mask applied.
    #here will recieve a coloured mask.

    #cv2.imshow('lambo',imgResize)
    #cv2.imshow('lamboHSV',imgHSV)
    #cv2.imshow('Mask',mask)
    #cv2.imshow('Result',imgResult)

    imgStack = stackImages(0.6,([img,imgHSV],[mask,imgResult]))
    cv2.imshow('Stacked Images',imgStack)    #printing only stacked images

    cv2.waitKey(1)
