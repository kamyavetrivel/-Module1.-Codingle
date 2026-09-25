import speech_recogniton as sr
import pyttxs3
from googletrans import Translator
def speak(text,language="en"):
    engine = pyttxs3
    engine.setproperty('rate',150)
    voices = engine.getProperty('voices')
    if language == "en":
        engine.setProperty('voice', voices[0].id)
    else:
         engine.setProperty('voice', voices[1].id)
    engine.say(text)
    engine.run and wait()
    




