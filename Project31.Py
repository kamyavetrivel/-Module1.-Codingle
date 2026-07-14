def check_sentiment(text):
    text = text.lower()

    if "good" in text or "happy" in text or "love" in text:
        print("Sentiment = Positive")

    elif "bad" in text or "sad" in text or "hate" in text:
        print("Sentiment = Negative")

    else:
        print("Sentiment = Neutral")


while True:
    user_input = input("Enter a sentence or type 'q' to quit: ")

    if user_input.lower() == "q":
        break

    check_sentiment(user_input)