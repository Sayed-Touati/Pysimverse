# Importing the Drone class from pysimverse
from pysimverse import Drone
import time

# Create a drone object
drone = Drone()

# Connect to the drone
drone.connect()

drone.take_off()

time.sleep(6) # wait 3 sec while the drone stays airborne
drone.land()
time.sleep(4)