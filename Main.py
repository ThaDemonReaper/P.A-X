import os
import time
import webbrowser
import random
import AssistantSpeak
import Respond
import playsound
import MusicPlaylist
from gtts import gTTS 


AssistantSpeak.AssistantSpeak("How can i help you today?")
while 1:
    VoiceData=input("|:")
    Respond.Respond(VoiceData)