import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
image = cv.imread(r"D:\aiml_b\FCV\lab_2\fruits.jpg")
blurred = cv.GaussianBlur(image, (5, 5), 2.0)
amount = 3
sub = image - blurred
sharpened = cv.addWeighted(image,1+ amount, blurred, -amount, 0)
images = [image,blurred,sub,sharpened]
tags = ["original","blurred","subtracted","sharpened"]
plt.figure(figsize=(12,8))
for i in range(len(images)):
    plt.subplot(2,2,1+i)
    im = images[i]
    im = cv.cvtColor(im,cv.COLOR_BGR2RGB)
    plt.imshow(im)
    plt.title(tags[i])
    plt.axis('off')
plt.tight_layout()
plt.show()