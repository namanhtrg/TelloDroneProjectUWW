import math
from time import sleep

import cv2
import numpy as np

import KeypressModule as kp

# PARAMETERS #
fSpeed = 117 / 10  # Forward Speed cm/s 15cm/s #
aSpeed = 360 / 10  # Angular Speed degrees/s 50d/s #
interval = 0.25

dInterval = fSpeed * interval
aInterval = aSpeed * interval

x, y = 75, 675
a = 0
yaw = 0

kp.init()


points = [(0, 0), (0, 0)]


def getKeyboardInput():
    lr, fb, ud, yv = 0, 0, 0, 0

    speed = 15
    aspeed = 50
    global x, y, yaw, a
    d = 0

    if kp.getKey("LEFT"):
        lr = -speed
        d = dInterval
        a = -180
    elif kp.getKey("RIGHT"):
        lr = speed
        d = -dInterval
        a = 180

    if kp.getKey("UP"):
        fb = speed
        d = dInterval
        a = 270
    elif kp.getKey("DOWN"):
        fb = -speed
        d = -dInterval
        a = -90

    if kp.getKey("w"):
        ud = speed
    elif kp.getKey("s"):
        ud = -speed

    if kp.getKey("a"):
        yv = -aspeed
        yaw -= aInterval
    elif kp.getKey("d"):
        yv = aspeed
        yaw += aInterval



    sleep(interval)
    a += yaw
    x += int(d * math.cos(math.radians(a)))
    y += int(d * math.sin(math.radians(a)))

    return [lr, fb, ud, yv, x, y]


def drawPoints(img, points):
    for point in points:
        cv2.circle(img, point, 7, (0, 255, 0), cv2.FILLED)
    cv2.circle(img, points[-1], 15, (255, 0, 0), cv2.FILLED)
    cv2.putText(img, f'({(points[-1][0] - 75) / (10/3) }, {(points[-1][1] - 675) / (10/3) })cm',
                (points[-1][0] + 10, points[-1][1] - 15),
                cv2.FONT_ITALIC, 0.5, (74, 159, 216), 2, 1)


while True:
    vals = getKeyboardInput()
    sleep(0.05)

    img = 255 * np.ones((750, 750, 3), np.uint8)
    dx, dy = 50, 50
    grid_color = [0, 0, 0]
    img[:, ::dy, :] = grid_color
    img[::dx, :, :] = grid_color

    if points[-1][0] != vals[4] or points[-1][1] != vals[5]:
        points.append((vals[4], vals[5]))
    drawPoints(img, points)
    cv2.imshow("Arena", img)
    cv2.waitKey(1)
