


#to detect faces we are going to use a method proposed by viola and jones
#positive = faces, negative = not faces --> then we will train and find a file which will have face
#many algorithms are more accurate than Haar cascades (HOG + Linear SVM, SSDs, Faster R-CNN, YOLO, to name a few), but they are still relevant and useful today.

#One of the primary benefits of Haar cascades is that they are just so fast — it’s hard to beat their speed.

#The downside to Haar cascades is that they tend to be prone to false-positive detections, require parameter tuning when being applied for inference/detection, and just, in general, are not as accurate as the more “modern” algorithms we have today.

#We will not be training a model but will use a pretrained model from openCV.

#opencv cascades.

import cv2
faceCascade = cv2.CascadeClassifier("Resources/haarcascade_frontalface_default.xml")
img =cv2.imread('Resources/lena.png')

imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#now time to detect the faces

faces = faceCascade.detectMultiScale(imgGray,1.1,4)  #scale is set 1.1 and minimum neighbours are 4

#next we need bouding boxes around the detected faces
#hence loop through detected faces and put boxes

for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

cv2.imshow('Result',img)

cv2.waitKey(0)

