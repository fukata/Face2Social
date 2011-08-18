#! /usr/bin/env python

import cv
import sys

FACE_XML = "data/haarcascade_frontalface_default.xml"
LOAD_IMG = sys.argv[1]
OUT_IMG = "out.jpg"

hc = cv.Load(FACE_XML)
img = cv.LoadImage(LOAD_IMG, cv.CV_LOAD_IMAGE_UNCHANGED)
faces = cv.HaarDetectObjects(img, hc, cv.CreateMemStorage())
for (x,y,w,h),n in faces:
    cv.Rectangle(img, (x,y), (x+w,y+h), cv.RGB(255, 0, 0))
cv.SaveImage(OUT_IMG, img)
