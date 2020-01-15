import pytesseract as tess
# TODO: get a basic ocr script up and running
s = tess.image_to_string("test.jpg")
print(s)
