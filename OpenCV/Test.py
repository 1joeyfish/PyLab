import cv2 as cv
import os

current_location = os.getcwd()
path = os.path.join(current_location, "APPs\OpenCV\q.png")
path2 = os.path.join(current_location, "APPs\OpenCV\w.jpg")
img3 = cv.imread('d:\\1-JoStudio\APPs\OpenCV\\r.png')

img = cv.imread(path,1)
img2 = cv.imread(path2,1)
cv.imshow("Cool thing", img)
cv.imshow("Another cool thing", img2)
cv.imshow("Random cool thing",img3)

cv.waitKey(0)
cv.destroyAllWindows()