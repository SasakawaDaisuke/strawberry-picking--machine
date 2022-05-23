from pynput import keyboard


old_key = ""

def x_right():
    print("右に上がる")

def x_left():
    print("左に進む")

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

def continue_move():
    print(print("動きを継続"))

def on_press(key):
    global old_key
    
    try:
        print(f'Alphanumeric key pressed: {key.char}')
        if key.char == "a":
            x_left()
            old_key = key.char
    
    except AttributeError:
        print('special key pressed: {key}')
        if key == keyboard.Key.up:
            if old_key == key:
                continue_move()
                old_key = key  #  1個前の文字と入れ替えを行う
            else:
                y_up()
                old_key= key




def on_release(key):
    print('Key released: {0}'.format(
        key))
    print(f"old_keyboard:{old_key}")
    stop()
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()



# from pynput import keyboard

# def on_press(key):
#     try:
#         print('Alphanumeric key pressed: {0} '.format(
#             key.char))
#     except AttributeError:
#         print('special key pressed: {0}'.format(
#             key))

# def on_release(key):
#     print('Key released: {0}'.format(
#         key))
#     if key == keyboard.Key.esc:
#         # Stop listener
#         return False

# # Collect events until released
# with keyboard.Listener(
#         on_press=on_press,
#         on_release=on_release) as listener:
#     listener.join()