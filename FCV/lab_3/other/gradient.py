import cv2 as cv
import numpy as np
image = cv.imread("/home/laserhammer/LAB/FCV/lab_2/fruits.jpg")
sob1 = cv.Sobel(image,cv.CV_64F,1,0,ksize=5)
sob2 = cv.Sobel(image,cv.CV_64F,0,1,ksize=5)
magnitude = np.sqrt(sob1**2 + sob2**2)

cv.imshow('Original Image', image)
cv.imshow('Sobel X', sob1)
cv.imshow('Sobel Y', sob2)
magnitude = np.sqrt(sob1**2 + sob2**2)

magnitude = cv.normalize(
    magnitude,
    None,
    0,
    255,
    cv.NORM_MINMAX
)

magnitude = magnitude.astype(np.uint8)

cv.imshow('Magnitude', magnitude)
cv.waitKey(0)

cv.destroyAllWindows()
