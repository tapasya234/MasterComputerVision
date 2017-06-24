
# coding: utf-8

# In[1]:

import cv2
import numpy as np

image = cv2.imread('images/opencv_inv.png', 0)
cv2.imshow('Original', image)
cv2.waitKey(0)

# Let's define our kernel size
kernel = np.ones((5, 5), np.uint8)

# Erosion - Adds white pixels to the boundaries of an object
erosion = cv2.erode(image, kernel, iterations = 1)
cv2.imshow('Erosion', erosion)
cv2.waitKey(0)

# Dilation - Removes white pixels at the boudaries of an object
dilation = cv2.dilate(image, kernel, iterations = 1)
cv2.imshow('Dilation', dilation)
cv2.waitKey(0)

# Opening - Erosion followed by Dilation - Noise removal
opening = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)
cv2.imshow('Opening', opening)
cv2.waitKey(0)

# CLosing - Dilation followed by Erosion - 
# Closing small black points on the foreground object.  
closing = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
cv2.imshow('CLOSING', closing)
cv2.waitKey(0)

cv2.destroyAllWindows()

