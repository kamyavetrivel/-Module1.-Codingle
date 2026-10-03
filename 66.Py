import speech_recognition as sr
import pyttsx3
from googletrans import Translator 
def speak(text, language="en"):
    engine = pyttsx3.init()
    engine.setProperly.init()
    voices = engine.getProperty('voices')

    if language == "en":
        engine.setProperty('voice',voices[0].id)
    else:
        engine.setProperty('voice', voices[1].id)
        engine.say(text)
        engine.runandWait()
def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("please speak in English now..")
        audio = recognizer.listen(source)
    try:
        print("recognizing speech..")
        text = recognizer.recognize_google(audio, language="en-US") 
        print(f"You said: {text}")
        return text
    except sr.UnknownValueError:
        print(" Could not understand the audio.")
    except sr.RequestError as e:
        print(f" API Error: {e}")
        return ""
 def translate_text(text, target_language="es"):
    translator = Translator()
    translation = translator.translate(text, dest=target_language)
    print(f"???? Translated text: {translation.text}")
    return translation.text
def display_langauge_options():
    print("available translation langauges:")
    print("1. Hindi (hi)")
    print("2. Tamil (ta)")
    print("3. Telegu (te)")
    print("4. Bengali (bn)")
    print("5. Marathi (mr)")
    print("6. Gujurati (gu)")
    print("7. Malyalam (ml)")
    print("8. Punjabi (pa)")
    choice = input("Please select the target langauge number (1-8):")
    langauge_dict ={
        "1": "hi",
        "2": "ta",
        "3": "te",
        "4": "bn",
        "5": "mr",
        "6": "gu",
        "7": "ml",
        "8": "pa"
    }
    return langauge_dict.get(choice,"es")

def main():
    target_language = display_language_options()  
    original_text = speech_to_text()              
    if original_text:
        translated_text = translate_text(original_text, target_language=target_language)  
        speak(translated_text, language="en")  
        print("translation spoken out!")
if __name__=="__main__":
    main()

