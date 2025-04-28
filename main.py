# movement file
import motors

# sound playing, recording, & analysis file
import audio

on = True
audioFiles = []
while on:
  print("Calling motors.drive()...")
  motors.drive()
  print("Calling audio.play()...")
  audio.play()
  # audioFiles.append(audio.record())

# movement should not be available until audio recording is finished,
# so that movement sounds do not corrupt audio files.