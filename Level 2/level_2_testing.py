# NOTE:
# Run this script to test out your code!
# Everything below here is for testing, you don't need to edit it.

import time
from rich import print
from level_2_code import do_we_ban_this_guy

# This is a list of example twitch chat messages
twitch_chat_messages = [
    "atrioc has no hair",
    "bald",
    "atrioc head LUL",
    "bald",
    "look at his big shiny fucking head OMEGALUL"
]

# Now we run your function on each of the twitch messages
for twitch_chat_message in twitch_chat_messages:
    ban_result = do_we_ban_this_guy(twitch_chat_message)
    print("\nWe got the following Twitch Chat message:")
    print("[yellow]      " + twitch_chat_message)
    print("And this was the ban result:")
    if ban_result:
        print("[red]      " + str(ban_result))
    else:
        print("[green]      " + str(ban_result))
    time.sleep(2)
