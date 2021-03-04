import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

GPIO.setup(12,GPIO.OUT)
GPIO.setup(16,GPIO.OUT)
GPIO.setup(20,GPIO.OUT)
GPIO.setup(21,GPIO.OUT)
GPIO.setwarnings(False)
def Front():
        GPIO.output(12,True)
        GPIO.output(16,False)
        
        GPIO.output(20,True)
        GPIO.output(21,False)

def Back():
        GPIO.output(16,True)
        GPIO.output(12,False)
        
        GPIO.output(21,True)
        GPIO.output(20,False)
def Left():
        GPIO.output(12,True)
        GPIO.output(16,False)
        GPIO.output(20,False)
        GPIO.output(21,True)
        time.sleep(0.5)
        GPIO.output(12,False)
        GPIO.output(21,False)
def Right():
        GPIO.output(12,False)
        GPIO.output(16,True)
        GPIO.output(20,True)
        GPIO.output(21,False)
        time.sleep(0.5)
        GPIO.output(16,False)
        GPIO.output(20,False)
def Stop():
        GPIO.output(12,False)
        GPIO.output(16,False)
        GPIO.output(20,False)
        GPIO.output(21,False)

