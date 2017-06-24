
# coding: utf-8

# In[3]:

import cv2

# Load our image
image = cv2.imread('./images/input.jpg')
cv2.imshow('Original', image)
cv2.waitKey()

# We use cvtColor, to convert to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow('Grayscale', gray_image)
cv2.waitKey()
cv2.destroyAllWindows()


# In[4]:

# Faster method
img = cv2.imread('./images/input.jpg', 0)
# 0 - Reads the image in grayscale format

cv2.imshow('Grayscale', img)
cv2.waitKey()
cv2.destroyAllWindows()

