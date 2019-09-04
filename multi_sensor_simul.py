#https://pypi.org/project/VL53L1X/
#https://github.com/pimoroni/vl53l1x-python
#dropbox link: https://www.dropbox.com/sh/97run5rykuicl66/AAA9jkZRS9MHY9Xd3o_SKF-aa?dl=0

import VL53L1X
import time
import RPi.GPIO as GPIO


"""
Open and start the VL53L1X ranging sensor
"""
SHUTX_PIN_1 = 16
SHUTX_PIN_2 = 20

GPIO.setwarnings(False)

# Setup GPIO for shutdown pins on each VL53L0X
GPIO.setmode(GPIO.BCM)
GPIO.setup(SHUTX_PIN_1, GPIO.OUT)
GPIO.setup(SHUTX_PIN_2, GPIO.OUT)

# Set all shutdown pins low to turn off each VL53L0X
GPIO.output(SHUTX_PIN_1, GPIO.LOW)
GPIO.output(SHUTX_PIN_2, GPIO.LOW)
time.sleep(1)

#not checked yet
#in arduino has some problems with address

# multiple sensors
# sensor 1
GPIO.output(SHUTX_PIN_1, GPIO.HIGH)
time.sleep(0.2) # delay 200ms
#tof1 = VL53L1X.VL53L1X(i2c_bus=1, i2c_address=0x29)
#tof1 = VL53L1X.VL53L1X()
tof1 = VL53L1X.VL53L1X(i2c_bus=1, i2c_address=0x22)
#tof1.change_address(0x22)
tof1.open() # Initialise the i2c bus and configure the sensor
GPIO.output(SHUTX_PIN_1, GPIO.LOW)

# sensor 2
GPIO.output(SHUTX_PIN_2, GPIO.HIGH)
time.sleep(0.2) # delay 200ms
#tof2 = VL53L1X.VL53L1X(i2c_bus=1, i2c_address=0x28)
#tof2 = VL53L1X.VL53L1X()
tof2 = VL53L1X.VL53L1X(i2c_bus=1, i2c_address=0x28)
#tof2.change_address(0x32)
tof2.open() # Initialise the i2c bus and configure the sensor
GPIO.output(SHUTX_PIN_2, GPIO.LOW)


GPIO.output(SHUTX_PIN_1, GPIO.HIGH)
GPIO.output(SHUTX_PIN_2, GPIO.HIGH)
tof1.start_ranging(3) # Start ranging, 1 = Short Range, 2 = Medium Range, 3 = Long Range
time.sleep(0.2) # delay 200ms
tof2.start_ranging(3) # Start ranging, 1 = Short Range, 2 = Medium Range, 3 = Long Range
time.sleep(0.2) # delay 200ms


while(1):

    distance_in_mm1 = tof1.get_distance() # Grab the range in mmimport VL53L1X
    distance_in_mm2 = tof2.get_distance() # Grab the range in mmimport VL53L1X
    print("sensor 1 : ")
    print(distance_in_mm1)
    print("\n")
    print("sensor 2 : ")
    print(distance_in_mm1)
    print("\n")
    time.sleep(0.1)

