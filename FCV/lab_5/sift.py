import cv2 as cv
import numpy as np
from cv2 import SIFT_create
import matplotlib.pyplot as plt
img = cv.imread(r"D:\aiml_b\FCV\play.png")
img = cv.cvtColor(img,cv.COLOR_BGR2RGB)
rt = cv.rotate(img, cv.ROTATE_90_CLOCKWISE)
# img = cv.resize(img,(10000,10000))

def do_sift(img):
    sift = SIFT_create()
    keypoints, dis = sift.detectAndCompute(img,None)
    keypoints_with_size = np.copy(img) 
    print(len(keypoints))
    cv.drawKeypoints(img, keypoints,  keypoints_with_size, color = (255, 0, 0), 
    flags = cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS) 
    plt.imshow(keypoints_with_size), 
    plt.show() 

do_sift(img)
do_sift(rt)
do_sift(cv.resize(img,(190,400)))