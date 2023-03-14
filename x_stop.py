# -*- coding: utf-8 -*-
import time
import RPi.GPIO as GPIO


# GPIOの各ピンを指定するため
GPIO.setmode(GPIO.BCM)

ENable_x = 2  # 03pin
CW = 26 #05pin# 1=CW,0=CCW
CLK = 13 #12pin

# ピンのセットアップ
GPIO.setup(ENable_x, GPIO.OUT)  # GPIO2を出力として使うためのセットアップ
GPIO.setup(CLK , GPIO.OUT)
# GPIO.setup(CW , GPIO.OUT)
# pwm = GPIO.PWM(CLK, 100) #100Hz Max 200kHz
GPIO.output(ENable_x, 1)  # GPIO2に1(3.3V)を出力
GPIO.cleanup()