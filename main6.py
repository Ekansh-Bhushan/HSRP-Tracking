from PIL import Image

# Your existing code for prediction
from roboflow import Roboflow
rf = Roboflow(api_key="y7mPTzvEBkBqc0GiIVu0")
project = rf.workspace().project("license-plate-recognition-rxg4e")
model = project.version(4).model
prediction = model.predict("Issues/OCR Issue/v15.JPG", confidence=40, overlap=30).json()

# # Get the coordinates of the license plate
# license_plate = prediction['predictions'][0]
# x, y, width, height = license_plate['x'], license_plate['y'], license_plate['width'], license_plate['height']

# # Open the original image
# original_image = Image.open("Issues/OCR Issue/v15.JPG")

# # Crop the license plate from the original image
# cropped_license_plate = original_image.crop((x, y, x + width, y + height))

# # Save or display the cropped license plate
# cropped_license_plate.show()  # To display the cropped image
# # cropped_license_plate.save("cropped_license_plate.jpg")  # To save the cropped image to a file
