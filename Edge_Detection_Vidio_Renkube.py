import cv2 #for image processing
import numpy as np #manupulating the array
from numpy.core.numeric import count_nonzero #data  manupulating

# Author => Naveenprabaharan S - GCT [1918L12]

cap = cv2.VideoCapture('vid.mp4') # Web camera start 


while True:
    ret, frame = cap.read() # read video
    # frame = cv2.imread('img-10cop.jpg')
        
    
    # converting BGR to gray   
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
    

    # define range of red color in HSV   
    blur =  cv2.GaussianBlur(gray,(3,3),0)
    

    # 20,100
    canny_output = cv2.Canny(blur, 30, 90)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(3,3))  
    closed = cv2.morphologyEx(canny_output,cv2.MORPH_OPEN,kernel)
    closed = cv2.morphologyEx(closed,cv2.MORPH_CLOSE,kernel)  
    closed = cv2.morphologyEx(closed,cv2.MORPH_OPEN,kernel)
    
   
    # show image
    cv2.imshow('Original Frame', frame)
    cv2.imshow("30,90", canny_output)
    cv2.imshow("blur",blur)
    cv2.imshow("gray", gray)
    
    # break the showing window
    if cv2.waitKey(1) == 13:
        break

# destroy the window
cv2.destroyAllWindows()
cap.release()
