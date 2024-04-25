# pip install pynput
from pynput import mouse
from nicegui import ui, core

from test import paste_img, get_active_window_title, set_active_window_title

pressed_flag = False
window = None
title = None

def on_click(x, y, button, pressed):
    global pressed_flag, window, title
    print(pressed,pressed_flag,core.app.native.main_window)
    if pressed == True and pressed_flag == True and core.app.native.main_window:
        w, title = get_active_window_title()
        if title != "NiceGUI":
            window = w
        print("show========================================", pressed_flag, title)
        core.app.native.main_window.set_always_on_top(True)
        core.app.native.main_window.show()
    action = "按下了" if pressed else "释放了"
    print(f"鼠标按键：{button}，在位置处 {(x, y)} {action}{pressed}")


listener = mouse.Listener(on_click=on_click)
listener.start()

from pynput.keyboard import Listener
from pynput import keyboard

def on_press(key):
    global pressed_flag

    print(f"按键 {key} 被按下", pressed_flag)
    if key == keyboard.Key.alt_l:
        pressed_flag = True
        # 按下 'e' 键结束程序
    print(pressed_flag)


def on_release(key):
    print(f"按键 {key} 被释放")
    global pressed_flag
    if key == keyboard.Key.alt_l:
        # 按下 'e' 键结束程序
        pressed_flag = False
    print(pressed_flag)


keyboard_listener = Listener(on_press=on_press, on_release=on_release)
keyboard_listener.start()
def hide(event):
    core.app.native.main_window.hide()

def copy_image(event):
    global window, title
    # get_active_window_title()
    print(window, title, "=========")

    set_active_window_title(window)
    get_active_window_title()
    paste_img(r"C:\Users\aaronhua\Pictures\zjc.jpeg")

ui.button('hide', on_click=hide)
ui.button('copy', on_click=copy_image)

ui.run(frameless=True, reload=False)
