# NOTE:
# Run this script to test out your code!
# Everything below here is for testing, you don't need to edit it.


import asyncio
import threading
import time
import os
from rich import print
from twitchio.ext import commands
from twitchio import *
from obs_websockets import OBSWebsocketsManager
from audio_player import AudioManager
from level_3_code import *

TOTAL_BANNED_USERS = 0

TWITCH_MOD_OAUTH_TOKEN = os.getenv('TWITCH_MOD_ACCESS_TOKEN')

class AllMessagesBot(commands.Bot):

    def __init__(self):
        super().__init__(token=TWITCH_MOD_OAUTH_TOKEN, prefix='?', initial_channels=[CHANNEL_NAME])
        self.audio_manager = AudioManager()
        self.obswebsockets_manager = OBSWebsocketsManager()
    
    async def event_ready(self):
        print(f'[green]Logged into Twitch as {self.nick}')
        self.my_channel = await self.fetch_users(names=[CHANNEL_NAME])
    
    def is_user_subscribed(self, message):
        """Check if the user is a subscriber using badges and tags"""
        # Check badges first (most reliable)
        if hasattr(message.author, 'badges'):
            badges = message.author.badges or {}
            if 'subscriber' in badges:
                return True
        # Fallback to tags
        if hasattr(message, 'tags'):
            tags = message.tags or {}
            subscriber_tag = tags.get('subscriber', '0')
            return subscriber_tag == '1'
        return False
    
    async def event_message(self, message):
        await bot.process_message(message)

    async def process_message(self, message: Message):
        global TOTAL_BANNED_USERS
        username = message.author.name
        user_message = message.content
        is_subscriber = self.is_user_subscribed(message)

        # Make sure we don't accidentally ban nightbot
        if username.lower() == "nightbot":
            return

        ############################################
        # Call their function here, get a ban length
        timeout_length = do_we_ban_this_guy(user_message.lower(), username.lower(), is_subscriber)
        ############################################

        # Check that they returned a number between 0 and 1000000
        if not isinstance(timeout_length, int) or timeout_length < 0 or timeout_length > 1000000:
            print("[red]ERROR: your ban time must be an integer between 0 and 1000000\n")
            return
        
        if timeout_length > 0:

            # BAN THEIR ASS, GET EM
            user_to_ban = await self.fetch_users(names=[username])
            if len(self.my_channel) > 0 and len(user_to_ban) > 0:
                await self.my_channel[0].timeout_user(TWITCH_MOD_OAUTH_TOKEN, self.my_channel[0].id, user_to_ban[0].id, timeout_length, "You broke the new chat rules")
    
            # Display the banned user in OBS, plus play a gunshot
            try:
                self.obswebsockets_manager.set_text(OBS_TEXT_SOURCE, f"Banned {username}")
            except:
                print("[red]ERROR: couldn't update the OBS text with the banned username!")
            self.audio_manager.play_audio("Rifle Shot.mp3", False, False, False)

            # Keep track of the banned users, just for fun
            TOTAL_BANNED_USERS += 1
            print(f"[red]BANNING: {username}")
            print(f"[yellow]MESSAGE: {user_message}")
            print(f"TOTAL BANS:[red]{TOTAL_BANNED_USERS}[/red] chatters.")
        
                
def startBot():
    global bot
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    bot = AllMessagesBot()
    bot.run()

if __name__=='__main__':
    
    global bot_thread
    bot_thread = threading.Thread(target=startBot)
    bot_thread.start()

    while True:
        time.sleep(600)