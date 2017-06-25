
# coding: utf-8

# #### cv2.matchShapes(contour template, contour, method, method parameter)
# #### Output - match value ->lower it is, closer match
# ##### Contour Template - This is our reference contour that we're trying to find in the image
# ##### Contour - The individual contour we are checking against 
# ##### Method - Type of contour matching (1, 2, 3)
# ##### Method Parameter - Leave as 0.0 (Not fully utilized in Python OpenCV)

# In[12]:

import cv2
import numpy as np

# Load the shape template or reference image
template = cv2.imread('images/4star.jpg', 0)
cv2.imshow('Template', template)
cv2.waitKey()

# Load the target image with shapes we're trying to match
target = cv2.imread('images/shapestomatch.jpg')
target_gray = cv2.cvtColor(target, cv2.COLOR_BGR2GRAY)

# Threshold both images first before using cv2.findContours
ret, thresh1 = cv2.threshold(template, 127, 255, 0)
ret, thresh2 = cv2.threshold(target_gray, 127, 255, 0)

# Find contours in template
_, contours, hierarchy = cv2.findContours(thresh1, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)

# We need to sort the contours by area so that we can remove 
# the largest contour which is the image outline
sorted_contours = sorted(contours, key = cv2.contourArea, reverse = True)

# We extract the second largest contour whicch will be our template contour
template_contour = sorted_contours[1]

# Find contours in template
_, contours, hierarchy = cv2.findContours(thresh2, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)

for c in contours:
    # Iterate through each contourin the target image and 
    # use cv2.matchShapes to compare contour shapes
    match = cv2.matchShapes(template_contour, c, 1, 0.0)
    print match
    
    # If the match value is less than 0.15 we,
    if match < 0.15:
        closest_contour = c
    else:
        closest_contour = []

#print closest_contour
cv2.drawContours(target, [closest_contour], -1, (255, 255, 0), 3)
cv2.imshow('Output', target)
cv2.waitKey(0)
cv2.destroyAllWindows()

