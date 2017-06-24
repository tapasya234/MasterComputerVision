
# coding: utf-8

# In[3]:

import cv2
import numpy as np

image = cv2.imread('images/input.jpg')
height, width = image.shape[:2]

# Let's get the starting pixel coordinates (top left of the cropping rectangle)
start_row, start_col = int(height * 0.25), int(width * 0.25)

# Let's get the ending pixel coordinates (bottom right)
end_row, end_col = int(height * 0.75), int(width * 0.75)

# Simply use indexing to crop out the rectangle we desire
cropped = image[start_row:end_row, start_col:end_col]

cv2.imshow('Original image', image)
cv2.waitKey(0)
cv2.imshow('Cropped Image', cropped)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[ ]:



