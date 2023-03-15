import numpy as np
import pytesseract
import cv2
from PIL import ImageGrab, Image

def imToString():

# Path of tesseract executable
        pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

        img = Image.open("test.png")
        # ImageGrab-To capture the screen image in a loop. 
        # Bbox used to capture a specific area.
        cap = ImageGrab.grab(bbox =(700, 300, 1400, 900))

        # Converted the image to monochrome for it to be easily 
        # read by the OCR and obtained the output String.
        tesstr = pytesseract.image_to_string(
        cv2.cvtColor(np.array(cap), cv2.COLOR_BGR2GRAY), 
        lang ='eng')
        
        img = cv2.imread("test.png", cv2.IMREAD_COLOR)
        cv2.rectangle(img, (700, 300), (1400, 900), (255,0,0), 2)
        cv2.imwrite("lined.png", img)
        print(tesstr)

imToString()