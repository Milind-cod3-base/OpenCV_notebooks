import cv2

cap = cv2.VideoCapture(0+cv2.CAP_DSHOW)  #this cv2,CAP_DSHOW was added thanks to stackoverflow. And works instantly.

#this extra cv2 is there because the camera wont open while using third party apps.
cap.set(3,640)  #set is for settings, where 3 is for frame width
cap.set(4,480)  #4 is for frame height
cap.set(10, 200)  #10 is for brightness
while True:
    success, img = cap.read()       #because a video is just strings of images played without delay
    cv2.imshow("Video",img)
    if  cv2.waitKey(24) & 0xFF == ord('q'):  #this whole line looks for q and then stops when finds the q.
        break