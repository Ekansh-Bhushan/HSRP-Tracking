import cv2

# Load an image
img = cv2.imread("image2.jpg")

# Apply bilateral filtering
bfilter = cv2.bilateralFilter(img, d=9, sigmaColor=75, sigmaSpace=75)

# Display the filtered image
cv2.imshow("Bilateral Filtered Image", bfilter)
cv2.waitKey(0)
cv2.destroyAllWindows()



# In this example, cv2.bilateralFilter is used to filter the input image img with the specified 
# parameters. The result is displayed, showing the image with noise reduced while preserving 
# edges and fine details.