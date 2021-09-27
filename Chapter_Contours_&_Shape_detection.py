import cv2
import numpy as np

def getContours(img):    #defining a function
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)      #image and retrievel method, we are using external method. RETR_EXTERNAL retrieves the extreme outer contours #next we have approximations: where we can request either all info or we can get compressed value, hence reduced value. Here I am asking for all values.
    #contours will be saved in contours
    for cnt in contours:
        area = cv2.contourArea(cnt)    #gets the area of those contours
        print(area)

        #now I need to give minimum threshold area so that it doesnt detect any noise
        if area>500:
            cv2.drawContours(imgContour, cnt, -1, (255, 0, 0),3)  # it draws it out, but I wish to use it on copied image #first the image we need, then the contour, then index -1 because I need all the contours  #gave it blue color and gave the thickness as 3
            #as my shapes already had area > 500 it didnt create any issues.
            #now lets calculate the curve length
            peri = cv2.arcLength(cnt,True)   #True as contours is closed
            print(peri)
            #approximate the number of corner points
            approx = cv2.approxPolyDP(cnt,0.02*peri,True)   #a contour is given and then the resolution,
            print(len(approx))   #I just need the number of corner points and not the coordinates
            #create object corners
            objCor = len(approx)
            #create a bounding box around detected object
            x, y, w, h = cv2.boundingRect(approx)

            #now detect the type of shape

            if objCor ==3:objectType="Tri"
            elif objCor ==4:
                aspRatio = w/float(h)    #finding if its a square or rectangle
                if aspRatio >0.55 and aspRatio <1.5:objectType="Square"   #giving a deviation to fit in square
                else:objectType="Rectangle"
            elif objCor>4: objectType= "Circle"
            else:objectType="None"


            #drawing the rectangle around objects
            cv2.rectangle(imgContour,(x,y),(x+w,y+h),(0,255,0),2)

            cv2.putText(imgContour,objectType,(x+(w//2)-10, y+(h//2)-10),cv2.FONT_HERSHEY_COMPLEX, 0.8,(0,0,0),2)    #last is: where I wish to print

def stackImages(scale, imgArray):    #stacking function
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


img = cv2.imread('Resources/shapes.jpg')

#First the pre processing will be done by converting the image into grayscale and the corners will be found.

imgContour = img.copy()    #created a copy to be used inside the function.
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),1)   #kernel size set to 7,7 and blurring is done to smooth out the image, while the value of sigma is set 1.

imgCan = cv2.Canny(imgBlur,50,50)   #edges are marked.
getContours(imgCan)

imgblank = np.zeros_like(img)

imgStack = stackImages(0.5,([img,imgGray,imgBlur],[imgCan,imgContour,imgblank]))

cv2.imshow('Stacked Images', imgStack)
cv2.waitKey(0)