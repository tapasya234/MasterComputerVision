
# coding: utf-8

# In[1]:

# let's create some simple images
import cv2
import numpy as np

# Making a grayscale square
square = np.zeros((300, 300), np.uint8)
cv2.rectangle(square, (50, 50), (250, 250), 255, -2)
cv2.imshow("Square", square)
cv2.waitKey(0)

# Making an ellipse
ellipse = np.zeros((300, 300), np.uint8)
cv2.ellipse(ellipse, (150, 150), (150, 150), 30, 0, 180, 255, -1)
cv2.imshow("Ellipse", ellipse)
cv2.waitKey(0)

cv2.destroyAllWindows()


# # Experimenting with Bitwise operations

# In[2]:

# AND - Shows only where they intersect
And = cv2.bitwise_and(square, ellipse)
cv2.imshow('AND', And)
cv2.waitKey(0)

# OR - Shows where either square or ellipse or both are present
Or = cv2.bitwise_or(square, ellipse)
cv2.imshow('OR', Or)
cv2.waitKey(0)

# XOR - Shows where either square or ellipse is present
Xor = cv2.bitwise_xor(square, ellipse)
cv2.imshow('XOR', Xor)
cv2.waitKey(0)

# NOT - Shows everything that isn't part of the square
Not_sqr = cv2.bitwise_not(square)
cv2.imshow('NOT - Square', Not_sqr)
cv2.waitKey(0)

cv2.destroyAllWindows()


# In[ ]:



