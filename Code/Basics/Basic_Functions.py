import cv2 as cv

img = cv.imread('Documents\\papagan.jpg')

# Converting to graysacel
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray Image', gray)

# Blur the image
blur = cv.GaussianBlur(img, (3,3), cv.BORDER_DEFAULT)
cv.imshow('Blur Image', blur)

# Edge detection using Canny edge detection algorithm
canny = cv.Canny(img, 125,175)
cv.imshow("Canny", canny)

#Dilating a image
dilated = cv.dilate(canny, (7,7), iterations=2)
cv.imshow("Dilation", dilated)

#Eroding
eroded = cv.erode(dilated, (7,7), iterations=2)
cv.imshow('Eroded', eroded)

# Resize
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resize', resized)

# Cropping
cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)