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