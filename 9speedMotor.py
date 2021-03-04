from gpiozero import PWMLED, MCP3008
from time import sleep

pot = MCP3008(0)
led = PWMLED(26)

while True:
   print(round(pot.value,3))
   if (pot.value < 0.002):
      led.value = 0
   else:
      led.value = pot.value

print(pot.value)
sleep(0.1)
