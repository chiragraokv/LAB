#5. Implement Canny edge detection algorithm. 
import cv2 as cv
import numpy as np
image = cv.imread(r"D:\aiml_b\FCV\lab_2\fruits.jpg")
edge = cv.Canny(image,200,250)

cv.imshow("canny",edge)
cv.imshow("original",image)
cv.waitKey(0)
cv.destroyAllWindows()