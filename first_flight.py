# Importing the Drone class from pysimverse
from pysimverse import Drone
import time

# Create a drone object
drone = Drone()

# Connect to the drone
drone.connect()

drone.take_off() # Take off to the default height, which is often 100 cm in this package

"""
drone.move_down(20)
time.sleep(2)
drone.move_up(30)
time.sleep(2)
drone.move_left(20)
time.sleep(2)
drone.move_right(20)
time.sleep(2)
drone.move_forward(90)
time.sleep(2)
drone.move_backward(40)
time.sleep(2)
"""

drone.set_speed(50)
drone.move_forward(150)

# drone.rotate(-45)
# time.sleep(1)

drone.land()
time.sleep(4)