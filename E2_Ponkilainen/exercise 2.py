from ssd1306 import SSD1306_I2C
from machine import Pin, I2C, ADC, Timer, PWM
import utime
from time import sleep
from led import Led

led1=Led(22)
led2=Led(21)
led3=Led(20)
rot=Pin(12,mode=Pin.IN, pull=Pin.PULL_UP)
def interrupt(rotvalue):
    led1.off()
    led2.off()
    led3.off()
    updateOLED(led1,led2,led3)
rot.irq(handler = interrupt, trigger = Pin.IRQ_FALLING)
sw0=Pin(9,mode=Pin.IN, pull=Pin.PULL_UP)
sw1=Pin(8,mode=Pin.IN, pull=Pin.PULL_UP)
sw2=Pin(7,mode=Pin.IN, pull=Pin.PULL_UP)

i2c = I2C(1, sda= Pin(14), scl = Pin(15), freq = 400000)
oled = SSD1306_I2C(128, 64, i2c)

def updateOLED(led1,led2,led3):
    led1value=led1.value()
    led2value=led2.value()
    led3value=led3.value()
    if led1value==0:
        led1ok=" "
    else:
        led1ok="x"
    if led2value==0:
        led2ok=" "
    else:
        led2ok="x"
    if led3value==0:
        led3ok=" "
    else:
        led3ok="x"
        
    oled.fill(0)
    oled.text("________________________",0,-6,1)
    oled.text("LED 1 - [" + led1ok + "]",0,10,1)
    oled.text("LED 2 - [" + led2ok + "]",0,27,1)
    oled.text("LED 3 - [" + led3ok + "]",0,45,1)
    oled.text("________________________",0,56,1)
    oled.text("L",110,8,1)
    oled.text("E",110,22,1)
    oled.text("D",110,36,1)
    oled.text("S",110,50,1)
    oled.show()
    
def interrupt(rotvalue):
    if rotvalue==0:
        led1.off()
        led2.off()
        led3.off()
        updateOLED(led1,led2,led3)
    
    
led1.off()
led2.off()
led3.off()
updateOLED(led1,led2,led3)
while True:
    sw0value=sw0.value()
    sw1value=sw1.value()
    sw2value=sw2.value()
    if sw0value==0:
        led1.toggle()
        updateOLED(led1,led2,led3)
        while True:
            sw0value=sw0.value()
            if sw0value==1:
                break
    if sw1value==0:
        led2.toggle()
        updateOLED(led1,led2,led3)
        while True:
            sw1value=sw1.value()
            if sw1value==1:
                break
    if sw2value==0:
        led3.toggle()
        updateOLED(led1,led2,led3)
        while True:
            sw2value=sw2.value()
            if sw2value==1:
                break
    sleep(0.1)
    
    
        