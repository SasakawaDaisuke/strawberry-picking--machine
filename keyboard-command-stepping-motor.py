import time
import RPi.GPIO as GPIO

from pynput import keyboard


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

# キーボードの1つ前の入力を記憶
old_key = ""

# 周波数は1000で固定　低くしたら回転が遅くなる
speed = 1000


def x_right(speed):
    print("右に進む")
    pwm.start(50)
    GPIO.output(CW, 1)
    GPIO.output(ENable, 0)
    pwm.ChangeFrequency(speed/3)
    time.sleep(0.1)
    pwm.ChangeFrequency(speed)

def x_left(speed):
    print("左に進む")
    pwm.start(50)
    GPIO.output(CW, 0)
    GPIO.output(ENable, 0)
    pwm.ChangeFrequency(speed/3)
    time.sleep(0.1)
    pwm.ChangeFrequency(speed)

def y_up():
    print("上に上がる")

def y_down():
    print("下に下がる")

def z_push():
    print("奥に進む")

def z_pull():
    print("手前に進む")

def stop():
    print("停止します")
    GPIO.output(ENable, 0)
    pwm.ChangeDutyCycle(0)　 # pwmは0にできないため、Dutyを0にして止める 

def continue_move():
    print("動きを継続")

def on_press(key):
    global old_key
    
    try:
        print(f'Alphanumeric key pressed: {key.char}')
        if key.char == "a":
            old_key = key.char
    
    except AttributeError:
        
        print('special key pressed: {key}')
        
        if key == keyboard.Key.right:
            if old_key == key:  # 前と同じ入力キーなら動きを継続　
                continue_move()
                old_key = key  #  1個前の文字と入れ替えを行う
            else:
                x_right(speed)　　# 新しい入力であれば動作を行う
                old_key= key
        
        elif key == keyboard.Key.left:
            if old_key == key:
                continue_move()
                old_key = key
            else:
                x_left(speed)
                old_key= key


def on_release(key):
    print('Key released: {0}'.format(
        key))
    print(f"old_keyboard:{old_key}")
    stop()
    # GPIO.cleanup()
    if key == keyboard.Key.esc:
        # Stop listener
        stop()
        GPIO.cleanup()
        return False

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
