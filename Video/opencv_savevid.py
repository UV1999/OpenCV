# -*- coding: utf-8 -*-
"""
Created on Fri May 17 12:03:07 2019

@author: uvansankar
"""

#saving a video - cv2.VideoWriter_fourcc()

'''

After capturing a video and processing it frame-by-frame, we 
need to save that video.
Done using cv2.imwrite() function
This time we create a VideoWriter object. We should specify the 
output file name (eg: output.avi). Then we should specify the 
FourCC code. Then number of frames 
per second (fps) and frame size should be passed. And last one 
is isColor flag. If it is True, encoder expect color frame, 
otherwise it works with grayscale frame.

FourCC is a 4-byte code used to specify the video codec. The list
of available codes can be found in fourcc.org. It is platform 
dependent. Following codecs works fine for me.

FourCC code is passed as cv2.VideoWriter_fourcc('M','J','P','G') 
or cv2.VideoWriter_fourcc(*'MJPG) for MJPG.

'''

#import numpy as np
import cv2

cap = cv2.VideoCapture(0)

#define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'MPEG')
out = cv2.VideoWriter('output.mp4', fourcc, 60.0, (640,480))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        frame = cv2.flip(frame,1)
        
        #write the flipped frame
        out.write(frame)
        
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
    else :
        break
    
#release everything
cap.release()
out.release()
cv2.destroyAllWindows()


















