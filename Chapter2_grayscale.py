import cv2
import numpy as np

img = cv2.imread('Resources/lena.png')
kernel = np.ones((5,5), np.uint8)  #np uint8, means it can take upto 256 values ranging from 0 to 255
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(11,11),0)
#kernel size, and it must be odd. here it is 7x7 and our sigma X = 0
#gaussian blur is used to smooth out the photo and remove the noise, but a perfect kernel has to be used.

imgCanny = cv2.Canny(img,100,100)  #to reduce the edges increase the 100 to more, like 150 and 200.
#there problem with edge detection is that the edges are disjoint and hence cant detect an object, hence we need to add dilation
#also to deal with kernels, which are just matrices, we need a library which deal with matrices, behold the almighty Numpy.

imgDialation = cv2.dilate(imgCanny, kernel,iterations=1)
#after the kernel I need to define how many iterations the kernel need to move around
#more number of iterations will result in increase of the widthe of edges, which means the dilation has been iterated many times.

imgEroded = cv2.erode(imgDialation,kernel,iterations=1)
#this is opposite of dilation, makes the edges thinner
#here, lets thin the already dilated images.

cv2.imshow('lena baby gray',imgGray)
cv2.imshow('lena baby gray and blur',imgBlur)
cv2.imshow('Edge Detection',imgCanny)
cv2.imshow('Dialation Image', imgDialation)    #broadens the edges and hence dilated.
cv2.imshow('Eroded Image', imgEroded)
cv2.waitKey(0)