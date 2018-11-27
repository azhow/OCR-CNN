#!/usr/bin/python3
import numpy
import sys
import cv2

img = cv2.imread(sys.argv[1])

dst = cv2.fastNlMeansDenoisingColored(img, None, 10, 10, 7, 21)

cv2.imwrite("denoise.png", dst)
