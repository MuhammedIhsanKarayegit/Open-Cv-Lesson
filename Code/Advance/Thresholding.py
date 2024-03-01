import cv2 as cv

img = cv.imread('Documents\\papagan.jpg')
cv.imshow("Original Image", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Grayscaled Image', gray)

# Simple Tresholding
threshold, thresh  = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
cv.imshow('Simple Threshold',thresh )

threshold, thresh_inv  = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow('Simple Threshold Inverse', thresh_inv)

# Adaptive Tresholding
adaptive_thesh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 3)
cv.imshow('Adaptive Thresholding', adaptive_thesh)

cv.waitKey(0)