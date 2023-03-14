# -*- coding: utf-8 -*-
import time
import RPi.GPIO as GPIO


#init
GPIO.setmode(GPIO.BCM)

ENable = 2 #03pin
CW = 26 # 05pin 1=CW,0=CCW
CLK = 13 #12pin

GPIO.setup(ENable, GPIO.OUT)
GPIO.output(ENable, 1)
GPIO.setup(CW, GPIO.OUT)
GPIO.setup(CLK, GPIO.OUT)

pwm = GPIO.PWM(CLK, 100) #100Hz Max 200kHz
pwm.start(50) #duty 50%

def forward(speed):
    pwm.start(50)
    GPIO.output(CW, 0)
    GPIO.output(ENable, 0)
    pwm.ChangeFrequency(speed/3)
    time.sleep(0.1)
    pwm.ChangeFrequency(speed)
    

forward(100)
time.sleep(10)