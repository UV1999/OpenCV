# -*- coding: utf-8 -*-
"""
Created on Fri May 17 13:01:14 2019

@author: uvansankar
"""

#drawing in opencv

'''

Goals :
    
Learn to draw different geometric shapes with OpenCV
You will learn these functions : cv2.line(), cv2.circle() ,
cv2.rectangle(), cv2.ellipse(), cv2.putText() etc.

'''

#drawing line

import numpy as np
import cv2

img = cv2.imread('obt.jpg', cv2.IMREAD_UNCHANGED)

cv2.line(img,(0,0),(200,300),(255,255,255),50)
cv2.rectangle(img,(500,250),(1000,500),(0,0,255),15)
cv2.circle(img,(447,63),63,(0,255,0),-1)
pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
cv2.polylines(img, [pts], True, (0,255,255), 3)


from matplotlib import pyplot as plt
plt.imshow(img, cmap = 'gray', interpolation = 'nearest')
plt.xticks([], plt.yticks([])) 
plt.show()




font = cv2.FONT_HERSHEY_SIMPLEX

cv2.putText(img,'OpenCV Tuts!',(10,500), font, 6, (200,255,155), 13, cv2.LINE_AA)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('C:/Users/uvansankar/Documents/Python Scripts/Mustang_draw.png',img)





 


















