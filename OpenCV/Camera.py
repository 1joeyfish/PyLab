import cv2 as cv
from time import sleep

camerainfo = cv.VideoCapture(0)

ret, frame = camerainfo.read()
print('3')
sleep(1)
print('2')
sleep(1)
print('1')
sleep(1)
ret, frame = camerainfo.read()

print('Click!')
name = input('What do you want your file name to be? (Please use the undercore (_) instead of spaces:)')
filename = 'c:/Users/Techie/Desktop/Open CV saved/'+name+'.png'
cv.imwrite(filename, frame)
cv.imshow('Captured picture', frame)
cv.waitKey(0)
cv.destroyAllWindows()
camerainfo.release()