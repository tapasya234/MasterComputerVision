
# coding: utf-8

# ## Mini Project #1 - Live Sketch Using Webcam

# In[4]:

import cv2
import numpy as np

# Sketch generating function
def sketch(image):
    
    # Convert image to grayscale
    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Clean up image using Gaussian Blur
    img_gray_blur = cv2.GaussianBlur(img_gray, (5, 5), 0)
    
    # Extracting edges
    canny_edges = cv2.Canny(img_gray_blur, 10, 70)
    
    # Performing Inverse Binirization on the above image
    ret, mask = cv2.threshold(canny_edges, 127, 255, cv2.THRESH_BINARY_INV)
    return mask

# Initialize webcam, cap is the object provided by VideoCapture
# It contains a boolean indicating if it was successful (ret)
# It also contains the images collected from the webcam (frame)
cap = cv2.VideoCapture(0)

while True:
    ret,frame = cap.read()
    cv2.imshow('Live Sketch App', sketch(frame))
    
    if cv2.waitKey(1) == 13: # 13 - Enter Key ASCII value
        break

# Release camera and close windows
cap.release()
cv2.destroyAllWindows()

