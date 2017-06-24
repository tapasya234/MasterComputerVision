
# coding: utf-8

# cv2.getRotationMatrix2D(rotation_center_x, rotation_center_y, angle_of_rotation, scale)

# In[1]:

import cv2
import numpy as np

image = cv2.imread('images/input.jpg')
height, width = image.shape[:2]

# Divide by two to rotate the image around its centre
rotation_matrix = cv2.getRotationMatrix2D((width/2, height/2), 90, 1)
rotated_image = cv2.warpAffine(image, rotation_matrix, (width, height))

cv2.imshow('Rotated Image', rotated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[2]:

# A simpler method to rotate the image by 90 degrees anti-clockwise
img = cv2.imread('images/input.jpg')

rotated_image = cv2.transpose(img)

cv2.imshow('Transposed Image', rotated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

