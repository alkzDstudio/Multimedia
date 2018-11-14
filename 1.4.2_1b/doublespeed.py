import numpy as np
import cv2

def interpolate(A,B):
    return (A/2 + B/2)
  
org = cv2.VideoCapture("../LR1_1.avi") 

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('doublespeed.avi',fourcc,int(org.get(5)),(int(org.get(3)),int(org.get(4))))

list = []

check, vid0 = org.read()
list.append(vid0)
while(True): 
    check, vid1 = org.read()
    list.append(vid0)
    if check == False:
       break
    list.append(interpolate(vid0,vid1))
    vid0 = vid1

list.pop()   
for frame in list:
    frame = np.uint8(frame)
    out.write(frame) 
    cv2.imshow("Frame" , frame)
    if cv2.waitKey(25) and 0xFF == ord("q"): 
        break
  
org.release()
out.release()
cv2.destroyAllWindows() 


