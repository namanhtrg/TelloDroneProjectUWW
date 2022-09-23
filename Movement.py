from djitellopy import tello
from time import sleep
me = tello.Tello()
me.connect()
print(me.get_battery())

me.takeoff()
sleep(1)
me.flip_forward()
me.flip_back()
me.flip_left()
me.land()
