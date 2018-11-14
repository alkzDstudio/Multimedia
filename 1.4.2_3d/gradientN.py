import cv2
import numpy as np
 
def Interpolate (a,b,i,N):
    A = (N-i)/N
    B = i/N
    return (np.uint8(a*A) + np.uint8(b*B))

video1 = cv2.VideoCapture("../LR1_1.avi") 
video2 = cv2.VideoCapture("../LR1_2.avi") 

length1 = int(video1.get(cv2.CAP_PROP_FRAME_COUNT))
length2 = int(video2.get(cv2.CAP_PROP_FRAME_COUNT))

N = 30

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('gradient.avi',fourcc,int(video1.get(5)),(int(video1.get(3)),int(video1.get(4))))
j = 1
for i in range(length1 + length2 - 2*N):
    if i < (length1 - N):
        ret, frame = video1.read()
    if (i >= (length1 - N)) and (i < length1):
        ret, frame1 = video1.read()
        ret, frame2 = video2.read()
        frame = np.uint8(Interpolate(frame1,frame2,float(j),float(N)))
        j = j + 1
    if (i >= length1):
        ret, frame = video2.read()

    out.write(frame)
    cv2.imshow("Frame" , frame)
    if cv2.waitKey(25) and 0xFF == ord("q"): 
        break
  
video1.release()
video2.release()
out.release()
cv2.destroyAllWindows() 
