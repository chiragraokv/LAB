import cv2 as cv
import numpy as np
from tqdm import tqdm
image = cv.imread("/home/laserhammer/LAB/FCV/lab_2/fruits.jpg")
for i in tqdm(range(100000)):
    image = cv.GaussianBlur(image, (3, 3), 2.0)
    cv.imshow('Original Image', image)
    if cv.waitKey(50) & 0xFF == ord('q'):
            break

pix = image.reshape(-1, 3)

k = 7
iterations = 30

# Random initial centroids
index = np.random.choice(
    pix.shape[0],
    size=k,
    replace=False
)

centroids = pix[index].astype(np.float64)

label = np.zeros(pix.shape[0], dtype=np.int32)

color_palette = np.array([
    [0, 0, 255],       # Red
    [0, 255, 0],       # Green
    [255, 0, 0],       # Blue
    [0, 255, 255],     # Yellow
    [255, 0, 255],     # Magenta
    [255, 255, 0],     # Cyan
    [255, 255, 255],   # White
    [0, 0, 0]          # Black
], dtype=np.uint8)


# -----------------------------
# Create video writer
# -----------------------------

height, width = image.shape[:2]

fourcc = cv.VideoWriter_fourcc(*'mp4v')

video = cv.VideoWriter(
    "kmeans_evolution.mp4",
    fourcc,
    10,                  # FPS
    (width, height)
)


# -----------------------------
# K-means iterations
# -----------------------------
for i in range(300):

    # Calculate distances
    dist = np.linalg.norm(
        pix[:, np.newaxis, :] - centroids,
        axis=2
    )

    # Assign labels
    label = np.argmin(dist, axis=1)

    # Update centroids
    for l in range(k):
        cluster_pixels = pix[label == l]

        if len(cluster_pixels) > 0:
            centroids[l] = np.mean(
                cluster_pixels,
                axis=0
            )

    # Create segmented image
    segmented_image = color_palette[label]
    segmented_image = segmented_image.reshape(image.shape)

    # Display evolution
    cv.imshow("K-Means Evolution", segmented_image)

    # Wait 50 ms between iterations
    if cv.waitKey(50) & 0xFF == ord('q'):
        break

cv.destroyAllWindows()