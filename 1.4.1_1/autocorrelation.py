import cv2
import numpy
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import spline
from mpl_toolkits.mplot3d import Axes3D

from numpy import mean, var, std

def autocorrelation(obj_1, obj_2):
    Y1 = obj_1[:,:,0]*0.299 + obj_1[:,:,1]*0.587 + obj_1[:,:,2]*0.114
    Y2 = obj_2[:,:,0]*0.299 + obj_2[:,:,1]*0.587 + obj_2[:,:,2]*0.114
    f1 = Y1 - mean(Y1)
    f2 = Y2 - mean(Y2)
    Mobj = mean(f1*f2)
    Sigma = std(Y1)*std(Y2)
    rec = Mobj/Sigma
    return rec

video = cv2.VideoCapture('../LR1_3.avi')
length = int(video.get(cv2.CAP_PROP_FRAME_COUNT))

list = []

while(video.isOpened()):    
    ret, frame = video.read()
    if ret==True:	
        list.append(frame) 
    else:
        break

nexList = []
tao = 0

for tao in range(length):
    nexList.append([])
    i = 0
    while ((i + tao) < length):
        nexList[tao].append(autocorrelation(list[i], list[i + tao]))
        i = i + 1
    tao = tao + 1

hf = plt.figure()
plt.plot(nexList[1])
plt.ylim((-0.2,1.1))
plt.title('video (LR1_3.avi): t = 1')
plt.show()
hf = plt.figure()
plt.plot(nexList[4])
plt.ylim((-0.2,1.1))
plt.title('video (LR1_3.avi): t = 4')
plt.show()
hf = plt.figure()
plt.plot(nexList[30])
plt.title('video (LR1_3.avi): t = 30')
plt.ylim((-0.2,1.1))
plt.show()

video.release()
cv2.destroyAllWindows()
