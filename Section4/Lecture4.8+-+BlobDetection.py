
# coding: utf-8

# In[6]:

import cv2
import numpy as np;

image = cv2.imread('images/Sunflowers.jpg', cv2.IMREAD_GRAYSCALE)

# Set up the detector with default parameters
params = cv2.SimpleBlobDetector_Params()
detector = cv2.SimpleBlobDetector_create(params)

# Detect blobs
keypoints = detector.detect(image)

# Draw detected blobs as red circles
# cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures the size of
# the circle corresponds to the size of blob
blank = np.zeros((1, 1))
blobs = cv2.drawKeypoints(image, keypoints, blank, (0, 255, 255),
                         cv2.DRAW_MATCHES_FLAGS_DEFAULT)

# Show keypoints
cv2.imshow("Blobs", blobs)
cv2.waitKey(0)
cv2.destroyAllWindows()


# ### cv2.drawKeypoints(input, image, keypoints, blank_output_array, color, flag)
# 
# Flags:
#  - cv2.DRAW_MATCHES_FLAGS_DEFAULT
#  - cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS
#  - cv2.DRAW_MATCHES_FLAGS_DRAW_OVER_OUTING
#  - cv2.DRAW_MATCHES_FLAGS_NOT_DRAW_SIMGLE_POINTS
