import time
import RPi.GPIO as GPIO
import sys
from pynput import keyboard


# GPIOの各ピンをBCM方式で指定
GPIO.setmode(GPIO.BCM)

# 各ピンの役割を定義
ENable_x = 2  # 3pin
ENable_y = 14 # 8pin
# ENable_z =  # pin
CW = 3  # 5pin　# 1=CW, 0=CCW
CLK = 18  # 12pin
CLK_servo = 19 # 35pin


# x軸ピンのセットアップ
GPIO.setup(ENable_x, GPIO.OUT)  # GPIO2を出力として使うためのセットアップ
GPIO.output(ENable_x, 1)  # GPIO2に1(3.3V)を出力
GPIO.setup(CW, GPIO.OUT)  # GPIO3を出力として使うためのセットアップ

# y軸ピンのセットアップ
GPIO.setup(ENable_y, GPIO.OUT)  # GPIO2を出力として使うためのセットアップ
GPIO.output(ENable_y, 1)  # GPIO2に1(3.3V)を出力

# z軸ピンのセットアップ
# GPIO.setup(ENable_z, GPIO.OUT)  # GPIO2を出力として使うためのセットアップ
# GPIO.output(ENable_z, 1)  # GPIO2に1(3.3V)を出力

# ステッピングモーター用のPWMのセットアップ
GPIO.setup(CLK, GPIO.OUT)  # GPI18を出力として使うためのセットアップ
pwm = GPIO.PWM(CLK, 100)  # 100Hz Max 200kHz
pwm.start(50)  # duty 50%

# サーボ用のPWMのセットアップ
GPIO.setup(CLK_servo, GPIO.OUT)  # GPI19を出力として使うためのセットアップ
pwm_servo = GPIO.PWM(CLK_servo, 50)  # MG996Rは50Hzで動作させる
pwm_servo.start(0)


# キーボードの1つ前のコマンドの記憶用
old_key = ""

# 周波数は1000で固定
speed = 1000

def x_right(speed):
    print("右に移動")
    pwm.start(50)
    GPIO.output(CW, 1)
    GPIO.output(ENable_x, 0)
    pwm.ChangeFrequency(speed/3)
    time.sleep(0.1)
    pwm.ChangeFrequency(speed)

def x_left(speed):
    print("左に移動")
    pwm.start(50)
    GPIO.output(CW, 0)
    GPIO.output(ENable_x, 0)
    print("backwards", speed)
    pwm.ChangeFrequency(speed/3)
    time.sleep(0.1)
    pwm.ChangeFrequency(speed)

def y_up(speed):
    print("上に移動")
    pwm.start(50)
    GPIO.output(CW, 1)
    GPIO.output(ENable_y, 0)
    pwm.ChangeFrequency(speed/3)
    time.sleep(0.1)
    pwm.ChangeFrequency(speed)

def y_down(speed):
    print("下に移動")
    pwm.start(50)
    GPIO.output(CW, 0)
    GPIO.output(ENable_y, 0)
    pwm.ChangeFrequency(speed/3)
    time.sleep(0.1)
    pwm.ChangeFrequency(speed)

# def z_push():
#     print("奥に進む")
#     pwm.start(50)
#     GPIO.output(CW, 1)
#     GPIO.output(ENable_z, 0)
#     pwm.ChangeFrequency(speed/3)
#     time.sleep(0.1)
#     pwm.ChangeFrequency(speed)

# def z_pull():
#     print("手前に進む")
#     pwm.start(50)
#     GPIO.output(CW, 0)
#     GPIO.output(ENable_z, 0)
#     pwm.ChangeFrequency(speed/3)
#     time.sleep(0.1)
#     pwm.ChangeFrequency(speed)

def stop():
    print("停止します")
    GPIO.output(ENable_x, 1)
    GPIO.output(ENable_y, 1)
    # GPIO.output(ENable_z, 1)
    pwm.ChangeDutyCycle(0)

def continue_move():
    print("動きを継続")


def catch():
    pritn("掴む")
    pwm_servo.start(0)
    pwm_servo.ChangeDutyCycle(2.5) # -90度

def release():
    print("離す")
    pwm_servo.start(0)
    pwm_servo.ChangeDutyCycle(12.0) # 90度

def on_press(key):
    global old_key
    
    try:
        print(f'Alphanumeric key pressed: {key.char}')
        if key.char == "a":
            old_key = key.char

        else key.char == "k":
            catch()
            old_key = key.char

        else key.char == "l":
            release()
            old_key = key.char

    except AttributeError:
        
        print('special key pressed: {key}')
        

        if key == keyboard.Key.right:
            if old_key == key:
                continue_move()
                old_key = key  #  1個前の文字と入れ替えを行う
            else:
                x_right(speed)
                old_key= key
        
        elif key == keyboard.Key.left:
            if old_key == key:
                continue_move()
                old_key = key
            else:
                x_left(speed)
                old_key= key

        elif key == keyboard.Key.up:
            if old_key == key:
                continue_move()
                old_key = key
            else:
                y_up(speed)
                old_key= key
        
        elif key == keyboard.Key.down:
            if old_key == key:
                continue_move()
                old_key = key
            else:
                y_down(speed)
                old_key= key

        # elif key == keyboard.Key.left:
        #     if old_key == key:
        #         continue_move()
        #         old_key = key
        #     else:
        #         z_push(speed)
        #         old_key= key
        
        # else key == keyboard.Key.left:
        #     if old_key == key:
        #         continue_move()
        #         old_key = key
        #     else:
        #         z_pull(speed)
        #         old_key= key


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



