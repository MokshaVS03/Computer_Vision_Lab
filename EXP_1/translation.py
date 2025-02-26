import numpy as np
import cv2
import imutils

# load the image and display it to our screen
image = cv2.imread('coal_city.jpg')
cv2.imshow("Original", image)
cv2.waitKey(0)

# Define a translation  matrix (M) to shift the image 40 pixels
# to the right and 50 pixels downwards.
M = np.float32([[1, 0, 40], [0, 1, 50]])

# get image's width and height.
img_width = image.shape[1]
img_height = image.shape[0]
print(f"translation matrix:\n {M} \n Image's width: {img_width} \n Image's height: {img_height}")

# Shift the image 40 pixels rightwards and 50 pixels downwards
shifted_image = cv2.warpAffine(image, M, (img_width, img_height))
cv2.imshow("Shifted Down and Right", shifted_image)
cv2.waitKey(0)

# shift the image 70 pixels leftwards and 120 pixels rightwards
# by specifying negative values for the x and y directions,
# respectively
M = np.float32([[1, 0, -70], [0, 1, -120]])
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
cv2.imshow("Shifted Up and Left", shifted)
cv2.waitKey(0)

# use the imutils function to translate the image 100 pixels
# downwards in a single function call
shifted = imutils.translate(image, 0, 100)
cv2.imshow("Shifted Down", shifted)
cv2.waitKey(0)

# use the imutils function to translate the image 120 pixels
# to the left in a single function call
# by supplying negative values to the x-axis
shifted = imutils.translate(image, -120, 0)
cv2.imshow("Shifted Left", shifted)
cv2.waitKey(0)