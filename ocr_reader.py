# ocr_reader.py
from PIL import Image
import pytesseract

# For Windows (update path if needed)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def extract_text_from_image(image_path):
    """
    Extracts text from an uploaded image using OCR.
    """
    img = Image.open(image_path)
    extracted_text = pytesseract.image_to_string(img)
    return extracted_text.strip()
