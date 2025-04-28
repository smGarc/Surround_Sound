# movement file
import motors

# sound playing, recording, & analysis file
import audio

on = True
audioFiles = []
while on:
  motors()
  audio.play()
  audioFiles.append(audio.record())

# movement should not be available until audio recording is finished,
# so that movement sounds do not corrupt audio files.