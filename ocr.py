import cv2
import pytesseract
import os
from PIL import Image

# Load image
image_path = "test.jpg"
image = cv2.imread(image_path)

if image is None:
    print("Error: Unable to load image.")
    exit()

print("Image loaded successfully.")

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Gaussian Blur to reduce noise
gray = cv2.GaussianBlur(gray, (3, 3), 0)

# Apply adaptive thresholding to make text stand out
gray = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

# Apply morphological operations to remove small noise
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 1))
gray = cv2.morphologyEx(gray, cv2.MORPH_CLOSE, kernel)

# Save processed image for debugging
cv2.imwrite("processed_image.jpg", gray)
print("Processed image saved as 'processed_image.jpg'")

custom_config = "--psm 6 --oem 3" 
text = pytesseract.image_to_string(gray, lang="eng", config=custom_config)

# Print extracted text
print("Extracted Text:")
print(text.strip())  