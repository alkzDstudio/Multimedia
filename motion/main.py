import cv2
import numpy as np
from math import log

R = 5
blockSize = 16


def Clip(x, a, b):
    if (x > b): x = b
    if (x < a): x = a
    return x


def Y(A, W, H):
    B = 0.299 * A[:, :, 0] + 0.587 * A[:, :, 1] + 0.114 * A[:, :, 2]
    return B

def search(base, cur, H, W, Dx, Dy):
    diff = np.zeros((H, W))
    x = 0
    while (x < W):
        y = 0
        while (y < H):
            min = float("inf")

            rx = -R
            while (rx <= R):
                ry = -R
                while (ry <= R):
                    L = 0
                    for i in range(blockSize):
                        for j in range(blockSize):
                            if (x + rx + j >= 0) and (x + rx + j < W) and (y + ry + i >= 0) and (y + ry + i < H):
                                L += abs(int(cur[y + i][x + j]) - int(base[y + ry + i][x + rx + j]))
                            else:
                                L += cur[y + i][x + j]

                    L = L / (blockSize * blockSize)

                    if L < min:
                        min = L
                        dx = rx
                        dy = ry
                        Dx[int((W / blockSize) * (y / blockSize) + (x / blockSize))] = dx
                        Dy[int((W / blockSize) * (y / blockSize) + (x / blockSize))] = dy

                    ry = ry + 1
                rx = rx + 1

            for i in range(blockSize):
                for j in range(blockSize):
                    if (x + j + dx >= 0) and (x + j + dx < W) and (y + i + dy >= 0) and (y + i + dy < H):
                        diff[y + i][x + j] = Clip(int(cur[y + i][x + j]) - int(base[y + i + dy][x + j + dx]) + 128, 0,
                                                  255)
                    else:
                        diff[y + i][x + j] = 128

            y = y + blockSize
        x = x + blockSize

    return diff


# ----------------------------------------------------------------------- #


org = cv2.VideoCapture("../LR1_1.avi")

entropy_file = open('entropy.txt', 'w')

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('reverse.avi', fourcc, int(org.get(5)), (int(org.get(3)), int(org.get(4))))
W = int(org.get(3))
H = int(org.get(4))



dx = np.zeros(int((W / blockSize) * (H / blockSize)))
dy = np.zeros(int((W / blockSize) * (H / blockSize)))

pdx = np.zeros((2 * R + 1))
pdy = np.zeros((2 * R + 1))

blockCount = (W / blockSize) * (H / blockSize)
list = []

while (org.isOpened()):
    ret, vid = org.read()
    if ret == True:
        frame = Y(vid, W, H)
        frame = np.uint8(frame)
        list.append(frame)
    else:
        break

first = False

entropy_file.write('\tframe\t|\t\tentx\t\t|\t\tenty\n')
for t in range(80):
    entropy_file.write('—')
entropy_file.write('\n')

newDiff = np.zeros((H, W, 3))
fN = 1
for frame in list:
    if first == True:
        for i in range(H):
            for j in range(W):
                frame[i][j] = (int(frame[i][j]) + int(frame_old[i][j])) / 2

        diff = search(frame_old, frame, H, W, dx, dy)

        newDiff[:, :, 0] = newDiff[:, :, 1] = newDiff[:, :, 2] = diff[:, :]
        newDiff = np.uint8(newDiff)
        out.write(newDiff)

        # entropy
        entx = 0
        enty = 0
        for i in range(2 * R + 1):
            pdx[i] = 0
            pdy[i] = 0

        for i in range(int(blockCount)):
            pdx[int(dx[i]) + R] = pdx[int(dx[i]) + R] + 1
            pdy[int(dy[i]) + R] = pdy[int(dy[i]) + R] + 1

        for i in range(2 * R + 1):
            if (pdx[i] != 0):
                entx += (pdx[i] / blockCount) * (log((pdx[i] / blockCount), 2))
            if (pdy[i] != 0):
                enty += (pdy[i] / blockCount) * (log((pdy[i] / blockCount), 2))

        entropy_file.write('\t' + str(fN) + '\t|\t' + str(-entx) + '\t|\t' + str(-enty) + '\n')
        fN = fN + 1

    frame_old = frame
    first = True

entropy_file.close()
org.release()
out.release()
cv2.destroyAllWindows()
