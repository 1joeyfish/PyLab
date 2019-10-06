import cv2 as cv
from random import randint

img = cv.imread('d:\\1-JoStudio\APPs\OpenCV\qwerty.jpg')
for i in range(1000):
    cv.line(img, (randint(0,1366),randint(0,768)), (randint(0,1366),randint(0,768)), (randint(0,255),randint(0,255),randint(0,255)), randint(1,20))
    cv.circle(img, (randint(0,1366),randint(0,768)), randint(10,50), (randint(0,255),randint(0,255),randint(0,255)), randint(5,20))
    cv.rectangle(img, (randint(0,1366),randint(0,768)), (randint(0,1366),randint(0,768)), (randint(0,255),randint(0,255),randint(0,255)), randint(5,20))
    #cv.circle(img, (1366//2,768//2), i+1, (randint(0,255),randint(0,255),randint(0,255)), randint(5,20))
    #cv.rectangle(img, (1366//2-1-i, 768//2-1-i), (1366//2+1+i, 768//2+1+i), (randint(0,255),randint(0,255),randint(0,255)), randint(5,20))

cv.imshow("Art",img)

cv.waitKey(0)
cv.destroyAllWindows