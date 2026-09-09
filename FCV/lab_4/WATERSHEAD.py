import cv2 as cv
import numpy as np

image = cv.imread("/home/laserhammer/LAB/FCV/lab_2/fruits.jpg")

gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

# Binary threshold
_, binary = cv.threshold(
    gray,
    120,
    255,
    cv.THRESH_BINARY
)

# Distance transform
dist = cv.distanceTransform(
    binary,
    cv.DIST_L2,
    5
)

# Find foreground
_, foreground = cv.threshold(
    dist,
    0.5 * dist.max(),
    255,
    0
)

foreground = foreground.astype(np.uint8)

# Connected components
num_labels, markers = cv.connectedComponents(foreground)

# Background
markers = markers + 1

# Unknown region
unknown = cv.subtract(binary, foreground)

markers[unknown == 255] = 0

# Watershed
markers = cv.watershed(image, markers)

# Mark boundaries
image[markers == -1] = [0, 0, 255]

cv.imshow("Watershed", image)

cv.waitKey(0)
cv.destroyAllWindows()