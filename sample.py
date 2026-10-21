
import cv2
import numpy as np
import glob
import os

# Number of inner checkerboard corners
CHECKERBOARD = (6, 9)

# Calibration images folder
image_folder = r"D:\aiml_b\FCV\lab_8\calib_example"
images = glob.glob(os.path.join(image_folder, "*"))

images = [
    f for f in images
    if f.lower().endswith(
        (".jpg", ".jpeg", ".png", ".bmp", ".tif", ".tiff")
    )
]

if len(images) == 0:
    print("No images found! Check the calib_example folder.")
    raise SystemExit

# Corner refinement criteria
criteria = (
    cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER,
    30,
    0.001
)

# 3D coordinates of checkerboard corners
objp = np.zeros(
    (CHECKERBOARD[0] * CHECKERBOARD[1], 3),
    np.float32
)

objp[:, :2] = np.mgrid[
    0:CHECKERBOARD[0],
    0:CHECKERBOARD[1]
].T.reshape(-1, 2)

objpoints = []
imgpoints = []
image_size = None

# Detect checkerboard corners
for filename in images:
    img = cv2.imread(filename)

    if img is None:
        print("Cannot read:", filename)
        continue

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    found, corners = cv2.findChessboardCorners(
        gray, CHECKERBOARD, None
    )

    if found:
        corners2 = cv2.cornerSubPix(
            gray,
            corners,
            (11, 11),
            (-1, -1),
            criteria
        )

        objpoints.append(objp.copy())
        imgpoints.append(corners2)
        image_size = gray.shape[::-1]

        print("Corners detected:", filename)

        display = img.copy()
        cv2.drawChessboardCorners(
            display, CHECKERBOARD, corners2, found
        )
        cv2.imshow("Checkerboard Corners", display)
        cv2.waitKey(200)

    else:
        print("Checkerboard not detected:", filename)

cv2.destroyAllWindows()

# Check whether any checkerboards were detected
if len(objpoints) == 0:
    print("No checkerboards detected. Check the pattern dimensions.")
    raise SystemExit

# Perform camera calibration
ret, K, dist, rvecs, tvecs = cv2.calibrateCamera(
    objpoints,
    imgpoints,
    image_size,
    None,
    None
)

print("\n========== CALIBRATION RESULTS ==========")

print("\nReprojection RMS Error:")
print(ret)

print("\nIntrinsic Matrix K:")
print(K)

print("\nDistortion Coefficients:")
print(dist)

# Calculate matrices for every image
for i in range(len(rvecs)):

    # Convert rotation vector to rotation matrix
    R, _ = cv2.Rodrigues(rvecs[i])

    # Translation vector
    t = tvecs[i]

    # Extrinsic matrix [R | t] (3 x 4)
    extrinsic = np.hstack((R, t))

    # 3D-to-2D projection matrix (3 x 4)
    P_3D = K @ extrinsic

    # 2D planar projection matrix / homography (3 x 3)
    # Valid for points on the checkerboard plane (Z = 0)
    H_2D = K @ np.column_stack((
        R[:, 0],
        R[:, 1],
        t[:, 0]
    ))

    print(f"\n========== IMAGE {i + 1} ==========")

    print("\nRotation Vector:")
    print(rvecs[i])

    print("\nRotation Matrix R:")
    print(R)

    print("\nTranslation Vector t:")
    print(t)

    print("\nExtrinsic Matrix [R | t]:")
    print(extrinsic)

    print("\n2D Planar Projection Matrix H (3 x 3):")
    print(H_2D)

    print("\n3D-to-2D Projection Matrix P (3 x 4):")
    print(P_3D)

# Save calibration results
np.savez(
    "calibration_results.npz",
    camera_matrix=K,
    distortion=dist,
    rotation_vectors=np.array(rvecs),
    translation_vectors=np.array(tvecs),
    reprojection_rms=ret
)

print("\nResults saved to calibration_results.npz")
