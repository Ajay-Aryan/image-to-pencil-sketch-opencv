import cv2
import numpy as np
import os

# Load image
img = cv2.imread("dog.jpg")

if img is None:
    raise FileNotFoundError("Image not found. Make sure dog.jpg is in the same folder.")

# Step 1: Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Step 2: Invert the grayscale image
inverted = 255 - gray

# Step 3: Blur the inverted image
blur = cv2.GaussianBlur(inverted, (21, 21), 0)

# Step 4: Invert the blurred image
inverted_blur = 255 - blur

# Step 5: Pencil sketch using dodge blend
sketch = cv2.divide(gray, inverted_blur, scale=256)

# Save outputs
os.makedirs("outputs", exist_ok=True)
cv2.imwrite("outputs/grayscale.jpg", gray)
cv2.imwrite("outputs/inverted.jpg", inverted)
cv2.imwrite("outputs/pencil_sketch.jpg", sketch)

print("Pencil sketch images saved in outputs/ folder")
