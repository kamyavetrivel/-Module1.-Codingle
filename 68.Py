import speech_recognition as sr
import pyttsx3
from googletrans import Translator

def speak(text, language="en"):

    engine = pyttsx3.init()

    engine.setProperty('rate', 150)  # Speed of speech

    voices = engine.getProperty('voices')

    if language == "en":
        engine.setProperty('voice', voices[0].id)  # Default English voice

    else:

        engine.setProperty('voice', voices[1].id)
        engine.say(text)
        engine.run and wait()
def speech_to_text():
    recognizer=sr.recognizer()
    with sr.Microphone() as source:
        print("??? please speak now in english...")
        audio= recognizer.listen(source)
     try:
        print("???? Recognizing speech...")

        text = recognizer.recognize_google(audio,langauge-"en,Us")
        print("you said: {text}")
        return text 
    except sr.UnknownvalueError:
        print("could not understand the audio")
    except sr.RequestError as e:
        print("API Error: (e)")
    return""
def translate_text(text, target_langauge="es"):
    translator = translator()
    translation = translator.translate(text, dest= target_langauge)
    print("translated text:{translation.text}")
    return translation.text
def display_langauge_option():
    print("available translation langauge")
    print("1. Hindi (hi)")
    print("2. Tamil (ta)")
    print("3. Telegu (te)")
    print("4. Bengali (bn)")
    print("5. Marathi (mr)")
    print("6. Gujurati (gu)")
    print("7. Malyalam (ml)")
    print("8. Punjabi (pa)")

    choice= input("please select a language number from (1-8)")
    language_dict = { 
        "1": "hi",
        "2": "ta",
        "3": “te",
        "4" : "bn",
        "5": "nr",
        "6": "gu",
        "7": "ml",
        "8": "pa"}
    return language_dict.get(choice, "es")

def main():
    target_language = display_language_options()
    original_text = speech_to_text()

    

    if original_text:
        translate_text = translate_text(original_text, target_language=target_language)
        speak(translate_text,language="en")
        print("translation spoken out")
if __name__=="__main__":
    main()
