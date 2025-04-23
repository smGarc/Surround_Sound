from time import sleep
import sys, termios, tty, os

print("\n")
print("Default speed and direction of motor is Slow and Forward...")
print("W-Forward, A-Left, S-Backward, D-Left\nZ-Slow, X-Medium, C-High, E-Exit")
print("\n")

def getch():
  fd = sys.stdin.fileno()
  old_settings = termios.tcgetattr(fd)
  try:
      tty.setraw(sys.stdin.fileno())
      ch = sys.stdin.read(1)

  finally:
      termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
  return ch

while(1):
  x = getch()
  if x == 'w':
    print("Forward")
    x = 'p'

  elif x == 's':
    print("Backwards")
    x = 'p'

  elif x == 'a':
    print("Turn Right")
    x = 'p'

  elif x == 'd':
    print("Turn Left")
    x = 'p'

  elif x == 'z':
    print("Slow")
    x = 'p'

  elif x == 'x':
    print("Medium")
    x = 'p'

  elif x == 'c':
    print("Fast")
    x = 'p'

  elif x == 'e':
    quit()
