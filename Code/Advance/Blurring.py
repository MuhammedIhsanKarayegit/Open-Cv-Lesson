import cv2 as cv

img = cv.imread('Documents\\papagan.jpg')
cv.imshow('Orijinal', img)

# Averaging
average = cv.blur(img,(3,3))
cv.imshow("Average Image", average)

# Guassian Blur
gaussian_blurred = cv.GaussianBlur(img,(5,5),0)
cv.imshow("Guassian Blur", gaussian_blurred)

# Median Blur
median = cv.medianBlur(img, 9)
cv.imshow("Median Blur", median)

# Bilateral
bilat = cv.bilateralFilter(img, d=25, sigmaColor=5, sigmaSpace=75)
cv.imshow("Bilateral Filtering", bilat)

cv.waitKey(0)