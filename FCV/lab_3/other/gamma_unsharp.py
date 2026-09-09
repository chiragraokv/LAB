import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

image = cv.imread("/home/laserhammer/LAB/FCV/lab_2/fruits.jpg",cv.IMREAD_GRAYSCALE)
#unsharp mask
blurred = cv.GaussianBlur(image, (5, 5), 2.0)
amount = 1.5
unsharp = cv.addWeighted(image, 1 + amount, blurred, -amount, 0)
norm = unsharp / 255
gamma = 1.2
norm = np.array(255 * (norm ** gamma), dtype='uint8')
image = cv.cvtColor(image, cv.COLOR_BGR2RGB)
plt.figure(figsize=(12, 8))
plt.subplot(1, 2, 1)
plt.imshow(image)
plt.title('Original Image')
plt.axis('off')
plt.subplot(1, 2, 2)
plt.imshow(norm, cmap='gray')
plt.title('Unsharp Mask with Gamma Correction')
plt.axis('off')
plt.tight_layout()
plt.show()