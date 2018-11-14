import cv2
import numpy as np

up = cv2.VideoCapture("../LR1_1.avi")
down = cv2.VideoCapture("../LR1_2.avi")

W = int(up.get(3))
H = int(up.get(4))

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('up_down.avi',fourcc,int(up.get(5)),(int(up.get(3)),int(up.get(4))))

upFrame = []
downFrame = []

while(up.isOpened() or down.isOpened()):
    ret1, frame_u = up.read()
    ret2, frame_d = down.read()
    if ret1 == True and ret2 == True:
        upFrame = frame_u[0:H:2, 0:W]
	downFrame = frame_d[0:H:2, 0:W]
	frame = np.vstack((upFrame,downFrame))
        out.write(frame)
        cv2.imshow('frame',frame)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        break

up.release()
down.release()
out.release()
cv2.destroyAllWindows() 


