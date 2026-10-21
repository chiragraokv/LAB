import cv2 as cv
import numpy as np
img1 = cv.imread(r'FCV\lab_7\tower1.jpg') 
img2 = cv.imread(r'FCV\lab_7\tower2.jpg') 
sift = cv.SIFT_create()
kp1, des1 = sift.detectAndCompute(img1, None)
kp2, des2 = sift.detectAndCompute(img2, None)
matches = cv.BFMatcher().knnMatch(des1, des2, k=2)
good = [m for m, n in matches if m.distance < 0.75 * n.distance]
src = np.float64([kp1[m.queryIdx].pt for m in good])
dst = np.float64([kp2[m.trainIdx].pt for m in good])
best_H, best_inliers = None, []
for _ in range(1000):
    if len(src) < 4:
        break

    idx = np.random.choice(len(src), 4, replace=False)
    A = []

    for (x, y), (u, v) in zip(src[idx], dst[idx]):
        A += [[-x, -y, -1, 0, 0, 0, u*x, u*y, u],
              [0, 0, 0, -x, -y, -1, v*x, v*y, v]]

    _, _, V = np.linalg.svd(A)
    H = V[-1].reshape(3, 3)

    pts = np.c_[src, np.ones(len(src))]
    proj = (H @ pts.T).T
    valid = np.abs(proj[:, 2]) > 1e-10
    errors = np.full(len(src), np.inf)
    proj[valid] /= proj[valid, 2:3]
    errors[valid] = np.linalg.norm(proj[valid, :2] - dst[valid], axis=1)

    inliers = np.where(errors < 5)[0]

    if len(inliers) > len(best_inliers):
        best_H, best_inliers = H, inliers

# Refine homography using best inliers
if best_H is not None and len(best_inliers) >= 4:
    A = []
    for (x, y), (u, v) in zip(src[best_inliers], dst[best_inliers]):
        A += [[-x, -y, -1, 0, 0, 0, u*x, u*y, u],
              [0, 0, 0, -x, -y, -1, v*x, v*y, v]]

    _, _, V = np.linalg.svd(A)
    H = V[-1].reshape(3, 3)
    H /= H[2, 2]

    print("Homography matrix:\n", H)
    print("Inliers:", len(best_inliers))

    # Warp first image onto second
    result = cv.warpPerspective(
        cv.imread(r'FCV\lab_7\tower1.jpg'), H,
        (cv.imread(r'FCV\lab_7\tower2.jpg').shape[1],
         cv.imread(r'FCV\lab_7\tower2.jpg').shape[0])
    )
    cv.imwrite("result.jpg", result)
