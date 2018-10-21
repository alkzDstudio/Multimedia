import cv2 
  
org = cv2.VideoCapture("LR1_1.avi") 

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('reverse.avi',fourcc,int(org.get(5)),(int(org.get(3)),int(org.get(4))))

check, vid = org.read() 
list = [] 

while(check == True): 
    check, vid = org.read() 
    list.append(vid) 

list.pop()  
list.reverse()  
for frame in list: 
    out.write(frame) 
    cv2.imshow("Frame" , frame)
    if cv2.waitKey(25) and 0xFF == ord("q"): 
        break
  
org.release()
out.release()
cv2.destroyAllWindows() 


