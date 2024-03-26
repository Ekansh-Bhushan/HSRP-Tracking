# Example of using cv2.findContours() & cv2.drawContours() to find and draw contours in image

import cv2

# Load an image
image = cv2.imread("grey_image.jpg")

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Find contours in the grayscale image
contours, _ = cv2.findContours(gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Draw the contours on the original image
output_image = cv2.drawContours(image, contours, -1, (0, 0, 255), 2)  # Red color, 2-pixel thickness

# Display the image with contours
cv2.imshow("Contours", output_image)
cv2.waitKey(0)
cv2.destroyAllWindows()




# In this code, the code loads an image, converts it to grayscale, finds contours, and then uses 
# cv2.drawContours to draw the contours on the original image. 
# The drawn contours are highlighted in red with a 2-pixel thickness. 
# This visualization helps you see the boundaries of objects detected in the image.