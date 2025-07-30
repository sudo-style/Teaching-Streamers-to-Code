#################################################
#                                               #
#               LEVEL 1 INTRO                   #
#                                               #
#################################################

'''
LEVEL 1 CHALLENGE - HAPPY PRIDE MONTH
    Write a program that prints "Hello World" every 0.1 seconds, forever.
    Each printed line should be a different color than the previous line.

    
NEW CONCEPTS

    Printing with Color
        You can add "[COLOR]" to the beginning of the sentence when using print().
        This changes the color of the sentence in the output window.
        The possible colors are:
            [red] - Red
            [green] - Green
            [blue] - Blue
            [yellow] - Yellow
            [magenta] - Magenta
            [cyan] - Cyan

    While Loops
        A "while" Loop will repeat a block of code over and over.
        To put some code "in" the while loop, indent the line of code with the tab key
        If it says "while True:" then it loops the block of code forever.

    Pausing
        You can briefly pause your program, using the time.sleep() function
        This just stops the program for a brief amount of time. This is useful if you ever want a delay inbetween two actions.
        For this level, you'll want to add a delay inbetween your print() calls.
        To do this, use time.sleep(X). You pass in X, which is the number of seconds you want to pause.
'''

# This is an "import", ignore this for now, you're too hot and rich to understand this.
import time
from rich import print

# Print a sentence with red color
print("[red] This will be a red sentence!")

# Print a sentence with blue color
print("[blue] But this will be a blue sentence.")

# Pauses the program for 3 seconds
time.sleep(3)

# This is a while loop. Everything inside of it will run forever
# To put something "inside" the While loop, use the tab key to indent it
while True:
    print("[cyan]This line of code will loop forever!!")