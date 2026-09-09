import cv2 as cv
import numpy as np

image = cv.imread("/home/laserhammer/LAB/FCV/lab_2/fruits.jpg")

gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

h, w = gray.shape

# Seed point
seed_x = w // 2
seed_y = h // 2

threshold = 20

# Region mask
region = np.zeros((h, w), dtype=np.uint8)

# Queue
queue = [(seed_y, seed_x)]

region[seed_y, seed_x] = 255

seed_value = int(gray[seed_y, seed_x])

while queue:

    y, x = queue.pop(0)

    # 4-connected neighbours
    neighbours = [
        (y - 1, x),
        (y + 1, x),
        (y, x - 1),
        (y, x + 1)
    ]

    for ny, nx in neighbours:

        if ny < 0 or ny >= h or nx < 0 or nx >= w:
            continue

        if region[ny, nx] == 255:
            continue

        # Similarity condition
        if abs(int(gray[ny, nx]) - seed_value) <= threshold:

            region[ny, nx] = 255
            queue.append((ny, nx))

cv.imshow("Original", image)
cv.imshow("Region Growing", region)

cv.waitKey(0)
cv.destroyAllWindows()