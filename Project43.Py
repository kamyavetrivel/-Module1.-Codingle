
import speech_recognition as sr
import pyttsx3
from datetime import datetime
import random

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 150)

user_name = ""

def speak(text):
    engine.say(text)
    engine.runAndWait()

def get_audio():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Speak now...")
        audio = r.listen(source)

        try:
            command = r.recognize_google(audio)
            print("You said:", command)
            return command.lower()

        except sr.UnknownValueError:
            print("Could not understand.")
            speak("Sorry, try again.")

        except sr.RequestError as e:
            print("API error:", e)
            speak("There is a network problem.")

    return ""

def respond_to_command(command):
    global user_name

    if "hello" in command:
        if user_name:
            speak(f"Hi {user_name}, how can I help?")
        else:
            speak("Hello! How can I help you?")

    elif "your name" in command:
        speak("I am your Python assistant.")

    elif "time" in command:
        now = datetime.now().strftime("%H:%M")
        speak(f"The time is {now}")

    elif "date" in command:
        today = datetime.now().strftime("%B %d, %Y")
        speak(f"Today is {today}")

    elif "my name is" in command:
        user_name = command.split("my name is")[-1].strip().capitalize()
        speak(f"Nice to meet you, {user_name}!")

    elif "fact" in command:
        facts = [
            "Honey can last a very long time.",
            "Octopuses have three hearts.",
            "Bananas are berries.",
            "The Eiffel Tower can grow taller in summer.",
            "Water can boil and freeze at the same time."
        ]
        speak(random.choice(facts))

    elif "use male voice" in command:
        engine.setProperty('voice', voices[0].id)
        speak("Male voice selected.")

    elif "use female voice" in command:
        engine.setProperty('voice', voices[1].id)
        speak("Female voice selected.")

    elif "exit" in command or "stop" in command:
        speak("Goodbye!")
        return False

    else:
        speak("I don't understand that command.")

    return True

def main():
    speak("Voice assistant is ready. Say something!")

    while True:
        command = get_audio()

        if command and not respond_to_command(command):
            break

if __name__ == "__main__":
    main()
