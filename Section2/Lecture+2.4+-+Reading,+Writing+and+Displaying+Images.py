
# coding: utf-8

# In[2]:

# Importing the required directories
import cv2
import numpy as np


# In[4]:

# We don't need to do this again, but it's a good habit
import cv2

# Load an image using 'imread' specifying the path to image
input = cv2.imread('./images/input.jpg')

# To display image variable, we use 'imshow'
# The first parameter will be title shown on the image window
# The second parameter is the image variable
cv2.imshow('Hello World', input)

# waitKey allows us to inpupt information when a image window is open.
# By leaving it blank. it just waits for any key to be pressed before
# continuing. By placing numbers (except 0), we can specify a delay for
# how long you keep the window open ( time is in milliseconds )
cv2.waitKey()

# This closes all open windows
# Failure to place this will cause your program to hang
cv2.destroyAllWindows()


# # Let's take a closer look at how images are stored.

# In[5]:

import numpy as np


# In[6]:

print input.shape


# In[7]:

# Each dimension of the image

print 'Height of Image:', int(input.shape[0]), 'pixels'
print 'Width of Image:', int(input.shape[1]), 'pixels'


# In[8]:

# Use 'imwrite' by specifying the file name and the image variable name
# to save the image
cv2.imwrite('output.png', input)
cv2.imwrite('output.jpg', input)


# In[ ]:



