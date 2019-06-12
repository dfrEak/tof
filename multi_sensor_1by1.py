#https://pypi.org/project/VL53L1X/
#https://github.com/pimoroni/vl53l1x-python
#dropbox link: https://www.dropbox.com/sh/97run5rykuicl66/AAA9jkZRS9MHY9Xd3o_SKF-aa?dl=0

import VL53L1X
from time import sleep
import time
import RPi.GPIO as GPIO
from core.counter import counter


class sensor1by1:
    SHUTX_PIN_1 = 20
    SHUTX_PIN_2 = 16


    def __init__(self):
        GPIO.setwarnings(False)
        GPIO.setwarnings(False)

        # Setup GPIO for shutdown pins on each VL53L0X
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.SHUTX_PIN_1, GPIO.OUT)
        GPIO.setup(self.SHUTX_PIN_2, GPIO.OUT)

        # Set all shutdown pins low to turn off each VL53L0X
        GPIO.output(self.SHUTX_PIN_1, GPIO.LOW)
        GPIO.output(self.SHUTX_PIN_2, GPIO.LOW)
        sleep(1)

        # Start with first sensor
        self.pin = self.SHUTX_PIN_1
        GPIO.output(self.pin, GPIO.HIGH)

        # Initialise the i2c bus and configure the sensor
        self.tof = VL53L1X.VL53L1X()
        self.tof.open()
        GPIO.output(self.pin, GPIO.LOW)

        # counter
        self.c = counter()
        
        # set timing budget and intermeasurement period
        #self.tof.set_timing(20000,21)
        #self.tof.set_timing(33000,34)
        self.tof.set_timing(140000,141)
        
        # save pin --- HARDCODED
        self.pin1=0
        self.pin2=0

    def get_and_print_measurement(self):
        # Start ranging, 1 = Short Range, 2 = Medium Range, 3 = Long Range
        start = time.time()
        self.tof.start_ranging(3)
        #time1=time.time()-start
        #start= time.time()
        distance_in_mm = self.tof.get_distance()
        #time2=time.time()-start
        #start= time.time()
        self.tof.stop_ranging()
        #time3=time.time()-start
        #print("sensor on pin: %d\tvalue: %d\tstart: %f\tread: %f\tstop: %f" % (self.pin, distance_in_mm,time1,time2,time3) )
        print("sensor on pin: %d\tvalue: %d\ttime: %f" % (self.pin, distance_in_mm,time.time()-start) )
        
        # add to counter
        result = -1
        if (self.pin == self.SHUTX_PIN_1):
            result = self.c.checkMovementAdd(0, distance_in_mm)
            self.pin1=distance_in_mm
        else:
            result = self.c.checkMovementAdd(1, distance_in_mm)
            self.pin2=distance_in_mm

        #print("sensor1 %d\tsensor2 %d") % (self.pin1, self.pin2)

        if (result != -1):
            print("detected object to "+str(result))



    def toggle_pin(self,pin):
        if self.pin == self.SHUTX_PIN_2:
            new_pin = self.SHUTX_PIN_1
        else:
            new_pin = self.SHUTX_PIN_2
        return new_pin

    def reading(self):
        # start = time.time()
        self.pin = self.toggle_pin(self.pin)
        GPIO.output(self.pin, GPIO.HIGH)
        self.get_and_print_measurement()
        GPIO.output(self.pin, GPIO.LOW)
        sleep(0.005)
        # print("1 loop tooks %f" % (time.time()-start))

if __name__ == "__main__":
    s = sensor1by1()
    while True:
        s.reading()

