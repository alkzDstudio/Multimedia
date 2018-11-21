import cv2 
import time
from time import gmtime, strftime

  
org = cv2.VideoCapture("LR1_1.avi") 

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('metadata.avi',fourcc,int(org.get(5)),(int(org.get(3)),int(org.get(4))))

length = int(org.get(cv2.CAP_PROP_FRAME_COUNT)) 
fps = int(org.get(cv2.CAP_PROP_FPS))

    
while(org.isOpened()):
    ret, frame = org.read()
    if ret == True:
        text = "length (frame) = " + str(length) +  "; fps = " + str(fps) + "; msec = " + str(int(org.get(cv2.CAP_PROP_POS_MSEC)))
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame, text, (5, 15), font, 0.4, (0, 255, 0), 1)
        out.write(frame)
        cv2.imshow('frame',frame)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        break
  
org.release()
out.release()
cv2.destroyAllWindows() 

