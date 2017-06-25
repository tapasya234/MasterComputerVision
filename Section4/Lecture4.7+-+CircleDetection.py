
# coding: utf-8

# ## Circle Detection using Hough Circles
# #### cv2.HoughCircles(image, 
# ####                 method, # Curently cv2.HOUGH_GRADIENT 
# ####                 dp, # Inverse ratio of accumultor resolution
# ####                 minDist, # Min Dist between center of detected circles
# ####                 param1, # Gradient value used in edge detection
# ####                 param2, # Accumulator threshold for HOUGH_GRADIENT method
# ####                 minRadius, # Limits the smalest circle to this size
# ####                 maxRadius) # Limits the largest circle
# 

# In[4]:

import cv2
import numpy as np

image = cv2.imread('images/bottlecaps.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

blur = cv2.medianBlur(gray, 5)
circles = cv2.HoughCircles(blur, cv2.HOUGH_GRADIENT, 1.9, 50, 
                           param1 = 100, param2 = 100, 
                           minRadius = 20, maxRadius = 50)

for i in circles[0, :]:
    # draw the outer circle
    cv2.circle(image, (i[0], i[1]), i[2], (255, 0, 0), 2)
    
    # draw the center of the circle
    # cv2.circle(image, (i[0], i[1]), 2, (0, 255, 0), 5)

cv2.imshow('Detected Circles', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

