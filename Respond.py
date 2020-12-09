import AssistantSpeak
import os
import time
import webbrowser
import random
import playsound
import MusicPlaylist
from gtts import gTTS 



def Respond(Voice_Data):
    if "what is your name" in Voice_Data:
        AssistantSpeak("My name is Juana like Marijuana")
    if "what time is it" in Voice_Data:
        AssistantSpeak(time.ctime())
    if "google search" in Voice_Data:
        AssistantSpeak("What would you like me to search for ?")
        search=input("|:")
        url = "https://google.com/search?q="+search
        webbrowser.get().open(url)
        AssistantSpeak("Here is what i found for "+search)
    if "tell me the weather" in Voice_Data:
        print("weather is good")

    if "Play Music" or "Youtube" in Voice_Data:
        AssistantSpeak("Which Song would you like?")
        search=input("|:")
        yt="https://www.youtube.com/results?search_query="
        webbrowser.get().open(yt+search)
        AssistantSpeak("Here is what i found for "+search)

    if "shutdown" or "exit" or "close" in Voice_Data:
        exit()