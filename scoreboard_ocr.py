try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract


def scoreboard_ocr(filename):
    """
    This function will handle the core OCR processing of images.
    """
    # Pillow's Image class to open the image
    image_for_ocr = Image.open('images/sc2.jpg')
    new_size = tuple(20*x for x in image_for_ocr.size)
    image_for_ocr = image_for_ocr.resize(new_size, Image.ANTIALIAS)

    # pytesseract to detect the string in the image
    text = pytesseract.image_to_string(image_for_ocr)

    return text

print(scoreboard_ocr('images/testimage.jpg'))