import numpy as np
from scipy.ndimage import gaussian_filter, maximum_filter
import cv2 as cv
import matplotlib.pyplot as plt

    
def minimal_sift(img, num_features=50):
    dy, dx = np.gradient(img.astype(float))
    magnitude = np.sqrt(dx**2 + dy**2)
    orientation = np.arctan2(dy, dx) * (180 / np.pi) % 360
    local_max = maximum_filter(magnitude, size=5) == magnitude
    y_coords, x_coords = np.where(local_max & (magnitude > np.mean(magnitude) * 2))
    keypoints = []
    for y, x in zip(y_coords, x_coords):
        if 8 < y < img.shape[0]-8 and 8 < x < img.shape[1]-8:
            patch_mag = magnitude[y-4:y+5, x-4:x+5]
            patch_ori = orientation[y-4:y+5, x-4:x+5]
            hist, bins = np.histogram(patch_ori, bins=8, weights=patch_mag, range=(0,360))
            dominant_angle = bins[np.argmax(hist)]
            scale_radius = max(2.0, np.std(patch_mag) * 10) 
            keypoints.append({'pt': (x, y), 'size': scale_radius, 'angle': dominant_angle})
            keypoints = sorted(keypoints, key=lambda k: magnitude[int(k['pt'][1]), int(k['pt'][0])], reverse=True)
    return keypoints[:num_features]
def sift(img):
    features = minimal_sift(img, num_features=30)
    plt.figure(figsize=(8, 8))
    plt.imshow(img, cmap='gray')

    for kp in features:
        x, y = kp['pt']
        r = kp['size']
        angle_rad = np.radians(kp['angle'])
        circle = plt.Circle((x, y), r, color='cyan', fill=False, linewidth=1.5)
        plt.gca().add_patch(circle)
        line_x = x + r * np.cos(angle_rad)
        line_y = y + r * np.sin(angle_rad)
        plt.plot([x, line_x], [y, line_y], color='yellow', linewidth=1.5)
        plt.plot(x, y, 'r.', markersize=5)

    plt.title("Minimal SIFT from Scratch (Circles & Lines)")
    plt.axis('off')
    plt.show()
img = cv.rotate(cv.imread(r"D:\aiml_b\FCV\cat.jpg", cv.IMREAD_GRAYSCALE),cv.ROTATE_90_CLOCKWISE)
sift(img)
sift(cv.rotate(img,cv.ROTATE_90_COUNTERCLOCKWISE))
sift(cv.resize(img,(190,400)))

