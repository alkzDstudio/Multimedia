import cv2
import numpy as np

def biline(a,b):
   x = 0
   y = 0
   for i in range(b.shape[0]):
      for j in range(b.shape[1]):
         b[i][j] = int((int(a[x][y]) + int(a[x][y+1]) + int(a[x+1][y]) + int(a[x+1][y+1]))/4)
         y = j*2
      x = i*2
   return b

org = cv2.VideoCapture("../LR1_1.avi")

W = int(org.get(3)/2)
H = int(org.get(4)/2)

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('biline.avi',fourcc,int(org.get(5)),(W,H))
new = np.zeros((H,W,3))

while(org.isOpened()):
    ret, frame = org.read()
    if ret == True:
        biline(frame[:, :, 0],new [:, :, 0])
        biline(frame[:, :, 1],new [:, :, 1])
        biline(frame[:, :, 2],new [:, :, 2])
	new = np.uint8(new)
        out.write(new)
        cv2.imshow('frame',new)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        break

org.release()
out.release()
cv2.destroyAllWindows() 


