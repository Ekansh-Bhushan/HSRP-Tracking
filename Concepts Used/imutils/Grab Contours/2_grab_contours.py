# Example of how to use grab_contours with the output of cv2.findContours


import cv2
import imutils

# Load a binary image
image = cv2.imread("grey_image.jpg", 0)

# Find contours using cv2.findContours
contours, _ = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Use imutils.grab_contours to simplify the extraction of contours
contours = imutils.grab_contours((contours, _))

# Now, 'contours' contains the list of detected contours
for contour in contours:
    print(contour)



# In this code, imutils.grab_contours is used to extract the list of contours from the result of 
# cv2.findContours, making the code more concise and easier to read. 
# The resulting contours variable contains the list of detected contours, which can be further 
# processed as required.