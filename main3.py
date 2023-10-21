# ================================== Install and Import Dependencies =========================
import cv2
from matplotlib import pyplot as plt
import numpy as np 
import imutils
import easyocr
import pytesseract
import re



# ================================= Read in image, Grayscale and Blur ========================
img = cv2.imread("/Users/kartik/HSRP-Tracking/Issues/OCR Issue/v23.jpg")
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
# plt.show()
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Whenever you're displaying image using matplotlib, it expects RGB (by default img is in BGR)
plt.imshow(cv2.cvtColor(gray, cv2.COLOR_BGR2RGB))
# plt.show()



# =================================== Apply filter and find edges ============================
bfilter = cv2.bilateralFilter(gray, 17, 17, 17) # Noise Reduction
edged = cv2.Canny(bfilter, 30, 100) # Edge Detection
plt.imshow(cv2.cvtColor(edged, cv2.COLOR_BGR2RGB))
# plt.show()



# ========================================== Find Contours ===================================
# Detecing polygons (ideally we're looking for contour which has 4 points i.e. a rectangle)
# _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
keypoints = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
contours = imutils.grab_contours(keypoints)
contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]
location = None
for contour in contours:
    approx = cv2.approxPolyDP(contour, 10, True)
    if (len(approx) == 4):
        location = approx
        break
# print(location)



# ============================================= Masking ======================================
mask = np.zeros(gray.shape, np.uint8)
new_image = cv2.drawContours(mask, [location], 0, 255, -1)
new_image = cv2.bitwise_and(img, img, mask=mask)
plt.imshow(cv2.cvtColor(new_image, cv2.COLOR_BGR2RGB))
# plt.show()



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
plt.show()









import torch
from torchvision import transforms
from PIL import Image

# Load the ESRGAN model
esrgan_model = torch.load('/Users/kartik/ESRGAN', map_location=torch.device('cpu'))
esrgan_model.eval()

# Convert the cropped_image to a PIL image
cropped_image_pil = Image.fromarray(cropped_image)

# Define a transformation to prepare the image for ESRGAN
esrgan_transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])

# Apply the ESRGAN model to enhance the image
with torch.no_grad():
    input_image = esrgan_transform(cropped_image_pil).unsqueeze(0)
    enhanced_image = esrgan_model(input_image)

# Convert the enhanced image back to a NumPy array
enhanced_image = (enhanced_image.squeeze().permute(1, 2, 0).cpu().numpy() * 255).astype(np.uint8)

# Display the enhanced image
plt.imshow(enhanced_image, cmap='gray')
plt.show()














# # ==================================== Use Easy OCR to read text =============================
# reader = easyocr.Reader(['en'])
# result = reader.readtext(cropped_image)
# print(result)



# # # ================================== Render Result over actual image =========================
# if result:
#     plate_text = result[0][-2]
#     plate_text = plate_text.strip().replace(".", "") # Removing unnecessary Dots
#     plate_text = plate_text.strip().replace(" ", "") # Removing unnecessary Spaces
#     plate_text = plate_text.strip().replace("_", "") # Removing unnecessary Underscores
#     plate_text = plate_text.strip().replace(",", "") # Removing unnecessary Commas
#     plate_text2 = plate_text.strip().replace('“', '') # Removing unnecessary Colons
#     plate_text2 = plate_text.strip().replace('=', '') # Removing unnecessary Equal
#     plate_text = plate_text.upper() # Converting all letters to upper case
#     font = cv2.FONT_HERSHEY_SIMPLEX
#     res = cv2.putText(img, text=plate_text, org=(approx[0][0][0], approx[1][0][1]+60), fontFace=font, fontScale=1, color=(0,255,0), thickness=2, lineType=cv2.LINE_AA)
#     res = cv2.rectangle(img, tuple(approx[0][0]), tuple(approx[2][0]), (0,255,0),3)
#     plt.imshow(cv2.cvtColor(res, cv2.COLOR_BGR2RGB))
#     plt.show()
#     print("EasyOCR: ",plate_text)
# else:
#     print("No text found in the result.")
# plate_text2 = pytesseract.image_to_string(cropped_image, config='--psm 7')  # Adjust the configuration as needed
# plate_text2 = plate_text2.strip().replace(".", "") # Removing unnecessary Dots
# plate_text2 = plate_text2.strip().replace(" ", "") # Removing unnecessary Spaces
# plate_text2 = plate_text2.strip().replace("_", "") # Removing unnecessary Underscores
# plate_text2 = plate_text2.strip().replace(",", "") # Removing unnecessary Commas
# plate_text2 = plate_text2.strip().replace('“', '') # Removing unnecessary Colons
# plate_text2 = plate_text2.strip().replace('=', '') # Removing unnecessary Equal
# plate_text2 = plate_text2.upper() # Converting all letters to upper case
# print("Tesseract: ",plate_text2)


# print("Confirmed Output: ", end="")
# for i in range(len(plate_text)):
#     if(plate_text[i] == plate_text2[i]):
#         print(plate_text[i], end = "")
#     else:
#         print(" ",end = "")
#     i+=1
# print("\n")
