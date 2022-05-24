# coding: UTF-8
  
import time
import RPi.GPIO as GPIO

ENable = 2  # 03pin
CW = 3  # 5pin# 1=CW,0=CCW
CLK = 18  # 12pin

# init
GPIO.setmode(GPIO.BCM)
GPIO.setup(ENable, GPIO.OUT)  # GPIO2を出力として使うためのセットアップ
GPIO.output(ENable, 1)  # GPIO2に1(3.3V)を出力
GPIO.setup(CW, GPIO.OUT)  # GPIO3を出力として使うためのセットアップ
GPIO.setup(CLK, GPIO.OUT)  # GPI18を出力として使うためのセットアップ
pwm = GPIO.PWM(CLK, 100)  # 100Hz Max 200kHz
pwm.start(50)  # duty 50%

def forward(speed):
    GPIO.output(CW, 1)
    GPIO.output(ENable, 0)
    print("forward", speed)
    pwm.ChangeFrequency(speed/3)  # デューティ比の変更
    time.sleep(0.1)
    pwm.ChangeFrequency(speed)

def backwards(speed):
    GPIO.output(CW, 0)
    GPIO.output(ENable, 0)
    print("backwards", speed)
    pwm.ChangeFrequency(speed/3)
    time.sleep(0.1)
    pwm.ChangeFrequency(speed)

def Stop():
    GPIO.output(ENable, 0)
    pwm.stop()

# main
try:
    print("start")
    forward(1000)  # 固定する
    time.sleep(2)  # 1秒で半回転する、2なら1回転 
    backwards(500)
    time.sleep(2)
    Stop()
    GPIO.cleanup()  # GPIOの設定のリセット
except KeyboardInterrupt:
    pass
print("Done!")
Stop()
GPIO.cleanup()  # GPIOの設定のリセット
