import requests
from datetime import datetime
from random import choice

MESSAGE = {
    "message":"Hello!",
    "timestamp": ""
}

def post_message(content):
    msg = MESSAGE
    msg["message"] = content
    msg["timestamp"] = datetime.now().strftime("%F %H:%M:%S")
    requests.post("http://127.0.0.1:5000/messages", json=msg)

if __name__ == "__main__":
    greetings = ["hello", "hey", "howdy", "what's up"]
    for _ in range(100):
        selected_greeting = choice(greetings)
        post_message(selected_greeting)