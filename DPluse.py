import cv2

first = cv2.VideoCapture("LR1_1.avi")
last = cv2.VideoCapture("LR1_2.avi")

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('DPluse.avi',fourcc, first.get(5), (int(first.get(3)),int(first.get(4))))

while(first.isOpened()):
    ret, frame = first.read()
    if ret == True:
        out.write(frame)
        cv2.imshow('frame',frame)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        break

while(last.isOpened()):
    ret, frame = last.read()
    if ret == True:
        out.write(frame)
        cv2.imshow('frame',frame)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        break

first.release()
last.release()
out.release()
cv2.destroyAllWindows()

