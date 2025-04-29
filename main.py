# movement file
import motors

# sound playing, recording, & analysis file
import audio

on = True
audioFiles = []
print("Enter room name: ")
room = input()
while on:
  print("Calling motors.drive()...")
  motors.drive()
  print("Calling audio.record()...")
  audio.record(room)

# movement should not be available until audio recording is finished,
# so that movement sounds do not corrupt audio files.