import RPi.GPIO as GPIO
import time
import sys 

# GPIO 21番を使用
PIN = 19

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN, GPIO.OUT)
servo = GPIO.PWM(PIN, 50)


servo.start(0)
servo.ChangeDutyCycle(2.5)
time.sleep(3.0)
servo.ChangeDutyCycle(12.0)
time.sleep(3.0)
servo.stop()
GPIO.cleanup()