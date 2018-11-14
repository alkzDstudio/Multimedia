import cv2
import numpy as np

def biline(a,b,n):
   x = 0
   y = 0
   for i in range(b.shape[0]):
      for j in range(b.shape[1]):
         b[i][j] = int((int(a[x][y]) + int(a[x][y+1]) + int(a[x+1][y]) + int(a[x+1][y+1]))/4)
         y = j*n
      x = i*n
   return b

video1 = cv2.VideoCapture("../LR1_1.avi")
video2 = cv2.VideoCapture("../LR1_2.avi")

N = 2

W = int(video1.get(3)/N)
H = int(video1.get(4)/N)

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('videoToVideo.avi',fourcc,int(video2.get(5)),(int(video2.get(3)),int(video2.get(4))))
new = np.zeros((H,W,3))

while(video1.isOpened() or video2.isOpened() ):
    ret1, frame1 = video1.read()
    ret2, frame2 = video2.read()
    if ret1 == True and ret2 == True:
        biline(frame1[:, :, 0],new [:, :, 0],N)
        biline(frame1[:, :, 1],new [:, :, 1],N)
        biline(frame1[:, :, 2],new [:, :, 2],N)
	new = np.uint8(new)
	iX = int((video2.get(3) - new.shape[1])/2)
	iY = int((video2.get(4) - new.shape[0])/2)

        for i in range(int(video2.get(3))):
            for j in range(int(video2.get(4))):
               if (i < new.shape[0]) and (j < new.shape[1]):
	          frame2[i + iY,j+ iX] = new[i,j]
        out.write(frame2)
        cv2.imshow('frame',frame2)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        break

video1.release()
video2.release()
out.release()
cv2.destroyAllWindows() 


