import cv2
import numpy as np
import json
import pytesseract

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


# Load the RTO code data from a JSON file
with open("rto_codes.json", "r") as json_file:
    rto_data = json.load(json_file)


image_path = "vehicle_image2.jpg"
preprocessed = preprocess_image1(image_path)
cv2.imshow("Preprocessed Image", preprocessed)
cv2.waitKey(0)
# cv2.imshow("Preprocessed Image", preprocess_image2(image_path))
# cv2.waitKey(0)

# Use OpenCV to find contours in the image
contours, _ = cv2.findContours(
    preprocessed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Initialize variables to store license plate information
plate_text = ""
plate_coordinates = []

# Define a function to filter and validate license plate candidates


def is_valid_plate(candidate):
    # Implement your criteria for license plate validation here
    # For example, check for minimum and maximum dimensions, aspect ratio, etc.
    return True


# Iterate through the contours and process each potential license plate
for contour in contours:
    x, y, w, h = cv2.boundingRect(contour)
    if is_valid_plate(contour):
        # Extract the region of interest (ROI) containing the potential license plate
        plate_roi = preprocessed[y:y + h, x:x + w]

        # Perform OCR on the license plate region
        plate_text = pytesseract.image_to_string(plate_roi, config='--psm 6')

        # Store license plate coordinates
        plate_coordinates = [(x, y), (x + w, y), (x + w, y + h), (x, y + h)]
        break  # Break the loop after the first valid plate is found

# Check if a license plate was detected and extracted
if plate_text:
    # Remove all spaces from plate_text
    plate_text = plate_text.strip().replace(" ", "")
    print(f"License Plate: {plate_text}")
    print("License Plate Coordinates:", plate_coordinates)
else:
    print("No valid license plate detected.")


plate_code = plate_text[:4]
type_detector = plate_text[3]


# Look up the state and district information
if (type_detector.isdigit()):
    if plate_code in rto_data:
        state = rto_data[plate_code]["state"]
        district = rto_data[plate_code]["district"]
        if state == " " or state == district:
            print(f"The vehicle belongs to {district}")
        else:
            print(f"The vehicle belongs to {district}, {state}")
    else:
        print("RTO code not found in the database.")
elif (type_detector.isalpha()):
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
