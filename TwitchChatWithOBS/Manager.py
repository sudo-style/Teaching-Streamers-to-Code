from obs_websockets import *
from rich import print
from chatMessage import *

class Manager:
    def __init__(self):
        self.story = ""
        self.obswebsockets_manager = OBSWebsocketsManager()
        self.userJoined = {}
        self.actions = {'!join':self.joinStory,
                        '!unjoin':self.unjoinStory,
                        '!tts':self.readMessage}
        self.state = {'dev_mode':True}

    def readMessage(self, username, message):
        print("entering read message")
        ttsMode(username, message)
        print("read message")

    def addMessage(self, username, message):
        message = message.strip()
        self.story += f" {message}"
        self.showStory()

    def showStory(self):
        # updates the text of the story
        self.obswebsockets_manager.set_text("Story", f"story: {self.story}")
        time.sleep(1)

        # shows the scene
        self.obswebsockets_manager.set_scene("Twitch Plays")
        time.sleep(5)

        # goes back to code scene if streaming
        if self.state['dev_mode']:
            self.obswebsockets_manager.set_scene("Scene-Code")

    def joinStory(self, username, message):
        self.userJoined[username] = True
        print(self.userJoined)

    def unjoinStory(self, username, message):
        self.userJoined.pop(username, None)
        print(self.userJoined)

    def checkMessage(self, username, message):
        message = message.strip()
        params = message.split()
        action, action_parameter = params[0], params[1:]

        # is the message an action:
        #   do the action
        #   ex: !join: add user to the pool of participants

        #   ex: !tts Howdy
        if action in self.actions:
            message = ' '.join(action_parameter)
            self.actions[action](username, message)
            return

        # did the user join?
        #   add the message to the story

        if username in self.userJoined:
            self.addMessage(username, message)
            return

        # regular comment

def main():
    manager = Manager()

    chatMessages = ["!tts hello world", "!join", "sussy", "big boi", "!unjoin", "shouldn't show"]
    usernames = ["sudostyle","sudostyle","sudostyle","sudostyle","sudostyle","sudostyle"]

    for username, chatMessage in zip(usernames, chatMessages):
        cleanedMessage = chatMessage.strip()
        manager.checkMessage(username, cleanedMessage)
        print(cleanedMessage)
        time.sleep(1)

if __name__ == '__main__':
    main()