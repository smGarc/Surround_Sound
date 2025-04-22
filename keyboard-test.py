from pynput import keyboard
from pynput.keyboard import Key, KeyCode

def on_key_press(key):
  if key == Key.up:
    print("Forward")

  elif key == Key.down:
    print("Backwards")

  elif key == Key.right:
    print("Turn Right")

  elif key == Key.left:
    print("Turn Left")

  elif key == KeyCode(char='a'):
    print("Low")

  elif key == KeyCode(char='e'):
    quit()

with keyboard.Listener(on_release=on_key_press) as listener:
  listener.join()