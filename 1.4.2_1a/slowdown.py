import cv2 
  
org = cv2.VideoCapture("../LR1_1.avi") 
N = 2

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('slowdown.avi',fourcc,int(org.get(5))*N,(int(org.get(3)),int(org.get(4))))

check, vid = org.read() 
list = [] 

i = 0
while(check == True): 
    check, vid = org.read() 
    if i%N == 0:
        list.append(vid)
    i = i + 1

list.pop()   
for frame in list: 
    out.write(frame) 
    cv2.imshow("Frame" , frame)
    if cv2.waitKey(25) and 0xFF == ord("q"): 
        break
  
org.release()
out.release()
cv2.destroyAllWindows() 


