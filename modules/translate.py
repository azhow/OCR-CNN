import os
import sys
import cv2
import numpy as np
import from googletrans Translator
import pytesseract

#tradução do texto

def translate(input_string, dest_language):
    translator = Translator()
    return translator.translate(input_string, dest=dest_language, src='auto')

text = pytesseract.image_to_string(cv2.imread(sys.argv[1]))
translated_text = translate(text, 'pt')



