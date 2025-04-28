# import pyaudio
# import datetime
from playsound import playsound

# def record():
#   p = pyaudio.PyAudio()

def play():
  print("Playing sound...")
  playsound('600Hz.mp3')