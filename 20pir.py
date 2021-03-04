import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(26,GPIO.IN,pull_up_down = GPIO.PUD_UP)
while True:
	if(GPIO.input(26) ==1):
		print("PIR Sensor detected")
GPIO.cleanup()

        
