import cv2
import numpy as np
import json
import pytesseract
import re 

# Hologram Removal 
def preprocess_image1(image_path):  # Returns a thresholded (binarized) image
    original = cv2.imread(image_path)
    grayscale = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
    # Create an empty black image of the same size as the grayscale image
    thresholded = np.zeros_like(grayscale) * 0
    # Set pixels to white (255) if the grayscale pixel value is greater than 50
    thresholded[grayscale >= 40] = 255

    return thresholded


# Load the RTO code data from a JSON file
with open("rto_codes.json", "r") as json_file:
    rto_data = json.load(json_file)


image_path = "test.jpg"
original = cv2.imread(image_path)
preprocessed = preprocess_image1(image_path)
cv2.imshow("Preprocessed Image", preprocessed)
cv2.waitKey(0)

# Use OpenCV to find contours in the image
contours, _ = cv2.findContours(
    preprocessed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Initialize variables to store license plate information
plate_text = ""
plate_coordinates = []

# Define a function to filter and validate license plate candidates
def is_valid_plate(candidate):
    # print(candidate)
    # License plates in India typically have 10 or 9 characters
    if (len(candidate) != 10 and len(candidate)!=9):  
        return False 

    # Check if the first 2 characters are alphabets (state code)
    state_code = candidate[:2]
    if not re.match(r'^[A-Z]{2}$', state_code):
        return False
    
    # Check if the last 4 characters are digits
    numbers = candidate[-4:]
    if not re.match(r'^\d{4}$', numbers):
        return False

    # Check the color scheme (black on white for private vehicles, black on yellow for commercial vehicles)

    return True


# Iterate through the contours and process each potential license plate
for contour in contours:
    x, y, w, h = cv2.boundingRect(contour)
    # Extract the region of interest (ROI) containing the potential license plate
    plate_roi = preprocessed[y:y + h, x:x + w]
    plate_roi2 = original[y:y + h, x:x + w] # This is coloured, used for getting colour scheme

    # Perform OCR on the license plate region
    plate_text = pytesseract.image_to_string(plate_roi, config='--psm 6')

     # Store license plate coordinates
    plate_coordinates = [(x, y), (x + w, y), (x + w, y + h), (x, y + h)]
    break  # Break the loop after the first valid plate is found






# =========== Check if a license plate was detected and extracted =============
# Remove all spaces from plate_text
plate_text = plate_text.strip().replace(" ", "")
plate_code = plate_text[:4]
type_detector = plate_text[3]
if is_valid_plate(plate_text):
    print(f"License Plate Number: {plate_text}")
    print("License Plate Coordinates:", plate_coordinates)
else:
    print("No valid license plate detected.")





# ================= Look up the state and district information ================
if plate_code in rto_data:
    state = rto_data[plate_code]["state"]
    district = rto_data[plate_code]["district"]
    if state == " " or state == district:
        print(f"The vehicle belongs to {district}")
    else:
        print(f"The vehicle belongs to {district}, {state}")
else:
    print("RTO code not found in the database.")





# ======================= Look up the type of vehicle ===========================
if (type_detector.isalpha()):
    if type_detector == "C":
        print("The number plate belongs to a Car")
    elif type_detector == "E":
        print("The number plate belongs to Electric Vehicle")
    elif type_detector == "P":
        print("The number plate belongs to Passenger Vehicle")
    elif type_detector == "R":
        print("The number plate belongs to 3 wheeler Vehicle")
    elif type_detector == "S":
        print("The number plate belongs to 2 wheeler Vehicle")
    elif type_detector == "T":
        print("The number plate belongs to Tourist Purpose Vehicle")
    elif type_detector == "Y":
        print("The number plate belongs to Vehicle which can be hired")
    elif type_detector == "V":
        print("The number plate belongs to Vehicle used in Transportation")

