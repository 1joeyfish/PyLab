import cv2 as cv
from time import sleep

filename = input('what do you want your video name to be?:')

path = 'c:/Users/Techie/Desktop/Open CV saved/'+filename+'.mp4'

#Open camera
camerainfo = cv.VideoCapture(0)

#Assign video format
fourcc = cv.VideoWriter_fourcc(*'MJPG')
height = int(camerainfo.get(cv.CAP_PROP_FRAME_HEIGHT))
width = int(camerainfo.get(cv.CAP_PROP_FRAME_WIDTH))
packer = cv.VideoWriter(path, fourcc, 12.5, (width, height), isColor = True)

#Start
while camerainfo.isOpened():
    ret, frame = camerainfo.read()
    frame = cv.flip(frame, 1)
    cv.imshow('Captured video', frame)
    packer.write(frame)
    key = cv.waitKey(50) &0xFF
    if key == ord('g'):
        break
    else:
        pass

packer.release()
cv.destroyAllWindows()
camerainfo.release()