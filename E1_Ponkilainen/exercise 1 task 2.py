from machine import Pin, Timer
from time import sleep
led=Pin('LED',Pin.OUT)
led1=Pin(22,Pin.OUT)
led2=Pin(21,Pin.OUT)
led3=Pin(20,Pin.OUT)
def zero():
    led1.off()
    led2.off()
    led3.off()
    
def one():
    led1.on()
    led2.off()
    led3.off()
    
def two():
    led1.off()
    led2.on()
    led3.off()
    
def three():
    led1.on()
    led2.on()
    led3.off()
    
def four():
    led1.off()
    led2.off()
    led3.on()
    
def five():
    led1.on()
    led2.off()
    led3.on()
    
def six():
    led1.off()
    led2.on()
    led3.on()
    
def seven():
    led1.on()
    led2.on()
    led3.on()
    
def blink():
    led.on()
    sleep(0.1)
    led.off()
    
def loop():
    zero()
    blink()
    sleep(0.9)
    one()
    blink()
    sleep(0.9)
    two()
    blink()
    sleep(0.9)
    three()
    blink()
    sleep(0.9)
    four()
    blink()
    sleep(0.9)
    five()
    blink()
    sleep(0.9)
    six()
    blink()
    sleep(0.9)
    seven()
    blink()
    sleep(0.9)
    
while True:
    loop()