#import cv2, numpy and matplotlib libraries
import cv2
import numpy as np
import matplotlib.pyplot as plt
img=cv2.imread("img.jpeg")

# Converting BGR color to RGB color format
RGB_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Using 0 to read image in grayscale mode 
GRAY_img = cv2.imread("img.jpeg", cv2.IMREAD_GRAYSCALE) 

# Using cv2.ROTATE_180 rotate by 
# 180 degrees clockwise
rotated_img = cv2.rotate(img, cv2.ROTATE_180)

#Displaying image using cv2.imshow() method
cv2.imshow('Original image', img)
cv2.imshow('Colored image',RGB_img)
cv2.imshow('Grayscale image', GRAY_img) 
cv2.imshow('Rotated image', rotated_img)

#hold the window
cv2.waitkey(0)
cv2.destroyAllWindows()
