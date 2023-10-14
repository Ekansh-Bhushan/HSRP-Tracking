# Example of how to use the sorted function to sort contours by area in descending order


import cv2

# Load an image
image = cv2.imread("image4.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Find contours
contours, _ = cv2.findContours(gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Sort contours by area in descending order
sorted_contours = sorted(contours, key=cv2.contourArea, reverse=True)

# Loop through the sorted contours
for contour in sorted_contours:
    print(contour)



# In this code, cv2.contourArea is used as key function to calculate the area of each contour. 
# The contours are then sorted in descending order based on their areas, meaning the largest 
# contours come first in the sorted_contours list.

# You can replace cv2.contourArea with other functions or custom key functions depending on your 
# sorting criteria. 
# For example, you can use cv2.arcLength to sort contours by perimeter, or you can define a 
# custom function to sort by x or y coordinates, among other criteria. 
# The sorted function is highly versatile and can be used to sort contours based on various 
# criteria to suit your specific image processing needs.