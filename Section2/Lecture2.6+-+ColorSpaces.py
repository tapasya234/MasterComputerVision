
# coding: utf-8

# In[2]:

import cv2
import numpy as py

image = cv2.imread('./images/input.jpg')


# In[4]:

# BGR values for the first 0,0 pixel
B, G, R = image[0, 0]
print B, G, R
print image.shape


# In[6]:

# Converting to grayscale
grayImg = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
print grayImg.shape
print grayImg[0, 0]


# # HSV Color Space now

# In[7]:

# H: 0 - 180, S: 0 - 255, V: 0 - 255

image = cv2.imread('./images/input.jpg')
hsvImg = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

cv2.imshow('HSV Image', hsvImg)
cv2.imshow('Hue Channel', hsvImg[:, :, 0])
cv2.imshow('Saturation Channel', hsvImg[:, :, 1])
cv2.imshow('Value Channel', hsvImg[:, :, 2])

cv2.waitKey()
cv2.destroyAllWindows()


# # Individual channels of BGR now

# In[8]:

image = cv2.imread('./images/input.jpg')

# OpenCV's 'split' function splites the image into each color index
B, G, R = cv2.split(image)

print B.shape
cv2.imshow('Red Channel', R)
cv2.imshow('Green Channel', G)
cv2.imshow('Blue Channel', B)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Let's remake the original image
merged = cv2.merge([B, G, R])
cv2.imshow('Merged', merged)

# Let's amplify the blue color
merged = cv2.merge([B+100, G, R])
cv2.imshow('Amplified Blue Image', merged)

# Let's reverse the order
reversed = cv2.merge([R, G, B])
cv2.imshow('Reverse Order Image',reversed)

cv2.waitKey(0)
cv2.destroyAllWindows()


# In[11]:

import cv2
import numpy as np 

B, G, R = cv2.split(image)

# Let's  create a matrix of zeros
# with dimensions of the image h x w
zeros = np.zeros(image.shape[:2], dtype = 'uint8')

cv2.imshow('Red', cv2.merge([zeros, zeros, R]))
cv2.imshow('Green', cv2.merge([zeros, G, zeros]))
cv2.imshow('Blue', cv2.merge([B, zeros, zeros]))

cv2.waitKey(0)
cv2.destroyAllWindows()


# In[ ]:



