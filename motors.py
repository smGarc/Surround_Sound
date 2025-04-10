import RPi.GPIO as GPIO
from time import sleep

RIN1 = 24
RIN2 = 23
EN = 25
LIN1 = 17
LIN2 = 4
DIR = 1

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
print("D-Drive, P-Park, F-Forward, B-Backwards, R-Turn Right, L-Turn Left,\nS-Slow, M-Medium, H-High, E-Exit")
print("\n")

while(1):
  x = input()
  if x == 'd':
    print("Drive")
    if DIR == 1:
      GPIO.output(RIN1, GPIO.HIGH)
      GPIO.output(RIN2, GPIO.LOW)
      GPIO.output(LIN1, GPIO.HIGH)
      GPIO.output(LIN2, GPIO.LOW)
      print("Forward")
      x = 'z'
    else:
      GPIO.output(RIN1, GPIO.LOW)
      GPIO.output(RIN2, GPIO.HIGH)
      GPIO.output(LIN1, GPIO.LOW)
      GPIO.output(LIN2, GPIO.HIGH)
      print("Backward")
      x = 'z'

  elif x == 'p':
    print("Park")
    GPIO.output(RIN1, GPIO.LOW)
    GPIO.output(RIN2, GPIO.LOW)
    x = 'z'

  elif x == 'f':
    print("Forward")
    GPIO.output(RIN1, GPIO.HIGH)
    GPIO.output(RIN2, GPIO.LOW)
    GPIO.output(LIN1, GPIO.HIGH)
    GPIO.output(LIN2, GPIO.LOW)
    DIR = 1
    x = 'z'

  elif x == 'b':
    print("Backwards")
    GPIO.output(RIN1, GPIO.LOW)
    GPIO.output(RIN2, GPIO.HIGH)
    GPIO.output(LIN1, GPIO.LOW)
    GPIO.output(LIN2, GPIO.HIGH)
    DIR = 0
    x = 'z'

  elif x == 'r':
    print("Turn Right")
    GPIO.output(RIN1, GPIO.LOW)
    GPIO.output(RIN2, GPIO.HIGH)
    GPIO.output(LIN1, GPIO.LOW)
    GPIO.output(LIN2, GPIO.LOW)

  elif x == 'l':
    print("Turn Left")
    GPIO.output(RIN1, GPIO.LOW)
    GPIO.output(RIN2, GPIO.LOW)
    GPIO.output(LIN1, GPIO.HIGH)
    GPIO.output(LIN2, GPIO.HIGH)

  elif x == 's':
    print("Low")
    p.ChangeDutyCycle(25)
    x = 'z'

  elif x == 'm':
    print("Medium")
    p.ChangeDutyCycle(50)
    x = 'z'

  elif x == 'h':
    print("High")
    p.ChangeDutyCycle(75)
    x = 'z'

  elif x == 'e':
    GPIO.cleanup()
    break

  else:
    print("Wrong command")
    print("Please enter a correct command to continue")
