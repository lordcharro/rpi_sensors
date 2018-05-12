#!/usr/bin/python
import sys
import sensor_test

rpi_input = 0

#First menu to choose the action to do
def menu():
    print("""Choose an action: 
		R: Run the sensor test
		Q: Quit the program
		""")
    while True:
        action_input = get_command()
        if action_input in ["r", "R"]:
            action_R()

        if action_input in ["q", "Q"]:
            print("Exiting the program")
            sys.exit(1)


#get user input
def get_command():
    return input("Action: ")

#when the user press R, demands for the channel and verify if it is a number
def action_R():
    print("In what channel (GPIO.BOARD format) the sensor data pin is connected?")
    rpi_input = input("Channel: ")
    if rpi_input.isdigit():
        sensor_test.testing(rpi_input)
    else:
        print("""You must enter a number
        """)
        action_R()

menu()