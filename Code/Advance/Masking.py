# Maskeleme işlemlerini tam olarak gerçekleştirmedin. ALdığın hatalar sonucunda işleme devam edemedim. Ama mantık olarak ne yapmak
#istediğimizi anladım ilerleyen dönemlerde tekrardan dönmek ümidiyle


import cv2 as cv
import numpy as np

img = cv.imread('Documents\\boston.jpg')
cv.imshow('Original Image', img)

blank = np.zeros(img.shape[:2])
cv.imshow('Blank', blank)

masking = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
cv.imshow('Mask', masking)

masked_img = cv.bitwise_and(img, img, mask = masking)
cv.imshow('Masked Image', masked_img)

cv.waitKey(0)

