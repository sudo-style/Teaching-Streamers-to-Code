#################################################
#                                               #
#               LEVEL 4 INTRO                   #
#                                               #
#################################################

'''
LEVEL 4 CHALLENGE - OBS Hotkey Bot
    Write a function that will cause an effect in OBS when you press different keyboard keys.
    You must create at least 5 different hotkey functions.
    Code the most interesting set of hotkeys to win!

    I've provided some basic sound effects for you to use.
    Doug can grab any additional images / audio you want.
    
    We will combine these concepts with the Twitch Chat Ban concepts for the final level.
    

NEW CONCEPTS 

    Playing Sounds
        I've provided an Audio Manager variable - you can use it to play sounds!
        Play any of the sounds I've provided, or add your own to the folder.

    Updating OBS
        I've provided an OBS Manager variable - you can use it to update your OBS!
        There's a bunch of things you can change in OBS, see examples below.

'''

# We first create the obs_manager and audio_manager (You can ignore this)
from obs_websockets import OBSWebsocketsManager
from audio_player import AudioManager
obs_manager = OBSWebsocketsManager()
audio_manager = AudioManager()

# EXAMPLES BELOW!

# Play any audio file with audio_manager!
audio_manager.play_audio("Fart.mp3")

# Here's another:
audio_manager.play_audio("Air Horn.wav")

# You can turn any OBS sources on or off.
# For example, you can make an image visible, or making your camera invisible.
obs_manager.set_source_visibility("SCENE NAME", "SOURCE NAME 1", True)
obs_manager.set_source_visibility("SCENE NAME", "SOURCE NAME 2", False)

# You can change the text of Text Sources in OBS
obs_manager.set_text("TEXT SOURCE NAME", "Your new text here!")

# You can turn an OBS filter on or off
# Can use this to turn on or off crazy visual or audio filters
obs_manager.set_filter_visibility("SOURCE NAME", "FILTER NAME 1", True)
obs_manager.set_filter_visibility("SOURCE NAME", "FILTER NAME 2", False)

# You can change your OBS scene
obs_manager.set_scene("Your Scene Name Here")



# ADVANCED - ONLY DO THIS IF YOU HAVE EXTRA TIME

# You can get the shape and size of a source (i.e. the "transform"), and then change it!
    # This can let you completely change the size and look of anything in OBS.
# Use this function to edit any of the following values: 
    # positionX, positionY, scaleX, scaleY, rotation, width, height, sourceWidth, sourceHeight, cropTop, cropBottom, cropLeft, cropRight
    # e.g. {"scaleX": 2, "scaleY": 2.5}
obs_manager.set_source_transform("SCENE NAME", "SOURCE NAME", {"scaleX": 2, "scaleY": 2.5})