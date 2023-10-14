# ================================== Install and Import Dependencies =========================
import cv2
from matplotlib import pyplot as plt
import numpy as np 
import imutils
import easyocr


# ================================= Read in image, Grayscale and Blur ========================
# img = cv2.imread("image2.jpg") # giving issue for now
img = cv2.imread("image3.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Whenever you're displaying image using matplotlib, it expects RGB (by default img is in BGR)
plt.imshow(cv2.cvtColor(gray, cv2.COLOR_BGR2RGB))
plt.show()


# =================================== Apply filter and find edges ============================
bfilter = cv2.bilateralFilter(gray, 17, 17, 17) # Noise Reduction
edged = cv2.Canny(bfilter, 30, 200) # Edge Detection
plt.imshow(cv2.cvtColor(edged, cv2.COLOR_BGR2RGB))
plt.show()


# ========================================== Find Contours ===================================
# Detecing polygons (ideally we're looking for contour which has 4 points i.e. a rectangle)
keypoints = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
contours = imutils.grab_contours(keypoints)
contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]
location = None
for contour in contours:
    approx = cv2.approxPolyDP(contour, 10, True)
    if (len(approx) == 4):
        location = approx
        break
print(location)


# ============================================= Masking ======================================
mask = np.zeros(gray.shape, np.uint8)
new_image = cv2.drawContours(mask, [location], 0, 255, -1)
new_image = cv2.bitwise_and(img, img, mask=mask)
plt.imshow(cv2.cvtColor(new_image, cv2.COLOR_BGR2RGB))
plt.show()


# ============================== Extracting the number plate section =========================
(x,y) = np.where(mask == 255) # locate specific regions in the image where pixel values are 25
(x1, y1) = (np.min(x), np.min(y))
(x2, y2) = (np.max(x), np.max(y))
cropped_image = gray[x1:x2+1, y1:y2+1]
# Here's an explanation of how this line of code works:
# 1. gray is assumed to be a grayscale image. It's a two-dimensional NumPy array where each 
#     pixel's intensity is represented by a single value (typically ranging from 0 to 255).
# 2. (x1, y1) represents the top-left corner of the region of interest (ROI), and (x2, y2) 
#     represents the bottom-right corner of the ROI. These values were obtained using the 
#     numpy.where function and correspond to the coordinates of the bounding box around the 
#     number plate in the image.
# 3. The expression gray[x1:x2+1, y1:y2+1] is a NumPy array slicing operation that extracts the 
#     subregion of the gray image defined by the coordinates (x1, y1) as the top-left corner and 
#     (x2, y2) as the bottom-right corner.
#     (A) x1:x2+1 defines the range of rows to be extracted, where x1 is the starting row and 
#         x2+1 is the ending row. 
#         This ensures that the slice includes the row with index x2.
#     (B) y1:y2+1 defines the range of columns to be extracted, where y1 is the starting column 
#         and y2+1 is the ending column. 
#         This ensures that the slice includes the column with index y2.
# The +1 is added to the ending row and column indices to ensure that the bottom-right corner 
# pixel is included in the extracted region. 
# NumPy's array slicing is exclusive of the ending index by default, so adding 1 includes the 
# last element.
plt.imshow(cv2.cvtColor(cropped_image, cv2.COLOR_BGR2RGB))
# plt.show()