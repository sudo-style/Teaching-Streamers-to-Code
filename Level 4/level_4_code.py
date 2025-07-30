'''
LEVEL 4 CHALLENGE - OBS Hotkey Bot
    Write a function that will cause an effect in OBS when you press different keyboard keys.
    You must create at least 5 different hotkey functions.
    Code the most interesting set of hotkeys to win!
'''

# These are imports, ignore for now
from obs_websockets import OBSWebsocketsManager
from audio_player import AudioManager
from rich import print
import time
import random

obs_manager = OBSWebsocketsManager()
audio_manager = AudioManager()

def numpad_0_pressed():
    print("This code runs when numpad 0 is pressed!")

def numpad_1_pressed():
    print("This code runs when numpad 1 is pressed!")

def numpad_2_pressed():
    print("This code runs when numpad 2 is pressed!")

def numpad_3_pressed():
    print("This code runs when numpad 3 is pressed!")

def numpad_4_pressed():
    print("This code runs when numpad 4 is pressed!")

def numpad_5_pressed():
    print("This code runs when numpad 5 is pressed!")

def numpad_6_pressed():
    print("This code runs when numpad 6 is pressed!")

def numpad_7_pressed():
    print("This code runs when numpad 7 is pressed!")

def numpad_8_pressed():
    print("This code runs when numpad 8 is pressed!")

def numpad_9_pressed():
    print("This code runs when numpad 9 is pressed!")

def numpad_dot_pressed():
    print("This code runs when numpad . is pressed!")

def numpad_plus_pressed():
    print("This code runs when numpad + is pressed!")

def numpad_minus_pressed():
    print("This code runs when numpad - is pressed!")

def numpad_multiply_pressed():
    print("This code runs when numpad * is pressed!")

def numpad_divide_pressed():
    print("This code runs when numpad / is pressed!")

def enter_pressed():
    print("This code runs when Enter is pressed!")

def shift_pressed():
    print("This code runs when Shift is pressed!")

def backspace_pressed():
    print("This code runs when Backspace is pressed!")

def ctrl_pressed():
    print("This code runs when Control is pressed!")

def alt_pressed():
    print("This code runs when Alt is pressed!")

def up_arrow_pressed():
    print("This code runs when Up Arrow is pressed!")

def left_arrow_pressed():
    print("This code runs when Left Arrow is pressed!")

def down_arrow_pressed():
    print("This code runs when Down Arrow is pressed!")

def right_arrow_pressed():
    print("This code runs when Right Arrow is pressed!")
