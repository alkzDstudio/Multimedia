import cv2
import numpy as np

left = cv2.VideoCapture("../LR1_1.avi")
right = cv2.VideoCapture("../LR1_2.avi")

W = int(left.get(3))
H = int(left.get(4))
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('left_right.avi',fourcc,int(left.get(5)),(int(left.get(3)),int(left.get(4))))

leftFrame = []
rightFrame = []

while(left.isOpened() or right.isOpened()):
    ret1, frame_l = left.read()
    ret2, frame_r = right.read()
    if ret1 == True and ret2 == True:
        leftFrame = frame_l[0:H, 0:W:2]
	rightFrame = frame_r[0:H, 0:W:2]
	frame = np.hstack((leftFrame,rightFrame))
        out.write(frame)
        cv2.imshow('frame',frame)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        break

left.release()
right.release()
out.release()
cv2.destroyAllWindows() 


