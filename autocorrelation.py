import numpy as np
import cv2
import matplotlib.pyplot as plt

from numpy import mean, var, std

def autocorrelation(obj_1, obj_2):
    obj_1 = sum(obj_1) % 255
    obj_2 = sum(obj_2) % 255
    f1 = obj_1 - mean(obj_1)
    f2 = obj_2 - mean(obj_2)
    Mobj = mean(f1*f2)
    Sigma = std(obj_1)*std(obj_2)
    rec = Mobj/Sigma
    return rec


video = cv2.VideoCapture('LR1_1.avi')

frameA = video.read()
list = []

while(video.isOpened()):    
    ret, frameB = video.read()
    if ret==True:	
	list.append(autocorrelation(frameA,frameB)) 
	frameA = frameB;
    else:
        break
    
plt.plot(list)
plt.show()

video.release()
cv2.destroyAllWindows()




