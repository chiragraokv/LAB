import numpy  as np
import cv2 as cv
import matplotlib.pyplot as plt

# k means clustering based on colour
images = []
ks = []
for k in range(2,8):                                                                      
    iterations = 10
    image = cv.imread("/home/laserhammer/LAB/FCV/lab_2/fruits.jpg")
    image = cv.GaussianBlur(image,(3,3),2)
    image= image/ 255
    color_palette = np.array([
        [0, 0, 255],     # Red
        [0, 255, 0],     # Green
        [255, 0, 0],     # Blue
        [0, 255, 255],   # Yellow
        [255, 0, 255],   # Magenta
        [255, 255, 0],   # Cyan
        [255, 255, 255], # White
        [0, 0, 0]        # Black
    ], dtype=np.uint8)
    if image.ndim == 3:
        h, w, c = image.shape
        pixels = image.reshape(-1, c) 
    else:
        h, w = image.shape
        pixels = image.reshape(-1, 1) 

    random_indices = np.random.choice(pixels.shape[0], size=k, replace=False)
    if image.ndim == 3:
        
        h, w, c = image.shape
        pixels = image.reshape(-1, c)  
    else:
        h, w = image.shape
        pixels = image.reshape(-1, 1)
    centroids = pixels[random_indices]
    for i in range(iterations):
        distances = np.linalg.norm(pixels[:, np.newaxis, :] - centroids, axis=2)  
        labels = np.argmin(distances, axis=1) 
        label_image = labels.reshape(h, w)
        for k_idx in range(len(centroids)):                                                                                            
            if np.any(labels == k_idx): 
                centroids[k_idx] = np.mean(pixels[labels == k_idx], axis=0)

        k_max = len(centroids) - 1
    scaled_labels = (label_image * (255.0 / k_max)).astype(np.uint8)
    color_segmented_image = color_palette[label_image]
    images.append(color_segmented_image)
    ks.append(k)
    print(f"k:{k}")
plt.figure(figsize=(12,8))
for i in range(len(images)):
    plt.subplot(2,3,1+i)
    im = images[i]
    im = cv.cvtColor(im,cv.COLOR_BGR2RGB)
    plt.imshow(im)
    plt.title(f"{ks[i]}")
    plt.axis("off")
plt.tight_layout()
plt.show()

        