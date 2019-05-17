# -*- coding: utf-8 -*-
"""
Created on Fri May 17 10:16:31 2019

@author: uvansankar
"""

#capture video from camera - cv2.VideoCapture()

''''
To capture a video, you need to create a VideoCapture
object. 
Argument is either the name of a video file or the
device index.
Normally one camera will be connecte i.e., webcam
in a laptop. It is represented by number 0 or -1. 
For second camera, number 1 can be used.
Then, the video is captured frame-by-frame. 
The capture should be realeased at the end.

'''
#import numpy as np
import cv2

cap = cv2.VideoCapture(0)
cap.set(3,720)
cap.set(4,480)
#cap.set(16,True)


while(True):
    #capture frame-by-frame
    ret, frame = cap.read()
    print(frame)
    print(ret)
    
    #operations on the frame
    #gray = cv2.cvtColor(frame, cv2.COLOR)
    
    #display the resulting frame
    cv2.imshow('frame', frame)
    if cv2.waitKey(2) & 0xFF == ord('q'):
        break

#release the capture
cap.release()
cv2.destroyAllWindows()

'''
cap.read() returns a bool (True/False). If frame is 
read correctly, it will be True. So you can check 
end of the video by checking this return value.

'''








