
# coding: utf-8

# ## Black Square

# In[1]:

import cv2
import numpy as np

# Ceate a black image
image = np.zeros((512, 512, 3), np.uint8)

# Can we make this in black and white
imageBW = np.zeros((512, 512), np.uint8)

cv2.imshow('Black Rectangle (Color)', image)
cv2.imshow('Black Rectangle (B&W)', imageBW)

cv2.waitKey(0)
cv2.destroyAllWindows()


# ## Line

# In[2]:

image = np.zeros((512, 512, 3), np.uint8)
cv2.line(image, (0, 0), (511, 511), (255, 127, 0), 5)
cv2.imshow('Blue Line', image)

cv2.waitKey(0)
cv2.destroyAllWindows()


# ## Rectangle

# In[4]:

image = np.zeros((512, 512, 3), np.uint8)

cv2.rectangle(image, (100, 100), (300, 250), (125, 50, 127), 5)
# To fill the rectangle replace 5 with -1 
cv2.imshow('Rectangle', image)

cv2.waitKey(0)
cv2.destroyAllWindows()


# ## Circle

# In[5]:

image =np.zeros((512, 512, 3), np.uint8)


cv2.circle(image, (350, 350), 100, (15, 75, 50), -1)
cv2.imshow('Circle', image)

cv2.waitKey(0)
cv2.destroyAllWindows()


# ## Polygon

# In[6]:

image = np.zeros((512, 512, 3), np.uint8)

# Lets define 4 points
pts = np.array( [[10, 50], [400, 50], [90, 200], [50, 500]], np.int32)

# Let's reshape our points in form required by polylines
pts = pts.reshape((-1, 1, 2))

cv2.polylines(image, [pts], True, (0, 0, 255), 3)
# True depicts whether or not it is a closed polygon.
cv2.imshow('Polygon', image)

cv2.waitKey(0)
cv2.destroyAllWindows()


# ## Text

# In[7]:

image = np.zeros((512, 512, 3), np.uint8)

cv2.putText(image, 'Hello, World!', (75, 290), cv2.FONT_HERSHEY_COMPLEX, 2, (100, 170, 90), 3)
cv2.imshow('Blue Line', image)

cv2.waitKey(0)
cv2.destroyAllWindows()

