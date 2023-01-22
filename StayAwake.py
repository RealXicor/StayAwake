from pynput.mouse import Controller
from pynput import mouse as StayAwake_Mouse
import keyboard as StayAwake_Keyboard
import time
import threading

StayAwake_Mouse = Controller()

stop_event = threading.Event()

def on_press(key):
    if StayAwake_Keyboard.is_pressed('ctrl') and key.name == '1':
        stop_event.set()
        StayAwake_Keyboard.unhook_all()

def keep_me_alive():
    StayAwake_Keyboard.on_press(on_press)
    while not stop_event.is_set():
        StayAwake_Mouse.move(500, 0)
        time.sleep(5)
        StayAwake_Mouse.move(-500, 0)
        time.sleep(5)

mouse_thread = threading.Thread(target=keep_me_alive)
mouse_thread.start()