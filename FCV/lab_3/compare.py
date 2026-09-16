import cv2 as cv 
import numpy as np 
import matplotlib.pyplot as plt

image = cv.imread(r"D:\aiml_b\FCV\lab_2\fruits.jpg") 

box = cv.boxFilter(image, -1, (91, 91)) 
gauss = cv.GaussianBlur(image, (91, 91), 4) 
edge = cv.Laplacian(gauss, -1) 
median = cv.medianBlur(image, 99) 

sobel_64f = cv.Sobel(image, cv.CV_64F, 1, 0)
sobel = cv.convertScaleAbs(sobel_64f) 

images = [image, box, gauss, edge, median, sobel]
titles = ['Original Image', 'Box Filter', 'Gaussian Blur', 'Laplacian Edge', 'Median Blur', 'Sobel Filter']
plt.figure(figsize=(12, 8))

for i in range(6):
    plt.subplot(2, 3, i + 1)
    curr_img = images[i]
    curr_img = cv.cvtColor(curr_img, cv.COLOR_BGR2RGB)
    plt.imshow(curr_img)
    plt.title(titles[i])
    plt.axis('off')  

plt.tight_layout()
plt.show()