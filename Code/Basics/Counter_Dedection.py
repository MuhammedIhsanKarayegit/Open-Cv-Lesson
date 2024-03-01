import cv2 as cv
import numpy as np

img = cv.imread('Documents\\jhon.jpg')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
canny = cv.Canny(gray, 125, 175)

cv.imshow('Canny', canny)

contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)

print(f'{len(contours)} contour(s) found!')

cv.waitKey(0)