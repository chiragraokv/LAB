import cv2 as cv
import numpy as np
img = cv.imread(r"D:\aiml_b\FCV\line.jpg")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

edges = cv.Canny(gray, 50, 150)
lines = cv.HoughLines(edges,1, 10*np.pi / 180, 100)

if lines is not None:
    for line in lines:
        rho, theta = line[0]
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a * rho
        y0 = b * rho
        x1 = int(x0 + 1000 * (-b))
        y1 = int(y0 + 1000 * a)
        x2 = int(x0 - 1000 * (-b))
        y2 = int(y0 - 1000 * a)

        cv.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)
cv.imshow("Edges", edges)
cv.imshow("Detected Lines", img)

cv.waitKey(0)
cv.destroyAllWindows()
