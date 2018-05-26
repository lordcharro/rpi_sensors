#!/usr/bin/python
import sys
import sensor_test
import dht11

rpi_input = 0

#First menu to choose the action to do
def menu():
    print("""Choose an action: 
		R: Run the sensor test
		T: Run the DHT11 temperature and humidity sensor
		Q: Quit the program
		""")
    while True:
        action_input = get_command()
        if action_input in ["r", "R"]:
            action_R()

        if action_input in ["q", "Q"]:
            print("Exiting the program")
            sys.exit(1)
        
        if action_input in ["t","T"]:
            action_T()


#get user input
def get_command():
    return input("Action: ")

#get channel in the GPIO.BOARD format
def get_channel():
    print("In what channel (GPIO.BOARD format) the sensor data pin is connected?")
    return input("Channel: ")

#when the user press R or T, demands for the channel and verify if it is a number
def action_R():
    rpi_input = get_channel()
    if rpi_input.isdigit():
        sensor_test.testing(rpi_input)
    else:
        print("""You must enter a number
        """)
        action_R()
        
def action_T():
    print("In what channel (GPIO.BCM format) the sensor data pin is connected?")
    rpi_input = input("Channel: ")
    if rpi_input.isdigit():
        dht11.tempHum_Sensor(rpi_input)
    else:
        print("""You must enter a number
        """)
        action_T()

menu()