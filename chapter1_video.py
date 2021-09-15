import cv2

cap = cv2.VideoCapture("Resources/1 minute funny videos.mp4")

while True:
    success, img = cap.read()       #because a video is just strings of images played without delay
    cv2.imshow("Video",img)
    if  cv2.waitKey(24) & 0xFF == ord('q'):  #this whole line looks for q and then stops when finds the q.
        break


#ord('q') returns the Unicode code point of q
#cv2.waitkey(1) returns a 32-bit integer corresponding to the pressed key
#& 0xFF is a bit mask which sets the left 24 bits to zero, because ord() returns a value betwen 0 and 255, since your keyboard only has a limited character set
#Therefore, once the mask is applied, it is then possible to check if it is the corresponding key