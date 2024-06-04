import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
# Load the image
image = cv2.imread(r"C:\Users\sinha\OneDrive\Desktop\sem 5\python\captured_image.jpg")

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur to reduce noise (optional)
blur_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

# Use edge detection (Canny) to find the contours
edges = cv2.Canny(blur_image, 50, 150)

# Find contours in the edges
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Sort contours based on their area, and get the largest contour
contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]

number_plate_roi = None

# Loop through the potential contours to find the number plate region
for contour in contours:
    perimeter = cv2.arcLength(contour, True)
    approx = cv2.approxPolyDP(contour, 0.02 * perimeter, True)

    if len(approx) == 4:  # Assuming number plate has four corners
        x, y, w, h = cv2.boundingRect(contour)
        number_plate_roi = image[y:y+h, x:x+w]
        break

if number_plate_roi is not None:
    # Perform OCR on the ROI
    gray_roi = cv2.cvtColor(number_plate_roi, cv2.COLOR_BGR2GRAY)
    custom_config = r'--oem 3 --psm 6'  # Tesseract configuration options
    plate_text = pytesseract.image_to_string(gray_roi, config=custom_config)

    # Remove unwanted characters from the extracted text (if required)
    cleaned_plate_text = "".join(c for c in plate_text if c.isalnum())

    print("Extracted Number Plate:", cleaned_plate_text)
else:
    print("Number plate region not found.")
