import cv2


img = cv2.imread('Resources/lena.png')
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(11,11),0)
#kernel size, and it must be odd. here it is 7x7 and our sigma X = 0
#gaussian blur is used to smooth out the photo and remove the noise, but a perfect kernel has to be used.

imgCanny = cv2.Canny(img,100,100)  #to reduce the edges increase the 100 to more, like 150 and 200.
#there problem with edge detection is that the edges are disjoint and hence cant detect an object, hence we need to add dilation
#also to deal with kernels, which are just matrices, we need a library which deal with matrices, behold the almighty Numpy.

imgDialation = cv2.dilate(imgCanny,)
cv2.imshow('lena baby gray',imgGray)
cv2.imshow('lena baby gray and blur',imgBlur)
cv2.imshow('Edge Detection',imgCanny)
cv2.waitKey(0)