
# coding: utf-8

# ## Sobel Edge Detection - 
# ### To emphasize vertical or horizontal edges

# In[2]:

import cv2
import numpy as np

image = cv2.imread('images/input.jpg',0)

# Extract Sobel edges
sobel_x = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize = 5)
sobel_y = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize = 5)

cv2.imshow('Original', image)
cv2.waitKey(0)
cv2.imshow('Sobel X', sobel_x)
cv2.waitKey(0)
cv2.imshow('Sobel Y', sobel_y)
cv2.waitKey(0)

sobel_OR = cv2.bitwise_or(sobel_x, sobel_y)
cv2.imshow('Sobel OR', sobel_OR)
cv2.waitKey(0)
cv2.destroyAllWindows()


# ## Laplacian

# In[3]:

import cv2
import numpy as np

image = cv2.imread('images/input.jpg', 0)
cv2.imshow('Original', image)
cv2.waitKey(0)

laplacian = cv2.Laplacian(image, cv2.CV_64F)
cv2.imshow('Laplacian', laplacian)
cv2.waitKey(0)

cv2.destroyAllWindows()


# ## Canny - Low error rate, we defined edges and accurate detection

# In[6]:

import cv2
import numpy as np

image = cv2.imread('images/input.jpg', 0)
cv2.imshow('Original', image)
cv2.waitKey(0)

## We need to provide two values: threshold1 and threshold2.
# Any gradient value larger than threshold2 is considered to be an edge.
# Any value below threshold1 is considered not to be an edge.
# Values between threshold1 and threshold2 are either classified as edges
# or non-edges based on how their intensities are "connected". 

canny = cv2.Canny(image, 20, 170)
cv2.imshow('Canny', canny)
cv2.waitKey(0)

cv2.destroyAllWindows()

