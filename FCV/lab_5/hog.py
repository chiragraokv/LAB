import numpy as np
from scipy.ndimage import maximum_filter
import cv2 as cv

# ==========================================
# CORE HOG DESCRIPTOR IMPLEMENTATION
# ==========================================
def compute_hog_descriptor(img_gray, cell_size=8, bin_size=9):
    """Computes a simplified HOG descriptor for a given image region."""
    dy, dx = np.gradient(img_gray.astype(float))
    magnitude = np.sqrt(dx**2 + dy**2)
    orientation = np.arctan2(dy, dx) * (180 / np.pi) % 180  # Unsigned gradients (0-180)
    
    h, w = img_gray.shape
    num_cells_y = h // cell_size
    num_cells_x = w // cell_size
    
    histograms = np.zeros((num_cells_y, num_cells_x, bin_size))
    for cy in range(num_cells_y):
        for cx in range(num_cells_x):
            y_start, x_start = cy * cell_size, cx * cell_size
            m_patch = magnitude[y_start:y_start+cell_size, x_start:x_start+cell_size]
            o_patch = orientation[y_start:y_start+cell_size, x_start:x_start+cell_size]
            
            counts, _ = np.histogram(o_patch, bins=bin_size, range=(0, 180), weights=m_patch)
            histograms[cy, cx, :] = counts
            
    feature_vector = histograms.flatten()
    norm = np.linalg.norm(feature_vector)
    return feature_vector / norm if norm > 0 else feature_vector

# =========================================================
# FIX #1: LOAD A REAL HUMAN CROP AS THE REFERENCE
# =========================================================
# Step 1: Create or find an image snippet that ONLY contains a clean human figure silhouette.
# Load it, grayscale it, and forcibly resize it to 64x128.
ref_img_raw = cv.imread(r"D:\aiml_b\FCV\lab_5\images (1).jpg", cv.IMREAD_GRAYSCALE)

if ref_img_raw is None:
    print("Warning: Reference human image not found! Creating a placeholder layout instead.")
    # Fallback placeholder: drawing a crude white box silhouette on a black background instead of using random noise
    ref_human_img = np.zeros((128, 64), dtype=np.uint8)
    cv.rectangle(ref_human_img, (16, 20), (48, 110), 255, -1)
else:
    ref_human_img = cv.resize(ref_img_raw, (64, 128))

ref_human_hog = compute_hog_descriptor(ref_human_img)

# ==========================================
# SLIDING WINDOW RUNNER
# ==========================================
def detect_humans(test_image, ref_hog, win_shape=(128, 64), stride=16, threshold=0.45):
    h, w = test_image.shape
    win_h, win_x = win_shape
    detected_windows = []
    
    for y in range(0, h - win_h + 1, stride):
        for x in range(0, w - win_x + 1, stride):
            window = test_image[y:y+win_h, x:x+win_x]
            window_hog = compute_hog_descriptor(window)   
            similarity = np.dot(window_hog, ref_hog)
            
            if similarity >= threshold:
                detected_windows.append([x, y, x + win_x, y + win_h, similarity])
                
    return np.array(detected_windows)

# ==========================================
# FIX #2: CLEANED NON-MAXIMUM SUPPRESSION
# ==========================================
def non_max_suppression(boxes, overlap_thresh=0.3):
    if len(boxes) == 0: return []
    
    boxes = np.array(boxes)
    boxes = boxes[np.argsort(boxes[:, 4])[::-1]]
    pick = []
    
    x1, y1, x2, y2 = boxes[:, 0], boxes[:, 1], boxes[:, 2], boxes[:, 3]
    area = (x2 - x1) * (y2 - y1)
    idxs = np.arange(len(boxes))
    
    while len(idxs) > 0:
        last = idxs[0]
        pick.append(last)
        
        xx1 = np.maximum(x1[last], x1[idxs[1:]])
        yy1 = np.maximum(y1[last], y1[idxs[1:]])
        xx2 = np.minimum(x2[last], x2[idxs[1:]])
        yy2 = np.minimum(y2[last], y2[idxs[1:]])
        
        w = np.maximum(0, xx2 - xx1)
        h = np.maximum(0, yy2 - yy1)
        overlap = (w * h) / area[idxs[1:]]
        
        # Fixed list step alignment
        idxs = idxs[np.where(overlap <= overlap_thresh)[0] + 1]
        
    return boxes[pick]

# ==========================================
# TEST AND VISUALIZE PIPELINE
# ==========================================
scene_color = cv.imread(r"D:\aiml_b\FCV\lab_5\images.jpg")
if scene_color is None:
    raise FileNotFoundError("Could not find your main target scene image path.")

scene_img = cv.cvtColor(scene_color, cv.COLOR_BGR2GRAY)

# Lowered threshold slightly because a handmade basic HOG lacks linear SVM boundary weighting
raw_hits = detect_humans(scene_img, ref_human_hog, threshold=0.50)
final_detections = non_max_suppression(raw_hits)

print(f"Total raw detection windows found: {len(raw_hits)}")
print(f"Final windows preserved after NMS filtering: {len(final_detections)}")

# Draw the resulting tracking boxes on the canvas screen output
for box in final_detections:
    x1, y1, x2, y2, score = box
    cv.rectangle(scene_color, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
    cv.putText(scene_color, f"{score:.2f}", (int(x1), int(y1)-5), cv.FONT_HERSHEY_SIMPLEX, 0.4, (0, 255, 0), 1)

cv.imshow("Human Detection Output", scene_color)
cv.waitKey(0)
cv.destroyAllWindows()
