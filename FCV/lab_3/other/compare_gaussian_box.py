import cv2 as cv
import numpy as np

image = cv.imread(r"D:\aiml_b\FCV\lab_2\fruits.jpg")
box = cv.boxFilter(image,-1,(45,45))
gauss = cv.GaussianBlur(image,(5,5),3)
print("\nGradient Magnitude:")
cv.imshow("box",box)
cv.imshow("gauss",gauss)
cv.waitKey(0)
cv.destroyAllWindows()