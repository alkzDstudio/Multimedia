import numpy as np
import cv2
import matplotlib.pyplot as plt
from scipy.interpolate import spline

from numpy import mean, var, std


def average(numbers):
    return float(sum(numbers)) / max(len(numbers), 1)


def autocorrelation(obj_1, obj_2):
    obj_1 = sum(obj_1)
    obj_2 = sum(obj_2)
    f1 = obj_1 - mean(obj_1)
    f2 = obj_2 - mean(obj_2)
    Mobj = mean(f1*f2)
    Sigma = std(obj_1)*std(obj_2)
    rec = Mobj/Sigma
    return rec


video = cv2.VideoCapture('../LR1_2.avi')
length = int(video.get(cv2.CAP_PROP_FRAME_COUNT))

list = []

while(video.isOpened()):    
    ret, frame = video.read()
    if ret==True:	
	list.append(frame) 
    else:
        break

nexList = np.zeros((length,length))
tao = 1

while (tao < length):
    i = 0
    while ((i + tao) < length):
	nexList[tao][i] = (autocorrelation(list[i], list[i + tao]))
	i = i + 1
    tao = tao + 1

for i in range(3):
   plt.figure(i + 1)
   plt.plot(nexList[i + 1,:])
   plt.show()


video.release()
cv2.destroyAllWindows()

