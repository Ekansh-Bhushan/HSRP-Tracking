# Example of using EasyOCR's Reader function:


import easyocr

# Initialize the Reader with the English language
reader = easyocr.Reader(['en'])

# Perform OCR on an image
image_path = 'image1.jpg'
results = reader.readtext(image_path)

# Access and print OCR results
for (text, bbox, prob) in results:
    print(f"Text: {text}")
    print(f"BBox: {bbox}")
    print(f"Confidence: {prob}")
