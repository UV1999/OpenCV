# -*- coding: utf-8 -*-
"""
Created on Fri May 17 11:12:25 2019

@author: uvansankar
"""

#playing video from file

'''
Similar to cpaturing from camera, here the video file
name is given instead of the camera index.
While displaying the frame, use the appropriate time for
cv2.waitKey(). 
If it is too less, video will be very fast and if too high, 
video will be slow.  (This is how slow motion video plays)

'''

#qimport numpy as np
import cv2

cap = cv2.VideoCapture('opvid.mp4')
#cap.set(3, 640)
#cap.set(4, 480)



while(cap.isOpened()):
    ret, frame = cap.read()
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame',gray)
    
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()