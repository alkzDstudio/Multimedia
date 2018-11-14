import cv2
import numpy as np

video1 = cv2.VideoCapture("../LR1_1.avi")
video2 = cv2.VideoCapture("../LR1_2.avi")

W = int(video1.get(3))
H = int(video1.get(4))

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('25frame.avi',fourcc,int(video1.get(5)),(int(video1.get(3)),int(video1.get(4))))

check1 = True 
check2 = True 
list = [] 
N = 25
i = 0
while(check1 == True and check2 == True): 
    check1, v1 = video1.read()
    check2, v2 = video2.read()
    if i%N == 0: 
       list.append(v2)
    else:
       list.append(v1)
    i = i + 1

list.pop()  
for frame in list: 
    out.write(frame) 
    cv2.imshow("Frame" , frame)
    if cv2.waitKey(25) and 0xFF == ord("q"): 
        break

video1.release()
video2.release()
out.release()
cv2.destroyAllWindows() 


