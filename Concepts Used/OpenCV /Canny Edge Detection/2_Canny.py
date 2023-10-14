# Example of using the cv2.Canny() function in OpenCV for edge detection on an input image

import cv2
import numpy as np
from matplotlib import pyplot as plt

# Load an image
image = cv2.imread("image1.jpg", 0)  # Load the image in grayscale

# Apply Canny edge detection
edges = cv2.Canny(image, threshold1=30, threshold2=200)

# Display the original image and the detected edges side by side
plt.figure(figsize=(12, 5))
plt.subplot(121), plt.imshow(image, cmap="gray")
plt.title("Original Image"), plt.axis("off")
plt.subplot(122), plt.imshow(edges, cmap="gray")
plt.title("Canny Edges"), plt.axis("off")
plt.show()


# In this example:
# 1. We load an input image in grayscale mode using cv2.imread. The image is represented in 
#   grayscale to simplify the edge detection process.
# 2. We apply Canny edge detection using cv2.Canny(). The threshold1 and threshold2 parameters 
#   control the lower and upper thresholds for edge detection. These values can be adjusted 
#   based on the specific image and application requirements.
# 3. We use Matplotlib to display both original image and detected edges side by side for 
#   visualization. The cmap="gray" argument specifies that we want to display images in grayscale.

# When you run this code with your image file, you'll see the original image on the left and the 
# Canny edge-detected version on the right. The edges in the image are highlighted, making them 
# more visually apparent.

# The result will show the power of Canny edge detection in identifying the boundaries and edges 
# of objects in images. The specific threshold values may need to be adjusted depending on the 
# image content and your application's needs.