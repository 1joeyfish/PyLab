import cv2 as cv

img = cv.imread('d:\\1-JoStudio\APPs\OpenCV\\alu1.png', cv.IMREAD_GRAYSCALE)
cv.imshow('Original Object', img)

ret, thsa = cv.threshold(img, 128, 255, cv.THRESH_BINARY)
cv.imshow('Binary Threshed Object', thsa)

ret, thsb = cv.threshold(img, 128, 255, cv.THRESH_BINARY_INV)
cv.imshow('Inverse Binary Threshed Object', thsb)

ret, thsc = cv.threshold(img, 128, 255, cv.THRESH_TRUNC)
cv.imshow('Truncted Object', thsc)

ret, thsd = cv.threshold(img, 128, 255, cv.THRESH_TOZERO_INV)
cv.imshow('To Zero Inversed Object', thsd)

ret, thse = cv.threshold(img, 128, 255, cv.THRESH_TOZERO)
cv.imshow('To Zero Object', thse)

cv.waitKey(0)
cv.destroyAllWindows()