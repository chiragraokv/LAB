import cv2 as cv
import numpy as np
img = cv.imread(r"D:\aiml_b\FCV\line.jpg")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
gray = np.float32(gray)
dst = cv.cornerHarris(gray, blockSize=2, ksize=3, k=0.04)
dst = cv.dilate(dst, None)
img[dst > 0.01 * dst.max()] = [0, 0, 255]
cv.imshow('Harris Corner Detection', img)
cv.waitKey(0)
cv.destroyAllWindows()