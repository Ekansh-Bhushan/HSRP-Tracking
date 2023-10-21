from roboflow import Roboflow
from PIL import Image
import requests
from io import BytesIO

rf = Roboflow(api_key="y7mPTzvEBkBqc0GiIVu0")
project = rf.workspace().project("license-plate-recognition-rxg4e")
model = project.version(4).model

# Make a prediction
prediction = model.predict("./Issues/OCR Issue/v30.jpg", confidence=40, overlap=30)

# Save the prediction image
prediction_image = prediction.save("prediction.jpg")

# Open and display the saved image
img = Image.open("prediction.jpg")
img.show()


for single_prediction in prediction:
    # Check if this prediction has a class "License_Plate"
    if single_prediction["class"] == "License_Plate":
        license_plate_coords = {
            "left": single_prediction["width"],
            "top": single_prediction["height"],
            "right": single_prediction["x"] + single_prediction["width"],
            "bottom": single_prediction["y"] + single_prediction["height"]
        }

        # Crop the license plate from the image
        license_plate_img = img.crop((license_plate_coords["left"], license_plate_coords["top"],
                                      license_plate_coords["right"], license_plate_coords["bottom"]))

        # Save the cropped license plate
        license_plate_img.save("cropped_license_plate.jpg")
        license_plate_img.show()