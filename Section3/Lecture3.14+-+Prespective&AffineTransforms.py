
# coding: utf-8

# ## Perspective Transform

# In[3]:

import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread('images/scan.jpg')
cv2.imshow('Original', image)
cv2.waitKey(0)

# Coordinates of the 4 corners of the original image
points_A = np.float32([[320, 15],
                       [700, 215],
                       [85,  610],
                       [530, 780]])

# Coordinates of the 4 corners of the desired output
# We use a ratio of an A4 paper 1 : 1.41
points_B = np.float32([[0, 0],
                       [420, 0],
                       [0, 594],
                       [420, 594]])

# Use the two sets of four points to compute
# the Perspective Transformation matrix, M
M = cv2.getPerspectiveTransform(points_A, points_B)
warped = cv2.warpPerspective(image, M, (420, 594))

cv2.imshow('WarpPerspective', warped)
cv2.waitKey(0)
cv2.destroyAllWindows()


# ## Affine Transforms
# ### Only require 3 coordinates

# In[5]:

import cv2
import numpy as np

image = cv2.imread('images/ex2.jpg')
rows, cols, ch = image.shape
cv2.imshow('Original', image)
cv2.waitKey(0)

# Coordinates of the 4 corners of the original image
points_A = np.float32([[320, 15],
                       [700, 215],
                       [85, 610]])

# Coordinates of the 4 corners of the desired output
# We use a ratio of an A4 paper 1 : 1.41
points_B = np.float32([[0, 0],
                       [420, 0],
                       [0, 594]])

# Use the two sets of points to compute the Affine Transformation Matrix
M = cv2.getAffineTransform(points_A, points_B)

warped = cv2.warpAffine(image, M, (cols, rows))

cv2.imshow('WarpAffine', warped)
cv2.waitKey(0)
cv2.destroyAllWindows()

