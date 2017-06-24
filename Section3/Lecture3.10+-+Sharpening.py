
# coding: utf-8

# In[3]:

import cv2
import numpy as np

input = cv2.imread('images/input.jpg')
cv2.imshow('Original', input)

# Create a sharpening kernel. We don't normalize it since the 
# values in the matrix sum to 1
kernel_sharpening = np.array([[-1, -1, -1],
                              [-1, 9,  -1],
                              [-1, -1, -1]])

# Applying different kernels to the input image
sharpened = cv2.filter2D(input, -1, kernel_sharpening)
cv2.imshow('Sharpened', sharpened)

cv2.waitKey(0)
cv2.destroyAllWindows()

