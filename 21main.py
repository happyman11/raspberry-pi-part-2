import RPi.GPIO as GPIO
import time
import urllib.request
import Adafruit_DHT

GPIO.setmode(GPIO.BCM)									#MQTT

myAPI = "RB5DEVUDPMVUCAXO"
baseURL = 'https://api.thingspeak.com/update?api_key=%s' % myAPI

try:
	while True:
		humidity, temperature = Adafruit_DHT.read_retry(11, 26)
		print("Humid:{0},Temp:{1}".format(humidity,temperature))
		
		urllib.request.urlopen(baseURL +"&field1=%s" % (str(temperature)))   
		time.sleep(15)
		urllib.request.urlopen(baseURL +"&field2=%s" % (str(humidity)))
		time.sleep(15)

except KeyboardInterrupt:
	print("stopping")
