# -*- coding: utf-8 -*-
import time
import sys
import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)

# GPIO 35番を使用
PIN = 19

GPIO.setup(PIN, GPIO.OUT)
servo = GPIO.PWM(PIN, 50)

servo.start(0)
servo.ChangeDutyCycle(10)
time.sleep(0.2)
servo.stop()
GPIO.cleanup()