# Write a program to detect edges in a image. 
import cv2 as cv
import numpy as np
image = cv.imread(r"D:\aiml_b\FCV\lab_2\fruits.jpg")
box = cv.boxFilter(image,-1,(9,9))
gauss = cv.GaussianBlur(image,(9,9),1)
edge = cv.Laplacian(gauss,-1) 
sub_g = image - gauss
sub_b = image - box
cv.imshow("box",sub_b)
cv.imshow("gauss",sub_g)
cv.imshow("Laplacian Filter",100*edge)
cv.waitKey(0)
cv.destroyAllWindows()

# REGION GROWING 
# K MEANS CLUSTERING
# EDGE BASED SEG USING CANNY  SOBEL LAPLACIAN PREWIT