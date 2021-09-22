import cv2
import numpy as np

#img = np.zeros((512,512))   #numpy creates a matrix of zeros of size 512,512, where 0 is a black pixel in image.

#above one is just a gray scale image, lets add colour to it.
img = np.zeros((512,512,3),np.uint8)   #3 is assigned for rgb and np.uint8 holds all numbers from 0 to 255
img[:] = 255,0,0    #this prints blue BGR  #all pixels are selected and coloured blue

print(img.shape)
img[200:300,400:500] = 0,255,0

#adding a line in cv2

cv2.line(img,(0,0),(img.shape[0],img.shape[1]),(0,255,0),3)   #here the width comes first and then the height. Hence imagshape[0]

cv2.rectangle(img,(0,0),(250,350),(0,0,255),cv2.FILLED)  #to fill the colour, put border value as -1. or with cv2.FILLED.

cv2.circle(img,(400,50),30,(255,255,0),-1)  #circle created, with centre defined and radius length is given along with color.

cv2.putText(img,"OPEN CV LEARNING",(150,180), cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)   #here we add the text, then origin, thn font, thn scale, then color and later thickness.
cv2.imshow("image",img)
cv2.waitKey(0)