from djitellopy import TelloSwarm

swarm = TelloSwarm.fromIps([
    "172.20.10.8",
    "172.20.10.10"
])
swarm.connect()
print(swarm.get_battery())
swarm.takeoff()

swarm.sequential(lambda i, tello: tello.move_forward(i * 20 + 20))
swarm.parallel(lambda i, tello: tello.move_left(i * 100 + 20))

swarm.land()
swarm.end()