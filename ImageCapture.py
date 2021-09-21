from djitellopy import tello
import cv2

hasbulla = tello.Tello()
hasbulla.connect()
print(hasbulla.get_battery())

hasbulla.streamon()

while True:
    img = hasbulla.get_frame_read().frame
    img = cv2.resize(img, (420, 300))
    cv2.imshow("Bild", img)
    cv2.waitKey(1)
