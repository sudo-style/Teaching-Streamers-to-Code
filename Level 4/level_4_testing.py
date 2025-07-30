# NOTE:
# Run this script to test out your code!
# Everything below here is for testing, you don't need to edit it.


import time
import keyboard
from rich import print
from level_4_code import *

if __name__=='__main__':

    print("[green italic]\nBEGINNING HOTKEY PROGRAM\n")
    
    while True:

        if keyboard.is_pressed(82):  # numpad 0
            print("[cyan]You pressed numpad 0")
            numpad_0_pressed()
            time.sleep(0.5)
        if keyboard.is_pressed(79):  # numpad 1
            print("[cyan]You pressed numpad 1")
            numpad_1_pressed()
            time.sleep(0.5)
        if keyboard.is_pressed(80):  # numpad 2
            print("[cyan]You pressed numpad 2")
            numpad_2_pressed()
            time.sleep(0.5)
        if keyboard.is_pressed(81):  # numpad 3
            print("[cyan]You pressed numpad 3")
            numpad_3_pressed()
            time.sleep(0.5)
        if keyboard.is_pressed(75):  # numpad 4
            print("[cyan]You pressed numpad 4")
            numpad_4_pressed()
            time.sleep(0.5)
        if keyboard.is_pressed(76):  # numpad 5
            print("[cyan]You pressed numpad 5")
            numpad_5_pressed()
            time.sleep(0.5)
        if keyboard.is_pressed(77):  # numpad 6
            print("[cyan]You pressed numpad 6")
            numpad_6_pressed()
            time.sleep(0.5)
        if keyboard.is_pressed(71):  # numpad 7
            print("[cyan]You pressed numpad 7")
            numpad_7_pressed()
            time.sleep(0.5)
        if keyboard.is_pressed(72):  # numpad 8
            print("[cyan]You pressed numpad 8")
            numpad_8_pressed()
            time.sleep(0.5)
        if keyboard.is_pressed(73):  # numpad 9
            print("[cyan]You pressed numpad 9")
            numpad_9_pressed()
            time.sleep(0.5)
        if keyboard.is_pressed(83):  # numpad .
            print("[cyan]You pressed numpad .")
            numpad_dot_pressed()
            time.sleep(0.5)
        if keyboard.is_pressed(78):  # numpad +
            print("[cyan]You pressed numpad +")
            numpad_plus_pressed()
            time.sleep(0.5)
        if keyboard.is_pressed(74):  # numpad -
            print("[cyan]You pressed numpad -")
            numpad_minus_pressed()
            time.sleep(0.5)
        if keyboard.is_pressed(55):  # numpad *
            print("[cyan]You pressed numpad *")
            numpad_multiply_pressed()
            time.sleep(0.5)
        if keyboard.is_pressed(53):  # numpad /
            print("[cyan]You pressed numpad /")
            numpad_divide_pressed()
            time.sleep(0.5)
        if keyboard.is_pressed('enter'):
            print("[cyan]You pressed Enter")
            enter_pressed()
            time.sleep(0.5)
        if keyboard.is_pressed('shift'):
            print("[cyan]You pressed Shift")
            shift_pressed()
            time.sleep(0.5)
        if keyboard.is_pressed('backspace'):
            print("[cyan]You pressed Backspace")
            backspace_pressed()
            time.sleep(0.5)
        if keyboard.is_pressed('ctrl'):
            print("[cyan]You pressed Control")
            ctrl_pressed()
            time.sleep(0.5)
        if keyboard.is_pressed('alt'):
            print("[cyan]You pressed Alt")
            alt_pressed()
            time.sleep(0.5)
                
        # if keyboard.is_pressed('a'):
        #     print("[cyan]You pressed A")
    
        time.sleep(0.05)


    