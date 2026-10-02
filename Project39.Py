
import random
import pyttsx3

engine = pyttsx3.init()
engine.setProperty("rate", 150)
engine.setProperty("volume", 0.9)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def get_samples():
    return [
        "Hello!",
        "Python is fun!",
        "I am AI!",
        "Welcome!",
        "Keep learning!"
    ]

def main():
    print("VOICE MASTER")
    speak("Hello! Type something!")

    while True:
        user_input = input("You: ").strip().lower()

        if user_input == "exit":
            speak("Goodbye!")
            break

        elif user_input == "sample":
            phrase = random.choice(get_samples())
            print(phrase)
            speak(phrase)

        elif user_input == "speed up":
            rate = engine.getProperty("rate") + 50
            engine.setProperty("rate", rate)
            speak("Speaking faster!")

        elif user_input == "slow down":
            rate = engine.getProperty("rate") - 50
            engine.setProperty("rate", rate)
            speak("Speaking slower!")

        elif user_input == "increase volume":
            vol = engine.getProperty("volume") + 0.1
            vol = min(1.0, vol)
            engine.setProperty("volume", vol)
            speak("Volume increased!")

        elif user_input == "decrease volume":
            vol = engine.getProperty("volume") - 0.1
            vol = max(0.0, vol)
            engine.setProperty("volume", vol)
            speak("Volume decreased!")

        elif user_input == "tell a joke":
            jokes = [
                "Why was the computer cold? It left its Windows open!",
                "What do computers eat? Microchips!"
            ]
            joke = random.choice(jokes)
            print(joke)
            speak(joke)

        elif user_input:
            speak(user_input)

        else:
            print("Try again!")
            speak("Please try again!")

if __name__ == "__main__":
    main()
