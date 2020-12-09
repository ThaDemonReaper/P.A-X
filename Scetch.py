import speech_recognition as sr
import os
import time
import webbrowser
import random
import playsound
from gtts import gTTS 

Recognizer = sr.Recognizer()


def AudioRecord(ask=False):
    with sr.Microphone as source:
        if ask:
            print(ask)
        audio=r.listen(source)
        try:
            VoiceData = r.recognize_google(audio) 
        except sr.UnknownVallueError:
            AssistantSpeak("Sorry,I did not get that")
        except sr.RequestError:
            AssistantSpeak("Sorry,my speech service is down")
        return VoiceData


def AssistantSpeak(audio_string):
    TextToSpeech = gTTS.(text=audio_string , lang ='en')
    r = random.randit(1,100000000)
    audio_file = "audio-"+ str(r)+".mp3"
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)



def Respond(Voice_Data):
    if "what is your name" in Voice_Data:
        AssistantSpeak("My name is Juana")
    if "what time is it" in Voice_Data:
        AssistantSpeak(ctime())
    if "Google Search" in Voice_Data:
        search = AudioRecord("What would you like me to search for?")
        url = "https://google.com/search?q="+search
        webbrowser.get().open(url)
        AssistantSpeak("Here is what i found for"+search)
    if "tell me the weather" in Voice_Data:
        
    if "shutdown" in Voice_Data:
        exit()
time.sleep(1)
AssistantSpeak("How can i help you today?")
while 1:
    VoiceData=AudioRecord()
    Respond(VoiceData)
