import cv2
import time
width=720
height=540
cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS,30)
while True:
    ignore,frame1=cam.read()
    FrameROI=frame1[240:340,320:400]
    frameROIGRAY=cv2.cvtColor(FrameROI,cv2.COLOR_BGR2GRAY)
    frameroibgr=cv2.cvtColor(frameROIGRAY,cv2.COLOR_GRAY2BGR)
    frame1[0:100,0:80]=frameroibgr
    cv2.imshow('the gray ROI',frameROIGRAY)
    cv2.moveWindow('the gray ROI',650,0)
    cv2.imshow('frameroi',FrameROI)
    cv2.moveWindow('frameroi',650,120)
    cv2.imshow('my-webcam',frame1) 
    cv2.moveWindow('my-webcam',0,0)
    if cv2.waitKey(1) & 0xff==ord('q'):
        break
cam.release()