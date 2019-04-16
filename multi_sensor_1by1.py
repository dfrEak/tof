#https://pypi.org/project/VL53L1X/
#https://github.com/pimoroni/vl53l1x-python
#dropbox link: https://www.dropbox.com/sh/97run5rykuicl66/AAA9jkZRS9MHY9Xd3o_SKF-aa?dl=0

import VL53L1X
from time import sleep
import time
import RPi.GPIO as GPIO
SHUTX_PIN_1 = 20
SHUTX_PIN_2 = 16

def get_and_print_measurement():
    # Start ranging, 1 = Short Range, 2 = Medium Range, 3 = Long Range
    start = time.time()
    tof.start_ranging(3)
    time1=time.time()-start
    start= time.time()
    distance_in_mm = tof.get_distance()
    time2=time.time()-start
    start= time.time()
    tof.stop_ranging()
    time3=time.time()-start
    print("sensor on pin: %d\tvalue: %d\tstart: %f\tread: %f\tstop: %f" % (pin, distance_in_mm,time1,time2,time3) )
    #print("sensor on pin: %d\tvalue: %d\ttime: %f" % (pin, distance_in_mm,time.time()-start) )

def toggle_pin(pin):
    if pin == SHUTX_PIN_2:
        new_pin = SHUTX_PIN_1
    else:
        new_pin = SHUTX_PIN_2
    return new_pin

GPIO.setwarnings(False)

# Setup GPIO for shutdown pins on each VL53L0X
GPIO.setmode(GPIO.BCM)
GPIO.setup(SHUTX_PIN_1, GPIO.OUT)
GPIO.setup(SHUTX_PIN_2, GPIO.OUT)

# Set all shutdown pins low to turn off each VL53L0X
GPIO.output(SHUTX_PIN_1, GPIO.LOW)
GPIO.output(SHUTX_PIN_2, GPIO.LOW)
sleep(1)

# Start with first sensor
pin = SHUTX_PIN_1
GPIO.output(pin, GPIO.HIGH)

# Initialise the i2c bus and configure the sensor
tof = VL53L1X.VL53L1X()
tof.open()
GPIO.output(pin, GPIO.LOW)

while True:
    #start = time.time()
    pin = toggle_pin(pin)
    GPIO.output(pin, GPIO.HIGH)
    get_and_print_measurement()
    GPIO.output(pin, GPIO.LOW)
    sleep(0.005)
    #print("1 loop tooks %f" % (time.time()-start))

