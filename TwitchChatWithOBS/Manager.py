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
        self.actions = \
            {'!join':self.joinStory,
            '!unjoin':self.unjoinStory,
            '!tts':self.readMessage,
            '!poll':self.poll,
            '!micdrop':self.mic_drop,
            }

        self.mod_actions = \
            {'!save_chat_messages': self.save_chat_messages,
             '!addmic': self.add_mic,
             '!showmics': self.show_mics,
             }
        self.state = {'dev_mode':True,
                      'auto_save_batch_messages':1,
                      'tts_mode':'mic_mode'}
        self.chat_messages = []

        self.microphones = []

        self.moderators = ['sudostyle']

    # needs to be a moderator,
    # give to a specific user
    def add_mic(self, mod_, params):

        # assume that message is the user
        print(f'adding a mics for : {params}')
        for user in params:
            print(f'adding user : {user.lower()}')

            self.microphones.append(user.lower())

    def mic_drop(self, username, *message):
        self.microphones.remove(username.lower())

    def show_mics(self, username, *messages):
        print(f"Mics: {self.microphones}")

    def readMessage(self, username, *message):
        print("entering read message")
        ttsMode(username, message)
        print("read message")

    def addMessage(self, username, *message):
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

    def joinStory(self, username, *message):
        self.userJoined[username] = True
        print(self.userJoined)

    def unjoinStory(self, username, *message):
        self.userJoined.pop(username, None)
        print(self.userJoined)

    def poll(self, username, *options):
        s = " ".join(options[0])
        print(s)
        s = s.replace("',", "', ").replace("  ", " ")

        # show the options
        for x in s.split(","):
            print(x)

    def checkMessage(self, username, message):
        message = message.strip()

        # save chat message to an array in .json format

        splitted_message = message.split(' ')

        action, action_parameters = splitted_message[0], splitted_message[1:]
        print(f'action: {action}')
        print(f'action_parameters: {action_parameters}')

        # examples:
        # action  | parameters
        # !join   |
        # !addMic | sudostyle TheGodlyPotato

        stripped_message = message.strip()


        self.save_chat_message(username, message)

        # if an action is in the message
        if any(sub in stripped_message for sub in self.actions):
            if action in self.actions:
                print(f"We are going to the action: {action}")
                print(f"action_parameters type: {type(action_parameters)}")
                self.actions[action](username, action_parameters)
                return

        # only works for mods
        if username in self.moderators:
            if any(sub in stripped_message for sub in self.mod_actions):
                if action in self.mod_actions:
                    print(f"we are going to the action: {action}")
                    print(f"action_parameters type: {type(action_parameters)}")
                    self.mod_actions[action](username, action_parameters)
                    return


        # only people with mic can talk
        if self.state['tts_mode'] == 'mic_mode':
            if username in self.microphones:
                self.readMessage(username, message)

        # anyone who has joined can talk
        if self.state['tts_mode'] == 'tts_mode':
            self.readMessage(username, message)


    def save_chat_message(self, username, message):
        now = datetime.now()
        chat_message = {
            'timestamp': now.isoformat(),
            'username': username,
            'message': message,
        }
        self.chat_messages.append(chat_message)

        # autosave all messages in queue after reaching batch size
        if len(self.chat_messages) >= self.state['auto_save_batch_messages']:
            print("saving batch messages")
            self.save_chat_messages()

    def save_chat_messages(self, *test):
        file_path = "TwitchChatWithOBS/chat_log.jsonl"
        with open(file_path, "a", encoding="utf-8") as f:
            for msg in self.chat_messages:
                f.write(json.dumps(msg, ensure_ascii=False) + "\n")
        self.chat_messages = []

def main():
    manager = Manager()

    chat_messages = ["!poll 'apple juice', 'bananas', 'grapes'"]
    usernames = ["testing"] * len(chat_messages)

    # see what it will do
    for username, chat_message in zip(usernames, chat_messages):
        message = chat_message.strip()
        manager.checkMessage(username, message)
        time.sleep(1)

if __name__ == '__main__':
    main()