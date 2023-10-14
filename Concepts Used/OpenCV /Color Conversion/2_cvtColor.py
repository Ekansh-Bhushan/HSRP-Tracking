# Example of how to use cv2.cvtColor() to convert an image from BGR to grayscale

import cv2

# Load an image
img = cv2.imread("vehicle_image2.jpg")

# Convert BGR image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Display the image
cv2.imshow("Grayscale Image", gray)
cv2.waitKey(0)
cv2.destroyAllWindows()



# Above code utilizes the OpenCV library to perform a sequence of image processing operations. 
# It begins by loading an image called "vehicle_image2.jpg" using the cv2.imread() function, 
# preserving its original BGR (Blue-Green-Red) color format. 
# Subsequently, code employs cv2.cvtColor() function with cv2.COLOR_BGR2GRAY color conversion 
# code to transform BGR image into grayscale image, resulting in single-channel representation. 
# The grayscale image is stored in the 'gray' variable. 
# Finally, code displays the grayscale image in OpenCV window titled "Grayscale Image" using 
# cv2.imshow(). 
# It waits for a key press using cv2.waitKey(0), and upon receiving a key press, it closes 
# window and releases system resources with cv2.destroyAllWindows().