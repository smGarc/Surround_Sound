import pyaudio, wave
from datetime import datetime
import sounddevice as sd
import soundfile as sf
import os

def record(room):
  newpath = str(room)
  if not os.path.exists(newpath):
    os.makedirs(newpath)

  chunk = 1024  # Record in chunks of 1024 samples
  sample_format = pyaudio.paInt16  # 16 bits per sample
  channels = 2
  fs = 44100  # Record at 44100 samples per second
  seconds = 10

  current_time = str(datetime.now())
  current_time = current_time.replace(' ', '_')
  current_time = current_time.replace(':', '-')
  current_time = current_time[:-7]

  filename = newpath + "/" + current_time + ".wav"

  p = pyaudio.PyAudio()  # Create an interface to PortAudio

  print('Recording...')

  stream = p.open(format=sample_format,
                  channels=channels,
                  rate=fs,
                  frames_per_buffer=chunk,
                  input=True)

  frames = []  # Initialize array to store frames

  play()

  # Store data in chunks for 3 seconds
  for i in range(0, int(fs / chunk * seconds)):
      data = stream.read(chunk)
      frames.append(data)

  # Stop and close the stream 
  stream.stop_stream()
  stream.close()
  # Terminate the PortAudio interface
  p.terminate()

  print('Finished recording...')

  # Save the recorded data as a WAV file
  wf = wave.open(filename, 'wb')
  wf.setnchannels(channels)
  wf.setsampwidth(p.get_sample_size(sample_format))
  wf.setframerate(fs)
  wf.writeframes(b''.join(frames))
  wf.close()

def play():
  print("Playing sound...")
  data, fs = sf.read('600Hz.mp3')
  sd.play(data, fs)