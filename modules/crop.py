#!/usr/bin/python3
import cv2
import sys
import os
import numpy as np

def mouseHandler(event,x,y,flags,param):
    global im_temp, pts_src

    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(im_temp,(x,y),1,(0,255,255),1,cv2.LINE_AA)
        cv2.imshow("Image", im_temp)
        if len(pts_src) < 2:
        	pts_src = np.append(pts_src,[(x,y)],axis=0)


# Read in the image.
im_src = cv2.imread(sys.argv[1])

# Create a window
cv2.namedWindow("Image", 1)

im_temp = im_src
pts_src = np.empty((0,2))

cv2.setMouseCallback("Image",mouseHandler)

cv2.imshow("Image", im_temp)
cv2.waitKey(0)

crop = im_src[int(pts_src[0][1]):int(pts_src[1][1]), int(pts_src[0][0]):int(pts_src[1][0])]

cv2.imshow("crop", crop)
cv2.waitKey(0)

if not os.path.exists("./../results/"):
    os.mkdir("./../results/")

cv2.imwrite("./../results/crop.png", crop)
