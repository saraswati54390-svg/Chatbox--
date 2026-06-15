import random
from datetime import datetime

print("🤖 Smart ChatBot")
print("Type 'bye' to exit.\n")

jokes = [
    "Why don't scientists trust atoms? Because they make up everything!",
    "Why did the computer go to the doctor? Because it had a virus!",
    "Why was the math book sad? Because it had too many problems!"
]

songs = [
    "Shape of You - Ed Sheeran",
    "Perfect - Ed Sheeran",
    "Believer - Imagine Dragons",
    "Kesariya",
    "Tum Hi Ho"
    "ye tune kya kiya "
    "pihu bole pihu bole"
]

while True:
    user = input("You: ").lower()

    if "hello" in user or "hi" in user:
        print("Bot: Hello! Nice to meet you. 😊")

    elif "name" in user:
        print("Bot: I am Smart ChatBot.")

    elif "how are you" in user:
        print("Bot: I am fine. Thanks for asking!")

    elif "time" in user:
        print("Bot:", datetime.now().strftime("%H:%M:%S"))

    elif "date" in user:
        print("Bot:", datetime.now().strftime("%d-%m-%Y"))

    elif "joke" in user:
        print("Bot:", random.choice(jokes))

    elif "song" in user or "music" in user:
        print("🎵 Song Suggestion:", random.choice(songs))

    elif "calculator" in user:
        try:
            exp = input("Enter calculation (e.g. 5+3): ")
            result = eval(exp)
            print("Result =", result)
        except:
            print("Invalid Calculation!")

    elif "python" in user:
        print("Bot: Python is a powerful programming language.")

    elif "bye" in user:
        print("Bot: Goodbye! Have a nice day. 👋")
        break

    else:
        print("Bot: Sorry, I don't understand that.")
