import cv2 as cv

image = cv.imread('/home/laserhammer/LAB/FCV/lab_2/gamma_10.png')
blur = cv.GaussianBlur(image, (5, 5), 2.0)
a = 1.5 
unsharp = cv.addWeighted(image, a, blur, -a, 0)
cv.imshow('Original Image', image)
cv.imshow('Unsharp Image', unsharp)
cv.waitKey(0)
cv.destroyAllWindows()