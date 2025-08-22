from obs_websockets import *
from rich import print

class Manager:
    def __init__(self):
        self.story = ""
        self.obswebsockets_manager = OBSWebsocketsManager()

    def addMessage(self, message):
        message = message.strip()
        self.story += f" {message}"

    def showStory(self):
        # updates the text of the story
        self.obswebsockets_manager.set_text("Story", f"story: {self.story}")
        time.sleep(1)

        # shows the scene
        self.obswebsockets_manager.set_scene("Twitch Plays")

def main():
    manager = Manager()

    chatMessages = ["Hi", "this", "is", "a", "test", "message"]
    for chatMessage in chatMessages:
        cleanedMessage = chatMessage.strip()
        manager.addMessage(cleanedMessage)

        time.sleep(1)
        manager.showStory()

    print(manager.data)

if __name__ == '__main__':
    main()