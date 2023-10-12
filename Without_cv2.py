import cv2
import numpy as np

# WITH BASE AS BLACK
def preprocess_image1(image_path):  # Returns a thresholded (binarized) image
    original = cv2.imread(image_path)
    grayscale = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
    # Create an empty black image of the same size as the grayscale image
    thresholded = np.zeros_like(grayscale) * 0
    # Set pixels to white (255) if the grayscale pixel value is greater than 50
    thresholded[grayscale >= 50] = 255

    return thresholded

# WITH BASE AS WHITE
def preprocess_image2(image_path):  # Returns a thresholded (binarized) image
    original = cv2.imread(image_path)
    grayscale = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
    # Create an empty white image of the same size as the grayscale image
    thresholded = np.ones_like(grayscale) * 255
    # Set pixels to black (0) if the grayscale pixel value is greater than 50
    thresholded[grayscale <= 50] = 0

    return thresholded


image_path = "vehicle_image2.jpg"
cv2.imshow("Preprocessed Image", preprocess_image1(image_path))
cv2.waitKey(0)
# cv2.imshow("Preprocessed Image", preprocess_image2(image_path))
# cv2.waitKey(0)
