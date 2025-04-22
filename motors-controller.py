import RPi.GPIO as GPIO
from time import sleep
import sys, termios, tty, os, keyboard

RIN1 = 24
RIN2 = 23
LIN1 = 17
LIN2 = 4
EN = 25
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

def resetMotors():
  GPIO.output(RIN1, GPIO.LOW)
  GPIO.output(RIN2, GPIO.LOW)
  GPIO.output(LIN1, GPIO.LOW)
  GPIO.output(LIN2, GPIO.LOW)

while(1):
  if keyboard.is_pressed('up'):
    print("Forward")
    GPIO.output(RIN1, GPIO.HIGH)
    GPIO.output(RIN2, GPIO.LOW)
    GPIO.output(LIN1, GPIO.HIGH)
    GPIO.output(LIN2, GPIO.LOW)
    resetMotors()

  elif keyboard.is_pressed('down'):
    print("Backwards")
    GPIO.output(RIN1, GPIO.LOW)
    GPIO.output(RIN2, GPIO.HIGH)
    GPIO.output(LIN1, GPIO.LOW)
    GPIO.output(LIN2, GPIO.HIGH)
    resetMotors()

  elif keyboard.is_pressed('right'):
    print("Turn Right")
    GPIO.output(RIN1, GPIO.LOW)
    GPIO.output(RIN2, GPIO.HIGH)
    GPIO.output(LIN1, GPIO.LOW)
    GPIO.output(LIN2, GPIO.LOW)
    resetMotors()

  elif keyboard.is_pressed('left'):
    print("Turn Left")
    GPIO.output(RIN1, GPIO.LOW)
    GPIO.output(RIN2, GPIO.LOW)
    GPIO.output(LIN1, GPIO.HIGH)
    GPIO.output(LIN2, GPIO.HIGH)

  elif keyboard.is_pressed('s'):
    print("Slow")
    p.ChangeDutyCycle(25)
    x = 'z'

  elif keyboard.is_pressed('d'):
    print("Medium")
    p.ChangeDutyCycle(50)
    x = 'z'

  elif keyboard.is_pressed('f'):
    print("Fast")
    p.ChangeDutyCycle(75)
    x = 'z'

  elif keyboard.is_pressed('e'):
    GPIO.cleanup()
    break
