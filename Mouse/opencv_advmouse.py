# -*- coding: utf-8 -*-
"""
Created on Sat May 18 12:43:39 2019

@author: uvansankar
"""

#advanced mouse operations

'''

Now we go for much more better application. In this, we draw 
either rectangles or circles (depending on the mode we select)
by dragging the mouse like we do in Paint application. So our 
mouse callback function has two parts, one to draw rectangle 
and other to draw the circles. This specific example will be 
really helpful in creating and understanding some interactive 
applications like object tracking, image segmentation etc.

'''

import cv2
import numpy as np

drawing = False    #true if mouse is pressed
mode = True    #if True, draw rectangle. Press 'm' to toggle
               #to curve
ix, iy = -1,-1

#mouse callback function
def draw_circle(event,x,y,flags,param):
    global ix,iy,drawing,mode
    
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            if mode == True:
                cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
            else:
                cv2.circle(img,(x,y),5,(0,0,255),-1)
                
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        if mode == True:
            cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
        else:
            cv2.circle(img,(x,y),100,(0,0,255),-1)
 
'''

Next we have to bind this mouse callback function to OpenCV 
window. In the main loop, we should set a keyboard binding 
for key ‘m’ to toggle between rectangle and circle.

'''
           

img = np.zeros((512,512,3), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)

while(1):
    cv2.imshow('image',img)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('m'):
        mode = not mode
    elif k == 27:
        break;
        
cv2.destroyAllWindows()
           
                
                
                
                
                
                
                
                
                
                
                