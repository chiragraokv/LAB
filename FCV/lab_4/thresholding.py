import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

image = cv.imread("/home/laserhammer/LAB/FCV/lab_2/fruits.jpg", cv.IMREAD_GRAYSCALE)
_, thr1 = cv.threshold(image,120,255,cv.THRESH_BINARY)
_, thr2 = cv.threshold(image,120,255,cv.THRESH_BINARY_INV)
_, thr3 = cv.threshold(image,120,255,cv.THRESH_TRUNC)
_, thr4 = cv.threshold(image,120,255,cv.THRESH_TOZERO)
_, thr5 = cv.threshold(image,120,255,cv.THRESH_TRIANGLE)
images = [image,thr1,thr2,thr3,thr4,thr5]
tags = ["original","THRESH_BINARY","THRESH_BINARY_INV","THRESH_TRUNC","THRESH_TOZERO","THRESH_TRIANGLE"]
plt.figure(figsize=(12,8))
for i in range(len(images)):
    plt.subplot(2,3,1+i)
    im = images[i]
    im = cv.cvtColor(im,cv.COLOR_BGR2RGB)
    plt.imshow(im)
    plt.title(tags[i])
    plt.axis("off")
plt.tight_layout()
plt.show()
