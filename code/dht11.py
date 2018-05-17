#import the Adafruit Library
import Adafruit_DHT

#Pick the sensor type, DHT11, DHT22 or AM2302 
sensor=Adafruit_DHT.DHT11

def TempHum_Sensor(channel):
	#Using the read_retry method in order to get at least 1 good measure, and waiting 2 seconds between each retry
	humidity, temperature = Adafruit_DHT.read_retry(sensor,channel)

	#The sensor occasionally fails to return good data and we can only make a read every 2 seconds
	if humidity is not None and temperature is not None:
		print("Temp={0:0.1f}°C Humidity={1:0.1f}%".format(temperature, humidity))
	else:
		print("Failed to read the data, please try again!")