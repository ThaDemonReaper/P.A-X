from speech_recognition import Microphone , Recognizer , UnknownValueError , RequestError
import time
import requests
import webbrowser
import random
import playsound
from gtts import gTTS
import os


def Response(audio_string):
    TextToSpeech = gTTS(text=audio_string , lang ='en')
    r = random.randint(1,100)
    audio_file = "audio-"+ str(r)+".mp3"
    TextToSpeech.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)

def VoiceInput():
    
    recog = Recognizer()
    mic = Microphone(device_index=1)

    with mic:
        audio = recog.listen(mic)
    try:
        recognized = recog.recognize_google(audio)
    except UnknownValueError:
        Response("Try Again")
        with mic:
            audio = recog.listen(mic)
            recognized = recog.recognize_google(audio)
    except RequestError as exc:
        Response("Sorry my service is down")
    print(recognized)
    return(recognized)