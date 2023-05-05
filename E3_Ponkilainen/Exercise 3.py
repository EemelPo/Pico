from machine import Pin, I2C, ADC, Timer, PWM
import utime
from led import Led
from ssd1306 import SSD1306_I2C
from piotimer import Piotimer
import micropython
import time
micropython.alloc_emergency_exception_buf(250)
i2c = I2C(1, sda= Pin(14), scl = Pin(15), freq = 400000)
oled = SSD1306_I2C(128, 64, i2c)
ppg=ADC(26)
led1=Led(22)



############################################
#Part 1 and Part 2 combined                #
#The PPG signal is printed to the console  #
#The heart rate is shown on the oled       #
#An LED also blinks when a beat is detected#
############################################


def box(oled):
    oled.text("________________________",0,-6,1)
    oled.text("________________________",0,56,1)
    oled.text("|",-3,2,1)
    oled.text("|",-3,10,1)
    oled.text("|",-3,18,1)
    oled.text("|",-3,26,1)
    oled.text("|",-3,34,1)
    oled.text("|",-3,42,1)
    oled.text("|",-3,50,1)
    oled.text("|",-3,58,1)
    
    oled.text("|",123,2,1)
    oled.text("|",123,10,1)
    oled.text("|",123,18,1)
    oled.text("|",123,26,1)
    oled.text("|",123,34,1)
    oled.text("|",123,42,1)
    oled.text("|",123,50,1)
    oled.text("|",123,58,1)
    
max_samples = 200
short_average=15
long_average=100
beat_threshold=150
finger_threshold=2000
history = []
ppgvalue=0
def finger_detected():
    avg_1=sum(history[-short_average:])/short_average
    avg_2=sum(history[-long_average:])/long_average
    if avg_1-avg_2 > beat_threshold:
        led1.value(1)
    else:
        led1.value(0)
def read_sample(tid):
    global ppgvalue
    ppgvalue = ppg.read_u16()
count=0
piotimer = Piotimer(mode=Piotimer.PERIODIC, freq=250, callback=read_sample)
while True:
    history.append(ppgvalue)
    history = history[-max_samples:]
    if max(history)-min(history) < finger_threshold:
        finger_detected()
        if count == 0:
            start = time.ticks_ms()
            count = 1
        else:
            if time.ticks_diff(time.ticks_ms(), start) > 300:
                PPI = time.ticks_diff(time.ticks_ms(), start)
                HR = 60/(PPI/1000)
                print(ppgvalue)
                oled.fill(0)
                box(oled)
                HR=int(HR)
                oled.text("HR: " + str(HR),25,32,1)
                oled.show()
                count = 0
    else:
        led1.value(0)
    