import colorama
from colorama import Fore, Style
from textblob import TextBlob

colorama.init()

print(Fore.CYAN + "welcome to Sentiment Spy!" + Style.RESET_ALL)

user_name = input(Fore.MAGENTA + "Please enter your name: " + Style.RESET_ALL)

if not user_name:
    user_name = "Mystery Agent"

Conversation_history = []

print("\nHello, Agent " + user_name)
print("Type a sentence and i will analyze it.")
print("Type reset, history, summary or exit\n")

positive = 0
negative = 0
neutral = 0

while True:
    user_input = input(Fore.GREEN + ">> " + Style.RESET_ALL).strip()

    if not user_input:
        print(Fore.RED + "please type something")
        continue

    if user_input.lower() == "exit":
        print("bye " + user_name)
        break

    elif user_input.lower() == "reset":
        Conversation_history.clear()
        positive = negative = neutral = 0
        print("cleared!")
        continue

    elif user_input.lower() == "history":
        if not Conversation_history:
            print("no history yet")
        else:
            for item in Conversation_history:
                print(item)
        continue

    elif user_input.lower() == "summary":
        print("positive:", positive)
        print("negative:", negative)
        print("neutral:", neutral)
        continue

    polarity = TextBlob(user_input).sentiment.polarity

    if polarity > 0:
        sentiment = "positive"
        pos += 1
        print(Fore.GREEN + sentiment)
    elif polarity < 0:
        sentiment = "negative"
        neg += 1
        print(Fore.RED + sentiment)
    else:
        sentiment = "neutral"
        neu += 1
        print(Fore.YELLOW + sentiment)

    Conversation_history.append((user_input, sentiment))

print("\nfinal report:")
print("positive:", positive, "negative:", negative, "neutral:", neutral)
