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


