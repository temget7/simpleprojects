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
    frame1=cv2.resize(frame1,(int(width/columns),int(height/columns)))
    for i in range(0, rows):
        for j in range(0,columns):
            cv2.imshow('my-webcam',frame1)
            cv2.moveWindow('my-webcam',int(width/columns)*j,int(height/columns)*i+30)
    if cv2.waitKey(1) & 0xff==ord('q'): 
        break
cam.release()  

