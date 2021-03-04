import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
motor = [12,16,20,21]
for i in motor:GPIO.setup(i,GPIO.OUT)
sequence1 = [[0,0,1,1],[0,1,1,0],[1,1,0,0],[1,0,0,1]]
sequence2 = [[1,1,0,0],[0,1,1,0],[0,0,1,1],[1,0,0,1]]
x = int(input("pass your input 1 as Forward 0 as Backward: "))
try:
	while True:
		if(x==1):
			for step in sequence1:
				for pin in range(4):
					GPIO.output(motor[pin],step[pin])
				time.sleep(0.006)
		elif(x==0):
			for step in sequence2:
				for pin in range(4):
					GPIO.output(motor[pin],step[pin])
				time.sleep(0.006)                        
except KeyboardInterrupt:
	GPIO.cleanup()
