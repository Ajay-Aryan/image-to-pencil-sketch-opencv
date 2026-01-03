# Image to Pencil Sketch using OpenCV

This project converts an RGB image into a pencil sketch using Python and OpenCV.

## Steps Performed
1. Convert RGB image to grayscale
2. Invert the grayscale image
3. Apply Gaussian Blur
4. Invert the blurred image
5. Apply dodge blending using image division to create a pencil sketch effect

## Technologies Used
- Python
- OpenCV
- NumPy

## How to Run
```bash
pip install -r requirements.txt
python sketch.py
```

## Output
The final output resembles a hand-drawn pencil sketch and is saved inside the `outputs` folder.
