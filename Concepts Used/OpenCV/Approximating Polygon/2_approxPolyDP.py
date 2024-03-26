# Example of using cv2.approxPolyDP to approximate a contour


import cv2
import numpy as np

# Load an image
image = cv2.imread("image3.jpg")

# Convert the image to grayscale and find contours
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
contours, _ = cv2.findContours(gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Approximate each contour to a simpler polygon
epsilon = 0.04 * cv2.arcLength(contours[0], True)  # Set the epsilon based on the original contour's perimeter
approximated_contour = cv2.approxPolyDP(contours[0], epsilon, True)

# Draw the original and approximated contours
cv2.drawContours(image, [contours[0]], -1, (0, 0, 255), 2)  # Red: Original contour
cv2.drawContours(image, [approximated_contour], -1, (0, 255, 0), 2)  # Green: Approximated contour

# Display the image
cv2.imshow("Contours", image)
cv2.waitKey(0)
cv2.destroyAllWindows()



# In this code, we load a image, find its contours, and then use cv2.approxPolyDP to approximate 
# the first contour in the list. The approximation is drawn in green, while the original contour 
# is drawn in red. This helps simplify the shape for further analysis or visualization.