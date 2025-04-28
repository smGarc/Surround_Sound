import RPi.GPIO as GPIO
import time
import sys, termios, tty, os

RIN1 = 24
RIN2 = 23
LIN1 = 17
LIN2 = 4
EN = 25
DIR = 1

def getch():
  fd = sys.stdin.fileno()
  old_settings = termios.tcgetattr(fd)
  try:
      tty.setraw(sys.stdin.fileno())
      ch = sys.stdin.read(1)

  finally:
      termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
  return ch

def resetMotors():
  GPIO.output(RIN1, GPIO.LOW)
  GPIO.output(RIN2, GPIO.LOW)
  GPIO.output(LIN1, GPIO.LOW)
  GPIO.output(LIN2, GPIO.LOW)

def drive():
  GPIO.cleanup()
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(RIN1, GPIO.OUT)
  GPIO.setup(RIN2, GPIO.OUT)
  GPIO.setup(LIN1, GPIO.OUT)
  GPIO.setup(LIN2, GPIO.OUT)
  GPIO.setup(EN, GPIO.OUT)
  GPIO.output(RIN1, GPIO.LOW)
  GPIO.output(RIN2, GPIO.LOW)
  GPIO.output(LIN1, GPIO.LOW)
  GPIO.output(LIN2, GPIO.LOW)
  p = GPIO.PWM(EN, 1000)
  p.start(25)
  print("\n")
  print("Default speed and direction of motor is Slow and Forward...")
  print("W-Forward, A-Left, S-Backward, D-Left\nZ-Slow, X-Medium, C-High, E-Exit\nF-Finish Collecting Data and Terminate Program")
  print("\n")
  while(1):
    x = getch()

    if x == 'w':
      print("Forward")
      GPIO.output(RIN1, GPIO.HIGH)
      GPIO.output(RIN2, GPIO.LOW)
      GPIO.output(LIN1, GPIO.HIGH)
      GPIO.output(LIN2, GPIO.LOW)
      x = 'p'

    elif x == 's':
      print("Backwards")
      GPIO.output(RIN1, GPIO.LOW)
      GPIO.output(RIN2, GPIO.HIGH)
      GPIO.output(LIN1, GPIO.LOW)
      GPIO.output(LIN2, GPIO.HIGH)
      x = 'p'

    elif x == 'a':
      print("Turn Right")
      GPIO.output(RIN1, GPIO.LOW)
      GPIO.output(RIN2, GPIO.HIGH)
      GPIO.output(LIN1, GPIO.LOW)
      GPIO.output(LIN2, GPIO.LOW)
      x = 'p'

    elif x == 'd':
      print("Turn Left")
      GPIO.output(RIN1, GPIO.LOW)
      GPIO.output(RIN2, GPIO.LOW)
      GPIO.output(LIN1, GPIO.HIGH)
      GPIO.output(LIN2, GPIO.HIGH)
      x = 'p'

    elif x == 'q':
      print("Stop")
      resetMotors()

    elif x == 'z':
      print("Slow")
      p.ChangeDutyCycle(25)
      x = 'p'

    elif x == 'x':
      print("Medium")
      p.ChangeDutyCycle(50)
      x = 'p'

    elif x == 'c':
      print("Fast")
      p.ChangeDutyCycle(75)
      x = 'p'

    elif x == 'e':
      GPIO.cleanup()
      return
    
    elif x == 'f':
      GPIO.cleanup()
      quit()

    else:
      print("Stop")
      resetMotors()
