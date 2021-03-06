#!/usr/bin/env python

import os
import time
import sys
import signal
import RPi.GPIO as GPIO

import VL53L1X


class graph:

    MAX_DISTANCE_MM = 800 # Distance at which our bar is full
    BAR_CHAR = u'\u2588' # Unicode FULL BLOCK

    ANSI_COLOR_RED = "\x1b[31m"
    ANSI_COLOR_YELLOW = "\x1b[33m"
    ANSI_COLOR_GREEN = "\x1b[32m"
    ANSI_COLOR_RESET = "\x1b[0m"

    print("""graph.py
    
    Display a bar graph that ranges up to 80cm and turns yellow/red as the range decreases.
    
    Press Ctrl+C to exit.
    
    """)

    """
    Grab the width/height of the terminal using `stty size`
    """
    rows, cols = [int(c) for c in os.popen("stty size", "r").read().split()]


    """
    Open and start the VL53L1X ranging sensor
    """
    SHUTX_PIN_1 = 20
    SHUTX_PIN_2 = 16

    GPIO.setwarnings(False)

    # Setup GPIO for shutdown pins on each VL53L0X
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(SHUTX_PIN_1, GPIO.OUT)
    GPIO.setup(SHUTX_PIN_2, GPIO.OUT)

    # Set all shutdown pins low to turn off each VL53L0X
    GPIO.output(SHUTX_PIN_1, GPIO.LOW)
    GPIO.output(SHUTX_PIN_2, GPIO.LOW)
    sleep(1)

    #not checked yet
    #in arduino has some problems with address

    # multiple sensors
    # sensor 1
    GPIO.output(SHUTX_PIN_1, GPIO.HIGH)
    time.sleep(0.2) # delay 200ms
    tof1 = VL53L1X.VL53L1X(i2c_bus=1, i2c_address=0x29)
    tof1.open() # Initialise the i2c bus and configure the sensor
    tof1.start_ranging(3) # Start ranging, 1 = Short Range, 2 = Medium Range, 3 = Long Range
    time.sleep(0.2) # delay 200ms

    # sensor 2
    GPIO.output(SHUTX_PIN_2, GPIO.HIGH)
    time.sleep(0.2) # delay 200ms
    tof2 = VL53L1X.VL53L1X(i2c_bus=1, i2c_address=0x28)
    tof2.open() # Initialise the i2c bus and configure the sensor
    tof2.start_ranging(3) # Start ranging, 1 = Short Range, 2 = Medium Range, 3 = Long Range
    time.sleep(0.2) # delay 200ms


    sys.stdout.write("\n")

    running = True

    def exit_handler(signal, frame):
        global running
        running = False
        tof1.stop_ranging() # Stop ranging
        sys.stdout.write("\n")
        sys.exit(0)

    signal.signal(signal.SIGINT, exit_handler)

    while running:
        println("sensor 1 ".tof1.get_distance())
        println("sensor 2 ".tof2.get_distance())


        distance_in_mm = tof1.get_distance() # Grab the range in mm
        distance_in_mm = min(MAX_DISTANCE_MM, distance_in_mm) # Cap at our MAX_DISTANCE
        bar_size = int((distance_in_mm / float(MAX_DISTANCE_MM)) * (cols-10)) # Scale bar_size to our terminal width
        bar = BAR_CHAR * bar_size # Create a bar out of `bar_size` unicode FULL BLOCK characters
        bar = bar.ljust(cols - 7, u' ') # Pad the bar to the full with of the terminal, minus the "00.00cm " prefix
        sys.stdout.write("\r") # Return the cursor to the beginning of the current line
        color = ANSI_COLOR_GREEN
        if distance_in_mm < MAX_DISTANCE_MM * 0.6:
            color = ANSI_COLOR_YELLOW
        if distance_in_mm < MAX_DISTANCE_MM * 0.3:
            color = ANSI_COLOR_RED
        sys.stdout.write(color)
        sys.stdout.write(u"{:04.1f}cm {}".format(distance_in_mm/10.0, bar)) # Output our measurement and bar
        sys.stdout.write(ANSI_COLOR_RESET)
        sys.stdout.flush() # Flush the output buffer, since we're overdrawing the last line
        time.sleep(0.1)

