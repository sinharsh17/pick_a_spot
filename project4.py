import cv2
import pytesseract
import numpy as np

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
cascade = cv2.CascadeClassifier(r'C:\Users\sinha\OneDrive\Desktop\sem 5\assignment\project\haarcascade_russian_plate_number.xml')

states = {
    # ... (your state abbreviations and names)
}

def capture_image_from_camera():
    cap = cv2.VideoCapture(0)  # 0 represents the default camera (you can change it if you have multiple cameras)
    
    if not cap.isOpened():
        print("Error: Could not open camera.")
        return
    
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Couldn't capture frame.")
            break
        
        cv2.imshow("Camera Feed", frame)
        
        # Press 'q' to capture the image and exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            image_filename = "captured_image.jpg"
            cv2.imwrite(image_filename, frame)
            break
    
    cap.release()
    cv2.destroyAllWindows()
    
    if 'image_filename' in locals():
        extract_num(image_filename)

def extract_num(img_name):
    # Your existing code for processing and extracting license plate goes here
    pass

# Example usage
if __name__ == "__main__":
    capture_image_from_camera()
