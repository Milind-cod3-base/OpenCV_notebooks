#this is the warp perspective tutorial of Opencv

#if we wish to know certain position of a pixel in an image, open it in paint and drag the cursor around.

import cv2
import numpy as np

img = cv2.imread("Resources/cards.jpg")
width,height = 250,350  #keeping the aspect ratio same

pts1 = np.float32([[109,220],[289,187],[153,482],[350,441]])
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])

matrix = cv2.getPerspectiveTransform(pts1,pts2)   #(src,dst) src is the points in source file and dst are the points in destination points
imgOutput = cv2.warpPerspective(img,matrix,(width,height))

cv2.imshow("image",img)
cv2.imshow("warped",imgOutput)
cv2.waitKey(0)