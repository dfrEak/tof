#https://pypi.org/project/VL53L1X/
#https://github.com/pimoroni/vl53l1x-python
#dropbox link: https://www.dropbox.com/sh/97run5rykuicl66/AAA9jkZRS9MHY9Xd3o_SKF-aa?dl=0

#import VL53L1X
#import RPi.GPIO as GPIO
from time import sleep
import time
from core.counter import counter

# import config
from .config import config
import json


class sensor1by1:


    def __init__(self):
        #parameter
        self.SHUTX_PIN = json.loads(config.config['SENSORS']['SHUTX_PIN'])
        print(self.SHUTX_PIN)

        self.SHUTX_PIN_1 = 20
        self.SHUTX_PIN_2 = 16
        GPIO.setwarnings(False)

        # Setup GPIO for shutdown pins on each VL53L0X
        GPIO.setmode(GPIO.BCM)
        #GPIO.setup(self.SHUTX_PIN_1, GPIO.OUT)
        #GPIO.setup(self.SHUTX_PIN_2, GPIO.OUT)
        for i in range(len(self.SHUTX_PIN))
            GPIO.setup(self.SHUTX_PIN[i], GPIO.OUT)

        # Set all shutdown pins low to turn off each VL53L0X
        #GPIO.output(self.SHUTX_PIN_1, GPIO.LOW)
        #GPIO.output(self.SHUTX_PIN_2, GPIO.LOW)
        for i in range(len(self.SHUTX_PIN))
            GPIO.output(self.SHUTX_PIN[i], GPIO.LOW)
        sleep(1)

        # Start with first sensor
        #self.pin = self.SHUTX_PIN_1
        self.iPin = 0
        self.pin = self.SHUTX_PIN[self.iPin]
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
        
        # save pin
        #self.pin1=0
        #self.pin2=0
        self.pin=[]
        for i in range(len(self.SHUTX_PIN))
            self.pin.append(0)


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
        '''
        if (self.pin == self.SHUTX_PIN_1):
            result = self.c.checkMovementAdd(0, distance_in_mm)
            self.pin1=distance_in_mm
        else:
            result = self.c.checkMovementAdd(1, distance_in_mm)
            self.pin2=distance_in_mm

        #print("sensor1 %d\tsensor2 %d") % (self.pin1, self.pin2)
        '''
        result = self.c.checkMovementAdd(self.iPin, distance_in_mm)
        # save data to var
        self.pin[self.iPin]=distance_in_mm
        # print all sensors data
        strTemp=""
        for i in range(len(self.SHUTX_PIN))
            strTemp += "sensor"+self.iPin+": "+self.pin[self.iPin]+"\t"
        print(strTemp)

        if (result != -1):
            print("detected object to "+str(result))



    def toggle_pin(self,pin):
        '''
        if self.pin == self.SHUTX_PIN_2:
            new_pin = self.SHUTX_PIN_1
        else:
            new_pin = self.SHUTX_PIN_2
        '''

        self.iPin += 1
        self.iPin %= len(self.SHUTX_PIN)
        new_pin = self.SHUTX_PIN[self.iPin]

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

