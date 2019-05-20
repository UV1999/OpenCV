# -*- coding: utf-8 -*-
"""
Created on Sat May 18 11:57:13 2019

@author: uvansankar
"""

#mouse as a paint-brush

'''
Goal :
     1. Learn to handle mouse events in OpenCV
     2. You will learn these functions : cv2.setMouseCallback()

Here, we create a simple application which draws a circle on 
an image wherever we double-click on it.

First we create a mouse callback function which is executed 
when a mouse event take place. Mouse event can be anything 
related to mouse like left-button down, left-button up, 
left-button double-click etc. It gives us the coordinates 
(x,y) for every mouse event. With this event and location, 
we can do whatever we like. 

Creating mouse callback function has a specific format which 
is same everywhere. It differs only in what the function does. 
So our mouse callback function does one thing, it draws a 
circle where we double-click.

'''

import cv2
import numpy as np

#mouse callback function
def draw_circle(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img,(x,y),100,(255,0,0),-1)
        
#create a black image, a window and bind the function to window
img = np.zeros((512,512,3), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)

while(1):
    cv2.imshow('image',img)
    if cv2.waitKey(20) & 0xFF == 27:
        break
    
cv2.destroyAllWindows()




