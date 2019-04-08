#https://pypi.org/project/VL53L1X/
#https://github.com/pimoroni/vl53l1x-python
#dropbox link: https://www.dropbox.com/sh/97run5rykuicl66/AAA9jkZRS9MHY9Xd3o_SKF-aa?dl=0

import VL53L1X
import time

tof = VL53L1X.VL53L1X(i2c_bus=1, i2c_address=0x29)
tof.open() # Initialise the i2c bus and configure the sensor
tof.start_ranging(1) # Start ranging, 1 = Short Range, 2 = Medium Range, 3 = Long Range

while(1):

    distance_in_mm = tof.get_distance() # Grab the range in mmimport VL53L1X
    print(distance_in_mm)
    print("\n")
    time.sleep(0.1)

