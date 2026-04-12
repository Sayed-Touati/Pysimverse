from pysimverse import Drone
import time

drone = Drone()
drone.connect()
drone.take_off()

drone.set_speed(100)

drone.move_forward(50)
drone.move_left(220)

drone.move_forward(150)
drone.move_right(220)

drone.move_forward(50)
drone.move_right(220)


drone.land()