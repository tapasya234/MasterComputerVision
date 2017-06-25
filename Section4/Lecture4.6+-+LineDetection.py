
# coding: utf-8

# ## Hough Lines
# ### cv2.HoughLines(binarized image, rho accuracy, thetha accuracy, threshold)

# In[17]:

import cv2
import numpy as np

image = cv2.imread('images/sudoku.jpg')
cv2.imshow('Original', image)
cv2.waitKey(0)

# Grayscale and Canny Edges extracted
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 100, 170, apertureSize = 3)

# Run HoughLines using rho accuracy of 1 pixel
# theta accuracy og np.pi / 180 which is 1 degree
# Our line threshold is set to 240 ( number of points on line)
lines = cv2.HoughLines(edges, 1, np.pi / 180, 230) # 240 - recomemded

# We iterate through each line and convert it to the format
# required by cv.lines (i.e., requiring end points)
for line in lines:
    
    rho, theta = line[0]
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a * rho
    y0 = b * rho
    x1 = int(x0 + 1000 * (-b))
    y1 = int(y0 + 1000 * (a))
    x2 = int(x0 - 1000 * (-b))
    y2 = int(y0 - 1000 * (a))
    cv2.line(image, (x1, y1), (x2, y2), (255, 0, 0), 2)
    
cv2.imshow('Hough Lines', image)
cv2.waitKey(0)
cv2.destroyAllWindows()


# ## Probabilistic Hough Lines
# ### cv2.HoughLinesP(binarized image, rho accuracy, theta accuracy, threshold, min line length, max line gap)

# In[19]:

import cv2
import numpy as np

image = cv2.imread('images/sudoku.jpg')

# Grayscale and Canny Edges extracted
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 100, 170, apertureSize = 3)

# Again, we use the same rho and theta accuracies.
# However, we specify a minimum vote (pts along line) of 100
# and Min line length of 5 pixels and max gap between lines as 10
lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 100, 5, 10)
print lines.shape

for line in lines:
    x1, y1, x2, y2 = line[0]
    cv2.line(image, (x1, y1), (x2, y2), (0, 255, 0), 3)
    
cv2.imshow('Probabilistic Hough Lines', image)
cv2.waitKey(0)
cv2.destroyAllWindows()


# http://cmp.felk.cvut.cz/~matas/papers/matas-bmvc98.pdf <-  Can't  be reached as of 06/25/2017
