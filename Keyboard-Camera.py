from djitellopy import tello
import KeyPressModule as kp
import time
import cv2


kp.init()
hasbulla = tello.Tello()
hasbulla.connect()
print(hasbulla.get_battery())
hasbulla.streamon()
global img


def getKeyboardInput():
    lr, fb, ud, yv = 0, 0, 0, 0
    speed = 50

    if kp.getkey("LEFT"):
        lr = - speed
    elif kp.getkey("RIGHT"):
        lr = speed

    if kp.getkey("UP"):
        fb = speed
    elif kp.getkey("DOWN"):
        fb = - speed

    if kp.getkey("w"):
        ud = speed
    elif kp.getkey("s"):
        ud = - speed

    if kp.getkey("d"):
        yv = speed
    elif kp.getkey("a"):
        yv = - speed

    if kp.getkey("q"):
        hasbulla.land()  #Om jag trycker på "Q" så landar drönaren.
    if kp.getkey("e"):
        hasbulla.takeoff()

    if kp.getkey("z"):
        cv2.imwrite(f'Recourses/Images/{time.time()}.jpg', img)
        time.sleep(0.3)
        

    return [lr, fb, ud, yv]


while True:
    value = getKeyboardInput()
    hasbulla.send_rc_control(value[0], value[1], value[2], value[3])
    img = hasbulla.get_frame_read().frame
    img = cv2.resize(img, (420, 300))
    cv2.imshow("Bild", img)
    cv2.waitKey(1)

