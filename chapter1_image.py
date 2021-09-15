import cv2

print('Pack imported')  #this to check if the package has been downloaded or not

#Chapter 1
#read images, videos and webcams

img = cv2.imread('Resources/lena.png')

cv2.imshow("Output",img)
cv2.waitKey(0)#0 is infinite or and 1000 = 1 seconds as it is in miliseconds.
