
# coding: utf-8

# In[2]:

import cv2
import numpy as np

# We need to import matplotlib to create our histogram plots
from matplotlib import pyplot as plt

image = cv2.imread('./images/input.jpg')

histogram = cv2.calcHist([image], [0], None, [256], [0, 256])

# We plot a histogram, ravel() flattens our image array
plt.hist(image.ravel(), 256, [0, 256]); plt.show()

# Viewing Separate Color Channels
color = ('b', 'g', 'r')

# We now separate the colors and plot each in the Histogram
for i, col in enumerate(color):
    histogram2 = cv2.calcHist([image], [i], None, [256], [0, 256])
    plt.plot(histogram2, color = col)
    plt.xlim([0, 256])
    
plt.show()


# In[9]:

import cv2

image = cv2.imread('./images/input.jpg')
cv2.imshow('Image', image)


# # cv2.calcHis(images, channels, mask, histSize, ranges[, hist[, accumulate]])

# In[3]:

import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread('images/tobago.jpg')
cv2.imshow('Tobago Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

histogram = cv2.calcHist([image], [0], None, [256], [0, 256])
plt.hist(image.ravel(), 256, [0, 256]); plt.show()

# Viewing separate color channels
color = ('b', 'g', 'r')

for i, col in enumerate(color):
    histogram2 = cv2.calcHist([image], [i], None, [256], [0, 256])
    plt.plot(histogram2, color = col)
    plt.xlim([0, 256])
    
plt.show()

