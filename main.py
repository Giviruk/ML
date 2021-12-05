import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'D:\tesseract\tesseract.exe'
img = cv2.imread('11111.png')
img = cv2.resize(img, None, fx=9, fy=9)  # Увеличение изображения в 9 раз

# Распознавание, допустимы только цифры
balance = pytesseract.image_to_string(img, config='outputbase digits')

print(balance)
