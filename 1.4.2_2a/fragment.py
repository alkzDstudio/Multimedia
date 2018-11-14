import cv2

org = cv2.VideoCapture("../LR1_1.avi") 
x = 0
y = 0
w = 100
h = 100

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('fragment.avi',fourcc,int(org.get(5)),(int(x + w),int(y + h)))

while(org.isOpened()):
    ret, frame = org.read()
    if ret == True:
	if (int(org.get(3)) > (x + w)) and (int(org.get(4)) > (y + h)):
	     frame = frame[x:(x + w), y:(y + h)]
        out.write(frame)
        cv2.imshow('frame',frame)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        break

  
org.release()
out.release()
cv2.destroyAllWindows() 


