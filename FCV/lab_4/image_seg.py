import cv2 as cv
import numpy as np
img = cv.imread(r"D:\aiml_b\FCV\house.jpg")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
_, binary = cv.threshold(gray, 127, 255, cv.THRESH_BINARY)
kernel = np.ones((5, 5), np.uint8)
opening = cv.morphologyEx(binary, cv.MORPH_OPEN, kernel)
closing = cv.morphologyEx(binary, cv.MORPH_CLOSE, kernel)
cv.imshow("Original", img)
cv.imshow("Opening", opening)
cv.imshow("Closing", closing)
cv.waitKey(0)
cv.destroyAllWindows()
