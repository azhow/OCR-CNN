#!/usr/bin/python3
import cv2
import sys
import os

img = cv2.imread(sys.argv[1])

dst = cv2.GaussianBlur(img, (9, 9), 10)
dst = cv2.addWeighted(img, 1.5, dst, -0.5, 0, img)

cv2.imshow("Sharp", dst)
cv2.waitKey(0)

if not os.path.exists("./../results/"):
    os.mkdir("./../results/")
cv2.imwrite("./../results/sharp.png", dst)
