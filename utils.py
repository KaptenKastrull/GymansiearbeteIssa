from djitellopy import Tello
import cv2
import numpy as np


def initializeTello():
    issa = Tello()
    issa.connect()
    issa.for_back_velocity = 0
    issa.left_right_velocity = 0
    issa.up_down_velocity = 0
    issa.yaw_velocity = 0
    issa.speed = 0
    print(issa.get_battery())
    issa.streamoff()
    issa.streamon()
    return issa


def telloGetFrame(issa, b = 360, h = 240):
    bild = issa.get_frame_read()
    bild = bild.frame
    img = cv2.resize(bild, (b, h))
    return img


def findFace(img):
    faceCascade = cv2.CascadeClassifier('Recourses/haarcascade_frontalface_default.xml')
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(imgGray, 1.2, 4)

    myFaceList = []
    myFaceListArea = []
    for (x, y, b, h) in faces:
        cv2.rectangle(img, (x, y), (x + b, y + h), (0, 0, 255), 2)
        cx = x + b // 2
        cy = y + h // 2
        area = b * h
        myFaceList.append([cx, cy])
        myFaceListArea.append(area)
    if len(myFaceListArea) != 0:
        i = myFaceListArea.index(max(myFaceListArea))
        return img, [myFaceList[i], myFaceListArea[i]]
    else:
        return img, [[0, 0], 0]


def trackFace(issa, info, b, pid, pError):

    error = info[0][0] - b // 2
    speed = pid[0] * error + pid[1] * (error-pError), np.CLIP(-100, 100)
    print(speed)

    if info[0][0] != 0:
        issa.yaw_velocity = speed
        issa.for_back_velocity = speed
    else:
        issa.for_back_velocity = 0
        issa.left_right_velocity = 0
        issa.up_down_velocity = 0
        issa.yaw_velocity = 0
        error = 0
    if issa.send_rc_control:
        issa.send_rc_control(issa.for_back_velocity, issa.left_right_velocity,
                             issa.up_down_velocity, issa.yaw_velocity)
        return error

