# -*- coding: utf-8 -*-
import time
import RPi.GPIO as GPIO


# GPIOの各ピンを指定するため
GPIO.setmode(GPIO.BCM)

ENable_z = 16  # 03pin
CW = 6 #05pin# 1=CW,0=CCW               
CLK = 12 #12pin

# ピンのセットアップ
GPIO.setup(ENable_z, GPIO.OUT)
GPIO.setup(CLK, GPIO.OUT)
GPIO.output(ENable_z, 1)
GPIO.cleanup()