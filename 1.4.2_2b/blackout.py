import cv2
import numpy as np

org = cv2.VideoCapture("../LR1_1.avi") 


def check(a):
    for i in range(int(org.get(4))):
        for j in range(int(org.get(3))):
		if (a[i,j] > 255):
		    a[i,j] = 255;
		if (a[i,j] < 0):
		    a[i,j] = 0;
    return a

def ver_r(a, v, size, zn):
   for i in range(size):
       a[i] = a[i] + v*zn
       if (a[i] > 255):
           a[i] = 255
       if (a[i] < -255):
           a[i] = -255   
   return a

def mask(a,N,zn):
     for i in range(N):
        a[i,:] = ver_r(a[i,:], N - i, a.shape[1],zn)
        a[-i-1,:] = ver_r(a[-i-1,:], N - i, a.shape[1],zn)
        a[:,i] = ver_r(a[:,i], N - i, a.shape[0],zn)
        a[:,-i-1] = ver_r(a[:,-i-1], N - i, a.shape[0],zn)
     return a

N = 70

Mas = np.zeros((int(org.get(4)),int(org.get(3))))
print mask(Mas,N,-1)

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('blackout.avi',fourcc,int(org.get(5)),(int(org.get(3)),int(org.get(4))))

while(org.isOpened()):
    ret, frame = org.read()
    if ret == True:
	frame[:,:,0] = check(frame[:,:,0] + Mas[:,:])	
	frame[:,:,1] = check(frame[:,:,1] + Mas[:,:])	
	frame[:,:,2] = check(frame[:,:,2] + Mas[:,:])
        out.write(frame)
        cv2.imshow('frame',frame)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        break

  
org.release()
out.release()
cv2.destroyAllWindows() 


