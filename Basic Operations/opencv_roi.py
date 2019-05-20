# -*- coding: utf-8 -*-
"""
Created on Mon May 20 10:31:41 2019

@author: uvansankar
"""

#image roi

'''

Sometimes, you will have to play with certain region of images. For eye 
detection in images, first perform face detection over the image until 
the face is found, then search within the face region for eyes. This 
approach improves accuracy (because eyes are always on faces :D ) and 
performance (because we search for a small area).

ROI is again obtained using Numpy indexing. Here I am selecting the ball
and copying it to another region in the image.

'''

import cv2
import numpy as np

img = cv2.imread('obt.jpg')

headlight = img[380:440, 330:390]

img[273:333, 100:160] = headlight

cv2.namedWindow('ROI')
cv2.imshow('ROI',img)
cv2.waitKey(0) & 0xFF
cv2.destroyAllWindows()

from matplotlib import pyplot as plt
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([], plt.yticks([]))  #to hide tick values on x and y axis
plt.show()

#splitting and merging image channels

b, g, r = cv2.split(img)
img = cv2.merge((r,g,b))

from matplotlib import pyplot as plt
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([], plt.yticks([]))  #to hide tick values on x and y axis
plt.show()

































