# -*- coding: utf-8 -*-
"""
Created on Mon May 20 10:02:18 2019

@author: uvansankar
"""

#basic operations on images

'''

Goal :
    Learn to:
        1. Access pixel values and modify them
        2. Access image properties
        3. Setting Region of Image (ROI)
        4. Splitting and Merging images
        
Almost all the operations in this section is mainly related to Numpy
rather than OpenCV. A good knowledge of Numpy is required to write 
better optimized code with OpenCV.

'''

#accessing and modifying values

#loading a color image
import cv2
import numpy as np
img = cv2.imread('obt.jpg')
#print(img)

'''

You can access a pixel value by its row and column coordinates. 
For BGR image, it returns an array of Blue, Green, Red values. For 
grayscale image, just corresponding intensity is returned.

'''

px = img[100,100]
print(px)

#accessing only blue pixel
blue = img[100,100,0]
print(blue)

'''

Why 0 in the array of img ? :
    An image in OpenCV is represented as a 3D numpy array. The 
first two axes (X and Y) represent the pixel matrix. The third axis 
(Z) contains the color channels (B,G,R). What you are doing in this 
line, is selecting a pixel by x, y and z coordinates. The third index
(the 0) in img[100,100,0] is the 0'th element in the array of the 
pixel's color values [B,G,R], thus your blue color channel. I hope 
this helps.

'''

#modifying the pixel values
img[100,100] = [255, 255, 255]
print(img[100,100])
green = img[100,100,1]
print(green)

#better pixel accesing and editing with numpy

#accessing red values
print(img.item(10,10,2))

#modifying RED values
img.itemset((10,10,2),100)
print(img.item(10,10,2))

#total number of pixels 
print(img.size)

#image datatype
print(img.dtype)

'''

img.dtype is very important while debugging because a large number of
errors in OpenCV-Python code is caused by invalid datatype.

'''





































































