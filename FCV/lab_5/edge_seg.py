import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
# Edge-based segmentation:
# Detecting and tracing object boundaries using edge detection
# algorithms like Canny, Sobel, Laplacian and prewitt

import numpy as np
import cv2 as cv

image = cv.imread(r"D:\aiml_b\FCV\house.jpg")  
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
gray = cv.GaussianBlur(gray, (3, 3), 0)
canny = cv.Canny(gray, 90, 200)
sobel_x = cv.Sobel(gray, cv.CV_64F, 1, 0, ksize=3)
sobel_y = cv.Sobel(gray, cv.CV_64F, 0, 1, ksize=3)
sobel_mag = cv.magnitude(sobel_x, sobel_y)
sobel = cv.convertScaleAbs(sobel_mag)  # Convert back to uint8
laplacian_raw = cv.Laplacian(gray, cv.CV_64F)
laplacian = cv.convertScaleAbs(laplacian_raw)
canny_bgr = cv.cvtColor(canny, cv.COLOR_GRAY2BGR)
sobel_bgr = cv.cvtColor(sobel, cv.COLOR_GRAY2BGR)
laplacian_bgr = cv.cvtColor(laplacian, cv.COLOR_GRAY2BGR)
prewitt_kernel_x = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]], dtype=np.float32)
prewitt_kernel_y = np.array([[-1, -1, -1], [0, 0, 0], [1, 1, 1]], dtype=np.float32)
prewitt_x = cv.filter2D(gray, cv.CV_64F, prewitt_kernel_x)
prewitt_y = cv.filter2D(gray, cv.CV_64F, prewitt_kernel_y)
prewitt = cv.convertScaleAbs(cv.magnitude(prewitt_x, prewitt_y))
prewitt_bgr = cv.cvtColor(prewitt, cv.COLOR_GRAY2BGR)
images = [canny_bgr, sobel_bgr, laplacian_bgr, prewitt_bgr]
tags = ["canny", "sobel", "laplacian", "prewitt"]

plt.figure(figsize=(12,8))

for i in range(len(images)):
    plt.subplot(2,2,1+i)
    im = images[i]
    im = cv.cvtColor(im,cv.COLOR_BGR2RGB)
    plt.imshow(im)
    plt.title(tags[i])
    plt.axis("off")
plt.tight_layout()
plt.show()

 # thresholding using adaptive thresholdig /
 # edge based segmentation roberts sobel laplacian and prewitt /
 # Region based segmenetaion: Assigning pizels to different regions
 # clusering segent an image into K color based regions using k means clustering algo /
 