
# coding: utf-8

# # Thresholding and Binarization
# ### Image should be in grayscale before it can be converted to binary form
# ### cv2.threshold(image, Threshold Value, Max Value, Threshold Type)
# ### Threshold Types:
# #### cv2.THRESH_BINARY - Most common
# #### cv2.THRESH_BINARY_INV - Most common
# #### cv2.THRESH_TRUNC
# #### cv2.THRESH_TOZERO
# #### cv2.THRESH_TOZERO_INV

# In[3]:

import cv2
import numpy as np

# Load image as grayscale
image = cv2.imread('images/gradient.jpg', 0)
cv2.imshow('Original', image)

# BINARY - Values below 127 goes to 0 and everything above 127 go to 255
ret, thresh1 = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
cv2.imshow('Threshold Binary', thresh1)

# INV BINARY - 0 - 127 -> 255 and 127 - 255 -> 0
ret, thresh2 = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY_INV)
cv2.imshow('Threshold Binary Inverse', thresh2)

# TRUNCATED - Values above 127 are truncated at 127
ret, thresh3 = cv2.threshold(image, 127, 255, cv2.THRESH_TRUNC)
cv2.imshow('Threshold Truncated', thresh3)

# TOZERO - Values below 127 go to 0, above 127 are unchanged
ret, thresh4 = cv2.threshold(image, 127, 255, cv2.THRESH_TOZERO)
cv2.imshow('Threshold ToZero', thresh4)

# TOZERO_INV - Values above 127 go to 255, below 127 are unchanged
ret, thresh5 = cv2.threshold(image, 127, 255, cv2.THRESH_TOZERO_INV)
cv2.imshow('Threshold ToZero INV', thresh5)

cv2.waitKey(0)
cv2.destroyAllWindows()


# ## Adaptive Thresholding

# In[4]:

import cv2
import numpy as  np

image = cv2.imread('images/Origin_of_Species.jpg', 0)
cv2.imshow('Original', image)
cv2.waitKey(0)

# BINARY
ret, thresh1 = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
cv2.imshow('Binary Thresholding', thresh1)
cv2.waitKey(0)

# It is a good practice to blur images as it removes noise.
image = cv2.GaussianBlur(image, (3, 3), 0)

# Using Adaptive Threshold
thresh2 = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                               cv2.THRESH_BINARY, 3, 5)
cv2.imshow('Adaptive Mean Thresholding', thresh2)
cv2.waitKey(0)

# Otsu's Thresholding
_, thresh3 = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
cv2.imshow("Otsu's Threshold", thresh3)
cv2.waitKey(0)

# Otsu's thresholding after Gaussian filtering
#blur = cv2.GaussianBlur(image, (5, 5), 0)
_, thresh4 = cv2.threshold(image, 0, 255, cv2.THRESH_OTSU + cv2.THRESH_BINARY)
cv2.imshow("Gaussian Otsu's Threshold", thresh4)
cv2.waitKey(0)
cv2.destroyAllWindows()


# #### cv2.adaptiveThreshold(image, Max Value, Adaptive type,  Threshold Type, Block Size, Constant that is subtracted from the mean)
# 
# #### Adaptive Threshold Types:
# ##### ADAPTIVE_THRESH_MEAN_C
# ##### ADAPTIVE_THRESH_GAUSSIAN_C
# ##### THRESH_OTSU -> Used cv2.threshold
