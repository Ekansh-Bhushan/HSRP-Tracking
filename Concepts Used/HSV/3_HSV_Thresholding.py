# Example of thresholding based on HSV color space 
import cv2
import numpy as np

# Load an image
image = cv2.imread('image.jpg')

# Convert to HSV
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Define lower and upper thresholds for hue, saturation, and value
lower_hue = 30
upper_hue = 60
lower_saturation = 100
upper_saturation = 255
lower_value = 50
upper_value = 255

# Create masks based on the thresholds
hue_mask = cv2.inRange(hsv_image[:, :, 0], lower_hue, upper_hue)
saturation_mask = cv2.inRange(hsv_image[:, :, 1], lower_saturation, upper_saturation)
value_mask = cv2.inRange(hsv_image[:, :, 2], lower_value, upper_value)

# Combine the masks as needed (e.g., an AND operation)
final_mask = cv2.bitwise_and(hue_mask, cv2.bitwise_and(saturation_mask, value_mask))

# Display the resulting mask
cv2.imshow('Thresholded Mask', final_mask)

cv2.waitKey(0)
cv2.destroyAllWindows()





# 1. Thresholding based on HSV:
#     For each HSV component (Hue, Saturation, and Value), you have defined lower and upper threshold 
#     values to segment specific ranges of colors or intensities.
# 2. Creating Masks: 
#     cv2.inRange() function is used to create masks for each of the HSV components based on threshold 
#     values. It essentially assigns a binary value (0 or 255) to each pixel in the component image 
#     based on whether it falls within the specified threshold range.
#     For example, hue_mask will contain a binary image where pixels with Hue values within lower_hue 
#     and upper_hue range are set to 255, and pixels outside that range are set to 0.
# 3. Combining Masks:
#     After creating individual masks for each component, you may want to combine them to obtain a 
#     single mask that meets all the specified criteria.
#     In this code, the cv2.bitwise_and() function is used to perform a bitwise AND operation between 
#     the hue_mask, saturation_mask, and value_mask. This means that a pixel in the final mask will be 
#     255 (white) if and only if it is 255 in all three component masks. Otherwise, it'll be 0 (black).
#     By doing this, you are ensuring that only the pixels that meet all the specified criteria for Hue, 
#     Saturation, and Value are retained in the final_mask.


# The final_mask is now a binary image where white pixels represent the areas in the original image that 
# satisfy all three conditions (Hue, Saturation, and Value), and black pixels represent the areas that 
# do not meet all the conditions.

# This combined mask can be further used for various purposes, such as object segmentation or extracting 
# regions of interest from an image based on specific color characteristics.


# In this code, we define lower & upper thresholds for Hue, Saturation, and Value. We then create 
# individual masks for each component based on these thresholds. The final mask is obtained by 
# performing bitwise AND operations on these component masks, which allows you to isolate the regions 
# that meet all the criteria.

# You can adjust the threshold values to segment specific color ranges or intensities in your image for 
# various applications, including object detection or color-based segmentation.