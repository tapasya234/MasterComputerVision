
# coding: utf-8

# In[1]:

import cv2
import numpy as np

image = cv2.imread('images/elephant.jpg')
cv2.imshow('Original Image', image)
cv2.waitKey(0)

# Creating our 3 x 3 kernel
kernel_3x3 = np.ones((3, 3), np.float32) / 9

# We use the cv2.filter2D to convolve the kernal with an image
blurred = cv2.filter2D(image, -1, kernel_3x3)
cv2.imshow('3x3 Kernal Blurring', blurred)
cv2.waitKey(0)

# Creating our 7x7 kernal
kernel_7x7 = np.ones((7, 7), np.float32) / 49

blurred2 = cv2.filter2D(image, -1, kernel_7x7)
cv2.imshow('7x7 Kernal Blurring', blurred2)
cv2.waitKey(0)

cv2.destroyAllWindows()


# # Other commonly used blurringmethods in OpenCV

# In[2]:

import cv2
import numpy as np

image - cv2.imread('images/elephant.jpg')

# Averaging done by convolving the image with a normalized box filter.
# This takes the pixels under the box and replaces the central element
# Box size needs to be odd and positive
blur = cv2.blur(image, (3,3))
cv2.imshow('Averaging', blur)
cv2.waitKey(0)

# Gaussian Kernal
gaussian = cv2.GaussianBlur(image, (7,7), 0)
cv2.imshow('Gaussian Blurring', gaussian)
cv2.waitKey(0)

# Takes median value of all pixels under the kernal area and
# central element is replaces with this median value
median = cv2.medianBlur(image, 5)
cv2.imshow('Median Blurring', median)
cv2.waitKey(0)

# Bilateral is very effective in noise removal
# while keeping the edges intact
bilateral = cv2.bilateralFilter(image, 9, 75, 75)
cv2.imshow('Bilateral Filtering', bilateral)
cv2.waitKey(0)

cv2.destroyAllWindows()


# ## Image De-noising - Non-Local Means Denoising

# ### 4 variations:
# cv2.fastNIMeansDenoising()- works with a single grayscale images
# 
# cv2.fastNIMeansDenoisingColored() - works with color image
# 
# cv2.fastNIMeansDenoisingMulti() - works with image sequence captured in a short period of time (grayscale images)
# 
# cv2.fastNIMeansDenoisingColoredMulti() - same as above, but for color image

# In[ ]:

import cv2

