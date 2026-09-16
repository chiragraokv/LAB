import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

image = cv.imread(r"D:\aiml_b\FCV\lab_2\fruits.jpg")
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

sobel_x = cv.Sobel(gray, cv.CV_64F, 1, 0, ksize=3)
sobel_y = cv.Sobel(gray, cv.CV_64F, 0, 1, ksize=3)
magnitude = np.sqrt(sobel_x**2 + sobel_y**2)
sobel_x_vis = cv.convertScaleAbs(sobel_x)
sobel_y_vis = cv.convertScaleAbs(sobel_y)
magnitude_vis = cv.convertScaleAbs(magnitude)
images = [gray, sobel_x_vis, sobel_y_vis, magnitude_vis]
labels = ["Original ", "Sobel X", "Sobel Y", "gradient"]

# 5. Plotting
plt.figure(figsize=(12, 8))
for i in range(len(images)):
    plt.subplot(2, 2, 1 + i)
    plt.imshow(images[i], cmap='gray')
    plt.title(labels[i])
    plt.axis('off')

plt.tight_layout()
plt.show()