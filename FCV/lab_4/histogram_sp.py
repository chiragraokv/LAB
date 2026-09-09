import cv2 as cv
import numpy as np
from scipy.stats import norm


def histogram_sp(image,reference):
    image_hist = np.histogram(image.flatten(),256,[0,256])[0]
    reference_hist = np.histogram(reference.flatten(),256,[0,256])[0]

    cdf_image = image_hist.cumsum()
    cdf_reference = reference_hist.cumsum()
    intensities = np.arange(256)

    # Desired Gaussian distribution
    mean = 128
    std = 40

    gaussian_cdf = norm.cdf(
        intensities,
        loc=mean,
        scale=std
    )

    # Normalize if necessary
    # cdf_reference = gaussian_cdf / gaussian_cdf[-1]

    cdf_image = cdf_image / cdf_image[-1]
    cdf_reference = cdf_reference / cdf_reference[-1]

    mapping = np.zeros(256, dtype=np.uint8)
    for i in range(256):
        diff = np.abs(cdf_image[i] - cdf_reference)
        mapping[i] = np.argmin(diff)
    print(mapping)
    image_equalized = mapping[reference]

    return image_equalized

im = cv.imread('/home/laserhammer/LAB/FCV/lab_2/gamma_10.png', cv.IMREAD_GRAYSCALE)
ref = cv.imread('/home/laserhammer/LAB/FCV/lab_2/gamma_5.png', cv.IMREAD_GRAYSCALE)
cv.imshow('Original Image', im)
cv.imshow('Reference Image', ref)
result = histogram_sp(im, ref)
cv.imshow('Result Image', result)
cv.waitKey(0)   
cv.destroyAllWindows()