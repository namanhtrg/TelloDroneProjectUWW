from djitellopy import tello
from time import sleep
me = tello.Tello()
me.connect()
print(me.get_battery())


me.takeoff()

me.move_down(40)
me.move_forward(50)
me.move_right(50)
me.move_back(50)
me.move_left(50)

me.land()