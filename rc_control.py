# Importing the Drone class from pysimverse
from pysimverse import Drone
import time

from zmq.ssh import forward

# Create a drone object
drone = Drone()

# Connect to the drone
drone.connect()

drone.take_off() # Take off to the default height, which is often 100 cm in this package

left_right = 0
forward_backward = 50
up_down = 0
yaw = 0

while True:
    drone.send_rc_control(left_right, forward_backward, up_down, yaw)

drone.land()
time.sleep(4)