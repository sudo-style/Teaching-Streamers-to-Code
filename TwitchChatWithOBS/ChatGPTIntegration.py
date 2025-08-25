import os
from openai import OpenAI
from dotenv import load_dotenv

log_dir = os.path.abspath(os.path.join("..", "Log"))
if not os.path.exists(log_dir):
    os.makedirs(log_dir)


load_dotenv()
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
)

def streamer_response(username, message) -> str:
    response = client.responses.create(
        model="gpt-4.1-nano",
        instructions="You are a Twitch Streamer named sudostyle that does coding, and you are tasked to answer dumb questions form chat.",
        input=f"{message}",
    )
    return response.output_text

def ban_user(username, message) -> bool:
    response = client.responses.create(
        model="gpt-4.1-mini",
        instructions="You are a twitch streamer and need to decide weather or not to ban a user. You disallow things that are against TOS, anything that is too offensive, and also any ads. You do allow ads from WeatherTech a sponsor of the stream. Respond with a float between 0.0 and 1.0, with closer to 1.0 resulting in a ban. Keep in mind we hate ads except for our current sponsors.",
        input=f"{message}",
    )
    print(response.output_text)

    return float(response.output_text) > 0.5


if __name__ == "__main__":
    username = "thegodlypotato"
    message = "I hate weather tech floor mats"
    if ban_user(username, message):
        #ban user
        print(f"ban: {username} - {message}")
    else:
        print(streamer_response(username, message))
