#!/usr/bin/python3
import numpy
import sys
import os
import cv2

img = cv2.imread(sys.argv[1])

dst = cv2.fastNlMeansDenoisingColored(img, None, 10, 10, 7, 21)

if not os.path.exists("./../results/"):
    os.mkdir("./../results/")

cv2.imwrite("./../results/denoise.png", dst)
