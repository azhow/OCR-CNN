#!/usr/bin/python3

import os
import sys
import cv2
import numpy as np

img = cv2.imread(sys.argv[1])

clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
cl1 = clahe.apply(img)

cv2.imshow("image", cl1)
if not os.path.exists("./../results/"):
    os.mkdir("./../results/")

cv2.imwrite("./../results/clahe.png", cl1)
cv2.waitKey(0)
