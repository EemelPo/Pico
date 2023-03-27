from machine import Pin, Timer
from time import sleep

led1=Pin(22,Pin.OUT)
led2=Pin(21,Pin.OUT)
led3=Pin(20,Pin.OUT)

def loop():
    sleep(1)
    led1.on()
    sleep(1)
    led1.off()
    led2.on()
    sleep(1)
    led2.off()
    led3.on()
    sleep(1)
    led3.off()
    
while True:
    loop()
    
    
