from utils import *
import cv2

issa = initializeTello()
b = 640
h = 480
pid = [0.5, 0.5, 0]
pError = 0
startcounter = 0  # för inte flyga sätt siffran 1, för att flyga sätt dit siffran 0.

while True:
    if startcounter == 0:
        issa.takeoff()
        startcounter = 1

    img = telloGetFrame(issa, b, h)

    cv2.imshow("Frame", img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        issa.land()
        break

    img, info = findFace(img)
    print(info[0][0])

    pError = trackFace(info, b, pid, pError)
