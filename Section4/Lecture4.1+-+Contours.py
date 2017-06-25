
# coding: utf-8

# In[16]:

import cv2
import numpy as np

image = cv2.imread('images/shapes.jpg')
cv2.imshow('Input Image', image)
cv2.waitKey(0)

# Grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Canny Edges
edged = cv2.Canny(gray, 30, 200)
cv2.imshow('Canny Edges', edged)
cv2.waitKey(0)

# Finding Contours
# Use a copy of your image e.g. edged.copy(), 
# since findContours() slters the image.
_, contours, hierarchy = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
cv2.imshow('Canny Edges after Contouring', edged)
cv2.waitKey(0)

print("Number of contours found = " + str(len(contours)))

# Draw all contours
# Use -1 as the 3rd paramater to draw all contours
cv2.drawContours(image, contours, -1, (0, 255, 0), 3)

cv2.imshow('Contours', image)
cv2.waitKey(0)
cv2.destroyAllWindows()


# cv2.findContours(Image, Retrieval Mode, Approximation Method)
# 
# image has be a grayscale image
# 
# Approximation Methods:
#     cv2.CHAIN_APPROX_NONE        cv2.CHAIN_APPROX_SIMPLE
#     
# Retrieval Mode: Defines hierarchy.
# 
# Heirarchy Types:
#     1) cv2.RETR_LIST - All contours
#     2) cv2.RETR_EXTERNAL - External contours only
#     3) cv2.RETR_COMP - Retrieves in 2-level hierarchy
#     4) cv2.RETR_TREE - Retrieves in full hierarchy
#     
# Hierarchy - [Next, Previous, First Child, Parent]
