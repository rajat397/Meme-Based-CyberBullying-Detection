import cv2
import pytesseract
import os

# Define the path to your dataset
dataset_path = "/home/rajat/Desktop/example"

for image_name in os.listdir(dataset_path):
    if image_name.endswith(".jpg") or image_name.endswith(".jpeg") or image_name.endswith(".png"):  # Adjust the image file extension if needed
        image_path = os.path.join(dataset_path, image_name)
        image = cv2.imread(image_path)

        # Perform OCR
        ocr_text = pytesseract.image_to_string(image, config='--oem 1')

        # Define the path for the OCR file
        ocr_file_path = os.path.splitext(image_path)[0] + ".ocr"

        # Write the OCR output to a file
        with open(ocr_file_path, "w") as ocr_file:
            ocr_file.write(ocr_text)

        print(f"Processed {image_name}. OCR file saved as {ocr_file_path}.")
