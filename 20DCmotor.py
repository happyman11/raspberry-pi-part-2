import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
MotorApin = 20
MotorBpin = 21
GPIO.setup(MotorApin,GPIO.OUT)
GPIO.setup(MotorBpin,GPIO.OUT)
delay = 2
try:
	while True:
		x = int(input("pass your input 1 as Forward 0 as Backward: "))
		if(x==1):
			GPIO.output(MotorApin,True)
			GPIO.output(MotorBpin,False)
		elif(x==0):
			GPIO.output(MotorApin,False)
			GPIO.output(MotorBpin,True)
except KeyboardInterrupt:
	GPIO.cleanup()
