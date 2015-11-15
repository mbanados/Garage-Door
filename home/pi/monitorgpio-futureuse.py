import time 
import sys
import RPi.GPIO as io 
io.setmode(io.BCM) 
gpiopin = sys.argv[1]
 
 
io.setup(gpiopin, io.IN, pull_up_down=io.PUD_UP)  
while True:
    if io.input(gpiopin):
        print("Circut Open")
    time.sleep(0.5)
