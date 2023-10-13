# Example to illustrate how to access and visualize each components of HSV color space 
import cv2
import numpy as np

# Load an image
image = cv2.imread('vehicle_image2.jpg')

# Convert to HSV
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Access HSV components
hue = hsv_image[:, :, 0]
saturation = hsv_image[:, :, 1]
value = hsv_image[:, :, 2]

# Display each component
cv2.imshow('Hue', hue)
cv2.imshow('Saturation', saturation)
cv2.imshow('Value', value)

cv2.waitKey(0)
cv2.destroyAllWindows()


# This code loads an image, converts it to the HSV color space, and then displays the individual Hue, 
# Saturation, and Value components.