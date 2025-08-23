from obs_websockets import *
from rich import print
from chatMessage import *
from datetime import datetime
import json

class Manager:
    def __init__(self):
        self.story = ""
        self.obswebsockets_manager = OBSWebsocketsManager()
        self.userJoined = {}
        self.actions = {'!join':self.joinStory,
                        '!unjoin':self.unjoinStory,
                        '!tts':self.readMessage,
                        '!save_chat_messages':self.save_chat_messages}
        self.state = {'dev_mode':True,
                      'auto_save_batch_messages':1}
        self.chat_messages = []

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

        self.save_chat_message(username, message)
        self.save_chat_messages()

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

    def save_chat_message(self, username, message):
        now = datetime.now()
        chat_message = {
            'timestamp': now.isoformat(),
            'username': username,
            'message': message,
        }
        self.chat_messages.append(chat_message)

        if len(self.chat_messages) >= self.state['auto_save_batch_messages']:
            print("saving batch messages")
            self.save_chat_messages()

    def save_chat_messages(self, *test):
        file_path = "chat_log.jsonl"
        print(f"saving chat log to {file_path}")

        with open(file_path, "a", encoding="utf-8") as f:
            for msg in self.chat_messages:
                f.write(json.dumps(msg, ensure_ascii=False) + "\n")
        self.chat_messages = []

def main():
    manager = Manager()

    chatMessages = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
    usernames = ["sudostyle","sudostyle","sudostyle","sudostyle","sudostyle","sudostyle","sudostyle","sudostyle","sudostyle"]

    for username, chatMessage in zip(usernames, chatMessages):
        cleanedMessage = chatMessage.strip()
        manager.checkMessage(username, cleanedMessage)
        manager.save_chat_message(username, cleanedMessage)

        if len(manager.chat_messages) > 0:
            print(manager.chat_messages[-1])
        else:
            print("no messages")
        time.sleep(1)

    manager.save_chat_messages()
    print(manager.chat_messages)


if __name__ == '__main__':
    main()