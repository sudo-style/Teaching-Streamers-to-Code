import socket
from chatMessage import *
from obs_websockets import *

# === CONFIG ===
server = 'irc.chat.twitch.tv'
port = 6667
nickname = 'sudostyle'  # lowercase
token = f"oauth:{os.getenv('TWITCH_MOD_ACCESS_TOKEN')}"
channel = '#sudostyle'  # lowercase, with #

# === CONNECT ===
sock = socket.socket()
sock.connect((server, port))
sock.send(f"PASS {token}\n".encode('utf-8'))
sock.send(f"NICK {nickname}\n".encode('utf-8'))
sock.send(f"JOIN {channel}\n".encode('utf-8'))

print(f"Connected to {channel}. Listening for chat...")

# === LISTEN LOOP ===
while True:
    resp = sock.recv(2048).decode('utf-8')

    print(resp)

    if resp.startswith('PING'):
        # Reply to Twitch server to stay connected
        sock.send("PONG :tmi.twitch.tv\n".encode('utf-8'))
        continue

    if "PRIVMSG" in resp:
        # Example raw: :username!username@username.tmi.twitch.tv PRIVMSG #channel :message here
        try:
            prefix, trailing = resp.split(" PRIVMSG ", 1)
            username = prefix.split("!")[0][1:]  # remove leading :
            message = trailing.split(" :", 1)[1]

            chatMessage(username, message)
        except Exception as e:
            print("Error parsing message:", resp, e)

    if "USERNOTICE" in resp:
        tags_part, rest = resp.split(" ", 1)
        tags = {tag.split("=")[0]: tag.split("=")[1] if "=" in tag else "" for tag in tags_part.lstrip("@").split(";")}

        msg_id = tags.get("msg-id", "")
        if msg_id == "raid":
            raider = tags.get("msg-param-displayName", "")
            viewer_count = tags.get("msg-param-viewerCount", "0")
            print(f"Raid detected! {raider} is raiding with {viewer_count} viewers!")
            # do something here, e.g., trigger a welcome message
            raid(raider, viewer_count)