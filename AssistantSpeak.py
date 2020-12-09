import os
import time
import webbrowser
import random
import playsound
import MusicPlaylist
from gtts import gTTS 

def AssistantSpeak(audio_string):
    TextToSpeech = gTTS(text=audio_string , lang ='en')
    r = random.randrange(1,100000000)
    audio_file = "audio-"+ str(r)+".mp3"
    TextToSpeech.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)