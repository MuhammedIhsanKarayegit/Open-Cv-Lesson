import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3))
cv.imshow( "Blank", blank)

# Paint the image a certain color
blank[:] = 0, 255, 0
cv.imshow("Green", blank)

# Draw rectangle
cv.rectangle(blank, (0,0), (50,250), (0,250,0), thickness=2)
cv.imshow('Rectangle', blank)

# Draw a circle
cv.circle(blank, (250,250), 40,(0,0,255),thickness=3)
cv.imshow('Circle', blank)

# Draw a line
cv.line(blank, (0,0), (250,250), (0, 255,0), thickness=2)
cv.line(blank, (0,500), (250,250), (0, 255,0), thickness=2)
cv.line(blank, (500,0), (250,250), (0, 255,0), thickness=2)
cv.line(blank, (500,500), (250,250), (0, 255,0), thickness=2)
cv.imshow('Line',blank)

cv.circle(blank, (250,250), 60,(0,0,255),thickness=3)
cv.imshow('Circle', blank)


# Write a text
cv.putText(blank, 'Hello', (225,225), cv.FONT_HERSHEY_TRIPLEX, 1.0, (255,255,255),2)
cv.imshow('Text', blank)


cv.waitKey(0)



