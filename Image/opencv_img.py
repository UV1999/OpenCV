# -*- coding: utf-8 -*-
"""
Created on Wed May 15 14:02:55 2019

@author: uvansankar
"""

#read an image - imread()

''' 
Image is read using the imread() function. 
It has two arguments. The first one is the name of the file. 
The second argumnet is a flag which specifies how the image should
be read.
The flags are :
    1. cv2.IMREAD_COLOR : Loads a color image. Transparency is 
                          neglected and is the default flag.
    2. cv2.IMREAD_GRAYSCALE : Loads image in grayscale mode.
    3. cv2.IMREAD_UNCHANGED : Loads image as such including 
                              alpha channel.
'''

import cv2
import numpy as np

#loading an image in grayscale
img = cv2.imread('C:/Users/uvansankar/Documents/Python Scripts/obt.jpg',0)
img_array = np.array(img)
print(img_array)  #printing the array

#display an image - imshow()

'''
Image is displayed using the imshow() function.
The window automatically fits to the image size.
First argument is the name of the window which is a string.
The second argument is the name is the name of the image.
'''

cv2.namedWindow('Mustang_Gray',cv2.WINDOW_NORMAL)
cv2.imshow('Mustang_Gray',img)
cv2.waitKey(0) & 0xFF
cv2.destroyAllWindows()

'''
cv2.waitKey() is a keyboard binding function. Its argument is 
the time in milliseconds. The function waits for specified 
milliseconds for any keyboard event. If you press any key in 
that time, the program continues. If 0 is passed, it waits 
indefinitely for a key stroke. It can also be set to detect 
specific key strokes like, if key a is pressed etc which we 
will discuss below.

cv2.destroyAllWindows() simply destroys all the windows we 
created. If you want to destroy any specific window, use the 
function cv2.destroyWindow() where you pass the exact window 
name as the argument.

There is a special case where you can already create a 
window and load image to it later. In that case, you can 
specify whether window is resizable or not. It is done with 
the function cv2.namedWindow(). By default, the flag is 
cv2.WINDOW_AUTOSIZE. But if you specify flag to be 
cv2.WINDOW_NORMAL, you can resize window. It will be helpful
when image is too large in dimension and adding track bar to
windows.

'''

#write an image - imwrite()

cv2.imwrite('C:/Users/uvansankar/Documents/Python Scripts/Mustang_Gray.png',img)

#Using Matplotlib

from matplotlib import pyplot as plt
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([], plt.yticks([]))  #to hide tick values on x and y axis
plt.show()



































