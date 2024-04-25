import time
from io import BytesIO

from PIL import Image
import win32clipboard
from pygetwindow import Win32Window

# 图片路径，替换为你自己的图片文件路径
file_image = r"C:\Users\aaronhua\Pictures\zhk.jpg"

def send_msg_to_clip(type_data, msg):
    """
    操作剪贴板分四步：
    1. 打开剪贴板：OpenClipboard()
    2. 清空剪贴板，新的数据才好写进去：EmptyClipboard()
    3. 往剪贴板写入数据：SetClipboardData()
    4. 关闭剪贴板：CloseClipboard()

    :param type_data: 数据的格式，通常是传 win32con.CF_UNICODETEXT
    :param msg: 要写入剪贴板的数据
    """
    win32clipboard.OpenClipboard()
    try:
        win32clipboard.EmptyClipboard()
        win32clipboard.SetClipboardData(type_data, msg)
    finally:
        win32clipboard.CloseClipboard()

def paste_img(file_img):
    image = Image.open(file_img)
    # 声明output字节对象
    output = BytesIO()
    # 用BMP (Bitmap) 格式存储
    # 这里是位图，然后用output字节对象来存储
    image.save(output, 'BMP')
    # BMP图片有14字节的header，需要额外去除
    data = output.getvalue()[14:]
    # 关闭
    output.close()
    # 设置好剪贴板的数据格式，再传入对应格式的数据，才能正确向剪贴板写入数据
    send_msg_to_clip(win32clipboard.CF_DIB, data)

import win32gui
import win32con

import pygetwindow
def get_active_window_title():
    window: Win32Window = pygetwindow.getActiveWindow()
    print("title ===========", window.title)
    return window, window.title

def set_active_window_title(window):
    try:
        # window.restore()
        window.activate()
    except Exception as e:
        print(e)


def main():
    paste_img(file_image)
    print("图片已成功写入剪贴板。")

if __name__ == '__main__':
    #
    #
    # window: Win32Window = pygetwindow.getActiveWindow()
    #
    # print(window.title)
    # time.sleep(3)
    # # 打印当前活动窗口的标题
    # window.activate()

    # print(get_active_window_title())
    # main()
    import ctypes
    print(ctypes.windll.user32.EnumWindows())
    window_hWnd = ctypes.windll.user32.GetForegroundWindow()
    print(dir(ctypes.windll.user32))
    print(ctypes.windll.user32.GetWindowTextW(window_hWnd))
    ctypes.windll.user32.SetForegroundWindow(window_hWnd)