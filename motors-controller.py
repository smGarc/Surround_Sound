import RPi.GPIO as GPIO
import time
import sys, termios, tty, os

RIN1 = 24
RIN2 = 23
LIN1 = 17
LIN2 = 4
EN = 25
DIR = 1

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

def resetMotors():
  GPIO.output(RIN1, GPIO.LOW)
  GPIO.output(RIN2, GPIO.LOW)
  GPIO.output(LIN1, GPIO.LOW)
  GPIO.output(LIN2, GPIO.LOW)

while(1):
  while getch() == 'p':
    print("Stop")
    resetMotors()

  while getch() == 'w':
    print("Forward")
    GPIO.output(RIN1, GPIO.HIGH)
    GPIO.output(RIN2, GPIO.LOW)
    GPIO.output(LIN1, GPIO.HIGH)
    GPIO.output(LIN2, GPIO.LOW)
    x = 'p'

  while getch() == 's':
    print("Backwards")
    GPIO.output(RIN1, GPIO.LOW)
    GPIO.output(RIN2, GPIO.HIGH)
    GPIO.output(LIN1, GPIO.LOW)
    GPIO.output(LIN2, GPIO.HIGH)
    x = 'p'

  while getch() == 'a':
    print("Turn Right")
    GPIO.output(RIN1, GPIO.LOW)
    GPIO.output(RIN2, GPIO.HIGH)
    GPIO.output(LIN1, GPIO.LOW)
    GPIO.output(LIN2, GPIO.LOW)
    x = 'p'

  while getch() == 'd':
    print("Turn Left")
    GPIO.output(RIN1, GPIO.LOW)
    GPIO.output(RIN2, GPIO.LOW)
    GPIO.output(LIN1, GPIO.HIGH)
    GPIO.output(LIN2, GPIO.HIGH)
    x = 'p'

  if getch() == 'z':
    print("Slow")
    p.ChangeDutyCycle(25)
    x = 'p'

  elif getch() == 'x':
    print("Medium")
    p.ChangeDutyCycle(50)
    x = 'p'

  elif getch() == 'c':
    print("Fast")
    p.ChangeDutyCycle(75)
    x = 'p'

  elif getch() == 'e':
    GPIO.cleanup()
    quit()
