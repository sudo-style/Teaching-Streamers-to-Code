'''
LEVEL 3 CHALLENGE - MAKING A CHAT BOT
    Write a function that reads every Twitch Chat message and decides whether to ban the guy.
    You will "return" how many seconds you want to ban the guy for.    
    Create the most interesting ban rule you can.
'''

CHANNEL_NAME = "dougdoug" # Update this to the name of your channel
OBS_TEXT_SOURCE = "BANNED USER" # Update this to the name of the text source you add in OBS

import random

# Your function takes in a message, their username, and their sub status (True or False)
# It returns the amount of time to ban the user, in seconds.
def do_we_ban_this_guy(message, username, sub):

    ban_time = 0

    # TODO - create your ban rules here! Decide how long to ban a guy!

    return ban_time