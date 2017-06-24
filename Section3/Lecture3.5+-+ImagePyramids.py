
# coding: utf-8

# Pyramiding Image refers to either upscaling or downscaling by 2
# 
# It is useful when makingobject detection that scales an image each time it looks for an object.

# In[1]:

import cv2
import numpy as np

image = cv2.imread('images/input.jpg')

smaller = cv2.pyrDown(image)
larger = cv2.pyrUp(smaller)

cv2.imshow('Original', image)
cv2.imshow('Smaller', smaller)
cv2.imshow('Larger', larger)
cv2.waitKey(0)
cv2.destroyAllWindows()

