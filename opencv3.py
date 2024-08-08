import cv2
from numpy import *
k=50
while True:
    frame=zeros([250,250,3],dtype=uint8)
    for i in range(1,k+1):
        for j in range(1,k+1):
            frame[int((250/k)*(i-1)):int((250/k)*(i)),int((250/k)*(j-1)):int((250/k)*(j))]=[0,255*((1-(-1)**(j+i))/2),0]
    cv2.imshow('my window',frame)
    if cv2.waitKey(1) & 0xff==ord('q'):
        break
    