# -*- coding: utf-8 -*-
import time
import RPi.GPIO as GPIO


# GPIOの各ピンを指定するため
GPIO.setmode(GPIO.BCM)

ENable_y = 14 # 08pin
CW = 3 #05pin# 1=CW,0=CCW
CLK = 18 #12pin

# ピンのセットアップ
GPIO.setup(ENable_y, GPIO.OUT)  # GPIO2を出力として使うためのセットアップ
# GPIO.output(ENable_y, 1)  # GPIO2に1(3.3V)を出力
# GPIO.setup(CW , GPIO.OUT) # 202301110-del
GPIO.setup(CLK, GPIO.OUT)
# pwm = GPIO.PWM(CLK, 100) #100Hz Max 200kHz
GPIO.output(ENable_y, 1)
GPIO.cleanup()