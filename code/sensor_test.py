#!/usr/bin/python
import RPi.GPIO as GPIO
import time

channel = 7

#1min for testing the sensor
timeout = 60
#time start
timeout_start = time.time()

#add event dectect to detect every time there is an event in the sensor
def setup_gpio(channel):
    
    #GPIO Setup   
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(channel, GPIO.IN)
    GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)
    GPIO.add_event_callback(channel, callback)

#When the test is over, we remove the event detect and cleanup the GPIO pins
def stop_gpio(channel):
    print("Time is over, removing the callback for the port {} and making a cleanup".format (channel))
    GPIO.remove_event_detect(channel)
    GPIO.cleanup()

#Everytime there is a callback it cames here
def callback(channel):
    if GPIO.input(channel):
        print ("Sensor enable, 1, True")
    else:
        print ("Sensor disabled, 0, False")

    
#infinite loop with safe exit for the GPIO pins
def testing(rpi_port):
    channel = int(rpi_port)
    print("Testing Sensor for 60s in channel {}".format (channel)) 
    setup_gpio(channel)
    try:
        while time.time() < timeout_start + timeout:
            time.sleep(1)
        stop_gpio(channel)
        
    # clean up the GPIO pins when Ctrl+C is pressed    
    except KeyboardInterrupt:
        GPIO.cleanup()         
    
#This part only runs when its called from other file
if __name__=="__main__":
    testing(channel)