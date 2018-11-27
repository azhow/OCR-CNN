#!/usr/bin/python3
import cv2
import sys

img = cv2.imread(sys.argv[1])

dst = cv2.GaussianBlur(img, (9, 9), 10)
dst = cv2.addWeighted(img, 1.5, dst, -0.5, 0, img)

cv2.imshow("Sharp", dst)
cv2.waitKey(0)

cv2.imwrite("sharp.png", dst)
