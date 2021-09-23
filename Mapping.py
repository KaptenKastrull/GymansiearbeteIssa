from djitellopy import tello
import numpy as np
import KeyPressModule as kp
from time import sleep
import cv2
import math

fSpeed = 117 / 10
aSpeed = 360 / 10
interval = 0.25

dinterval = fSpeed * interval
ainterval = aSpeed * interval

x, y = 500, 500
a = 0
yaw = 0

kp.init()
hasbulla = tello.Tello()
hasbulla.connect()
print(hasbulla.get_battery())
points = [(0, 0), (0, 0)]


def getKeyboardInput():
    lr, fb, ud, yv = 0, 0, 0, 0
    speed = 30
    anspeed = 50
    global x, y, yaw, a
    d = 0
    if kp.getkey("LEFT"):
        lr = - speed
        d = dinterval
        a = - 180
    elif kp.getkey("RIGHT"):
        lr = speedeeeee
        d = - dinterval
        a = 180

    if kp.getkey("UP"):
        fb = speed
        d = dinterval
        a = 270
    elif kp.getkey("DOWN"):
        fb = - speed
        d = - dinterval
        a = - 90

    if kp.getkey("w"):
        ud = speed
    elif kp.getkey("s"):
        ud = - speed

    if kp.getkey("a"):
        yv = - anspeed
        yaw -= ainterval
    elif kp.getkey("d"):
        yv = anspeed
        yaw += ainterval

    if kp.getkey("q"):
        hasbulla.land()  # Om jag trycker på "Q" så landar drönaren.
    if kp.getkey("e"):
        hasbulla.takeoff()

    sleep(interval)
    a += yaw
    x += int(d * math.cos(math.radians(a)))
    y += int(d * math.sin(math.radians(a)))

    return [lr, fb, ud, yv, x, y]


def drawPoints(img, points):
    for point in points:
        cv2.circle(img, point, 5, (0, 0, 255), cv2.FILLED)

    cv2.circle(img, points[-1], 8, (0, 225, 255), cv2.FILLED)
    cv2.putText(img, f'({(points[-1][0] - 500) / 100}, {(points[-1][1] - 500) / 100}) m',
                (points[-1][0] + 10, points[-1][1] + 30), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 255), 1)


while True:
    value = getKeyboardInput()
    hasbulla.send_rc_control(value[0], value[1], value[2], value[3])
    if points[-1][0] != value[4] or points[-1][1] != value[5]:
        points.append((value[4], value[5]))
    img = np.zeros((1000, 1000, 3), np.uint8)
    drawPoints(img, points)
    cv2.imshow("Output", img)
    cv2.waitKey(1)
