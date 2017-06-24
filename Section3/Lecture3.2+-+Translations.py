
# coding: utf-8

# In[1]:

import cv2
import numpy as np

image = cv2.imread('images/input.jpg')

# Store height and width of th image
height, width = image.shape[:2]

quarter_height, quarter_width = height/4, width/4

#     | 1 0 Tx |
# T = | 0 1 Ty |

# T is our transaltion matrix
T = np.float32([[1, 0, quarter_width], [0, 1, quarter_height]])

# We use warpAffine to transform the image using the matrix
image_transaltion = cv2.warpAffine(image, T, (width, height))
cv2.imshow('Translation', image_transaltion)

cv2.waitKey(0)
cv2.destroyAllWindows()


# In[2]:

# Lets take a look at T

print T

