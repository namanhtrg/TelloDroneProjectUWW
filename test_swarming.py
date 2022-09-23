from djitellopy import TelloSwarm
from time import sleep

swarm = TelloSwarm.fromIps(["172.20.10.8", "172.20.10.10"])
swarm.connect()
swarm.takeoff()


def doStuff(i, tello):
    if i == 1:
        tello.enable_mission_pads()
        tello.go_xyz_speed_mid(0, 0, 40, 50, 6)
        sleep(1)
        tello.go_xyz_speed_yaw_mid(80, 0, 40, 50, 0, 6, 4)
        sleep(1)
        tello.go_xyz_speed_yaw_mid(0, -70, 40, 50, 0, 4, 2)
        sleep(1)
        tello.go_xyz_speed_yaw_mid(100, 0, 40, 50, 0, 2, 6)
        sleep(1)
        tello.go_xyz_speed_mid(0, 0, 40, 50, 6)
        tello.land()
    if i == 0:
        tello.land()
    swarm.sync()


swarm.parallel(doStuff)

swarm.end()
