# Midsem TODO
## lab 2
- [x] Gamma correction: image = 255* ((image/255)**gamma)
- [x] Negative of image (bitwise_not)
- [x] Log transformation: Log(1/(1+max(image))) * log(1+image)
- [ ] piecewise_linear: scale image to different scale linearly
## lab 3
- [x] Gaussian blur, box filter, laplacian
- [x] Edge detection: image - blur
- [ ] gradient of an image: sobel filter: understand this
- [ ] correlation and convolution
- [ ] sharpened = cv.addWeighted(image, amount, blurred, -amount, 0)
