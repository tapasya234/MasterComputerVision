
# coding: utf-8

# cv2.resize(image, dsize(output image size), x_scale, y_scale, interpolation)

# In[1]:

import cv2
import numpy as np

image = cv2.imread('images/input.jpg')

# Let's make our image 3/4 of it's original size
image_scaled = cv2.resize(image, None, fx = 0.75, fy = 0.75)
cv2.imshow('Scaling - Linear Interpolation', image_scaled)
cv2.waitKey(0)

# Let's double the size of our image
image_scaled = cv2.resize(image, None, fx = 2, fy = 2, interpolation = cv2.INTER_CUBIC)
cv2.imshow('Scaling - Cubic Interpolation', image_scaled)
cv2.waitKey(0)

# Let's skew the resizing by setting exact dimensions
image_scaled = cv2.resize(image, (900, 400), interpolation = cv2.INTER_AREA)
cv2.imshow('Scaling - Skewed Image', image_scaled)
cv2.waitKey(0)

cv2.destroyAllWindows()


# ## Interpolation types
# cv2.INTER_AREA - Good for shrinking or down scaling
# 
# cv2.INTER_NEAREST - Fastest
# 
# cv2.INTER_LINEAR - Good for zooming or up scaling (default)
# 
# cv2.INTER_CUBIC - Better
# 
# cv2.INTER_LANCZOS4 - Best
