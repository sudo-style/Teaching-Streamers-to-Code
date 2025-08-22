import pyttsx3

def ttsMode(username, message):
    tts(f"{username} says: {message}")

def chatMessage(username, message):
    # should work for either ttsMode or botMode
    ttsMode(username, message)

def tts(message = "Hello, I am a free Python text to speech engine!"):
    engine = pyttsx3.init()
    engine.say(message)
    engine.runAndWait()

def main():
    chatMessage(username='sudostyle', message="hi this is a test message")

if __name__ == "__main__":
    main()