try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def number_scan():
    a = pytesseract.image_to_string(Image.open('num.jpg'))
    return a