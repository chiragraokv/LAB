import cv2 as cv
import matplotlib.pyplot as plt 
from cv2 import SIFT_create 
 
# read images 
img1 = cv.imread(r'FCV\lab_7\tower1.jpg') 
img2 = cv.imread(r'FCV\lab_7\tower2.jpg') 
img2 = cv.resize(img2, (750, 1200)) 
img1 = cv.cvtColor(img1, cv.COLOR_BGR2RGB) 
img2 = cv.cvtColor(img2, cv.COLOR_BGR2RGB) 
sift = SIFT_create() 
keypoints_1, descriptors_1 = sift.detectAndCompute(img1, None) 
keypoints_2, descriptors_2 = sift.detectAndCompute(img2, None) 
bf = cv.BFMatcher(cv.NORM_L1, crossCheck=True) 
matches = bf.match(descriptors_1, descriptors_2) 
matches = sorted(matches, key=lambda x: x.distance) 
line_color = (255, 0, 0) 
img3 = cv.drawMatches(img1, keypoints_1, img2, keypoints_2, matches[:150], 
img2, matchColor=line_color, singlePointColor=line_color, flags=2) 
plt.imshow(img3), 
plt.show() 
