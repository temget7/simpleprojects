import cv2
import time
width=720
height=540
x=0
y=0
cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS,30)
a=time.time()
while True:
    a=time.time()
    ignore,frame1=cam.read()
    frame1[140:220,250:390]=(0,0,255)
    cv2.rectangle(frame1,(250,140),(390,220),(0,255,0),4)
    cv2.circle(frame1,(320,180),25,(0,0,0),1)
    cv2.circle(frame1,(320,180),15,(0,0,0),1) 
    cv2.line(frame1,(250,140),(390,220),(0,255,0),4)
    cv2.putText(frame1,'FPS:'+ str(x),(503,50),cv2.FONT_HERSHEY_DUPLEX,1,(255,0,0),2)
    cv2.putText(frame1,'F'+str(y),(0,50),cv2.FONT_HERSHEY_DUPLEX,1,(255,0,0),2)
    cv2.imshow('my-webcam',frame1)
    cv2.moveWindow('my-webcam',0,0)
    b=time.time()
    x=1/(b-a)
    y+=1
    if cv2.waitKey(1) & 0xff==ord('q'):
        break
cam.release()
b=time.time()