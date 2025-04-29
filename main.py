# movement file
import motors

# sound playing, recording, & analysis file
import audio

audioFiles = []
print("Enter room name: ")
room = input()
while True:
  print("Calling motors.drive()...")
  motors.drive()
  print("Calling audio.record()...")
  audio.record(room)

# Movement should not be available until audio recording is finished,
# So that movement sounds do not corrupt audio files.