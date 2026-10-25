
import speech_recognition as sr
import pyttsx3
from googletrans import Translator

LANGUAGE_OPTIONS = {
    "1": ("Hindi", "hi"),
    "2": ("Tamil", "ta"),
    "3": ("Telugu", "te"),
    "4": ("Bengali", "bn"),
    "5": ("Marathi", "mr"),
    "6": ("Gujarati", "gu"),
    "7": ("Malayalam", "ml"),
    "8": ("Punjabi", "pa"),
}

def speak(text, language="en"):
    engine = pyttsx3.init()
    engine.setProperty("rate", 150)
    voices = engine.getProperty("voices")

    if voices:
        if language == "en":
            engine.setProperty("voice", voices[0].id)
        elif len(voices) > 1:
            engine.setProperty("voice", voices[1].id)

    engine.say(text)
    engine.runAndWait()

def speech_to_text():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("\nSpeak in English...")
        recognizer.adjust_for_ambient_noise(source, duration=0.7)
        audio = recognizer.listen(source)

    try:
        print("Recognizing speech...")
        text = recognizer.recognize_google(audio, language="en-US")
        print("You said:", text)
        return text

    except sr.UnknownValueError:
        print("Could not understand the audio.")

    except sr.RequestError as exc:
        print("Speech API error:", exc)

    return ""

def translate_text(text, target_language):
    translator = Translator()
    translation = translator.translate(text, dest=target_language)
    print("Translated text:", translation.text)
    return translation.text

def display_language_options():
    print("\nAvailable languages:")

    for key, (name, code) in LANGUAGE_OPTIONS.items():
        print(key, name, code)

    choice = input("Choose a language number (1-8): ").strip()
    return LANGUAGE_OPTIONS.get(choice, ("Hindi", "hi"))

def run_translator():
    target_name, target_code = display_language_options()
    print("Selected language:", target_name)

    original_text = speech_to_text()

    if not original_text:
        return

    translated_text = translate_text(original_text, target_code)
    print("Speaking translation...")
    speak(translated_text, language="en")
    print("Translation finished!")

def main():
    print("AI Voice Translator")

    while True:
        print("\n1. Start translation")
        print("2. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            run_translator()

        elif choice == "2":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
