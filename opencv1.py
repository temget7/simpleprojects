import cv2
width=1280
height=720
rows=int(input('enter n of rows: '))
columns=int(input('enter n of columns: '))
cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS,30)
while True:
    ignore,frame1=cam.read()
    ignore,frame2=cam.read()
    grayframe=cv2.cvtColor(frame1,cv2.COLOR_BGR2GRAY)
    grayframe2=cv2.cvtColor(frame1,cv2.COLOR_BGR2GRAY) 
    frame1=cv2.resize(frame1,(int(width/columns),int(height/columns)))
    cv2.imshow('my-webcam',frame1)
    cv2.moveWindow('my-webcam',0,0)
    cv2.imshow('my-greywebcam',grayframe)
    cv2.moveWindow('my-greywebcam',1280,0)
    cv2.imshow('my-greywebcam2',grayframe2)
    cv2.moveWindow('my-greywebcam2',0,515)
    cv2.imshow('my-webcam2',frame2)
    cv2.moveWindow('my-webcam2',1280,515)
    for i in range(0, rows):
        for j in range(0,columns):
            cv2.imshow('my-webcam',frame1)
            cv2.moveWindow('my-webcam',int(width/columns)*j,int(height/columns)*i+30)
    if cv2.waitKey(1) & 0xff==ord('q'):
        break
cam.release()  

