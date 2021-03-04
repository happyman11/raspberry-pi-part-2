import RPi.GPIO as GPIO
from time import sleep
import time
GPIO.setmode(GPIO.BCM)


# read SPI data from MCP3008 chip, 8 possible adc's (0 thru 7)
def readadc(adcnum, clockpin, mosipin, misopin, cspin):
        if ((adcnum > 7) or (adcnum < 0)):
                return -1
        GPIO.output(cspin, True)

        GPIO.output(clockpin, False)  # start clock low
        GPIO.output(cspin, False)     # bring CS low

        commandout = adcnum
        commandout |= 0x18  # start bit + single-ended bit
        commandout <<= 3    # we only need to send 5 bits here
        for i in range(5):
                if (commandout & 0x80):
                        GPIO.output(mosipin, True)
                else:
                        GPIO.output(mosipin, False)
                commandout <<= 1
                GPIO.output(clockpin, True)
                GPIO.output(clockpin, False)

        adcout = 0
        # read in one empty bit, one null bit and 10 ADC bits
        for i in range(12):
                GPIO.output(clockpin, True)
                GPIO.output(clockpin, False)
                adcout <<= 1
                if (GPIO.input(misopin)):
                        adcout |= 0x1

        GPIO.output(cspin, True)
        
        adcout >>= 1       # first bit is 'null' so drop it
        return adcout

# change these as desired - they're the pins connected from the
# SPI port on the ADC to the Cobbler
SPICLK = 11
SPIMISO = 9
SPIMOSI = 10
SPICS = 8

# set up the SPI interface pins
GPIO.setup(SPIMOSI, GPIO.OUT)
GPIO.setup(SPIMISO, GPIO.IN)
GPIO.setup(SPICLK, GPIO.OUT)
GPIO.setup(SPICS, GPIO.OUT)

i=0
j=0
energy=0
ener = 0
kwh= 1/1000


try:
        while True:
                # read the analog pin
                voltageRaw = readadc(0, SPICLK, SPIMOSI, SPIMISO, SPICS)
                currentRaw = readadc(1, SPICLK, SPIMOSI, SPIMISO, SPICS)
                volts=voltageRaw/1.8
                amps = currentRaw/200
                power=volts*amps
                print("Calculating Energy Per Hour...... wait for a minute .")
                while(i < 60):
                        print(".")
                        voltageRaw = readadc(0, SPICLK, SPIMOSI, SPIMISO, SPICS)
                        currentRaw = readadc(1, SPICLK, SPIMOSI, SPIMISO, SPICS)
                        volts=voltageRaw/1.8
                        amps = currentRaw/200
                        power = volts * amps
                        #print("POWER:",voltage*current)
                        ener=power
                        energy=ener+energy
                        i+=1                
                        time.sleep(1)
                energyperhour=energy/(60)
                #print("Watts Hour:",energyperhour)
                KWH=energyperhour/1000
                print("KilowattPerHour:",KWH)
                sleep(2)
                print("Voltage(V): {0} | current(A): {1} | Power(KWH): {2}".format(volts,amps,KWH))

except KeyboardInterrupt:
        GPIO.cleanup()
