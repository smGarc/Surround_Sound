import RPi.GPIO as GPIO
from time import sleep

IN1 = 24
IN2 = 23
EN = 25
TEMP1 = 1

GPIO.setmode(GPIO.BCM)
GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)
GPIO.setup(EN, GPIO.OUT)
GPIO.output(IN1, GPIO.LOW)
GPIO.output(IN2, GPIO.LOW)
p = GPIO.PWM(EN, 1000)
p.start(25)
print("\n")
print("Default speed and direction of motor is LOW and Forward...")
print("R-run, S-stop, F-forward, B-backwards, L-low, M-medium, H-high, E-exit")
print("\n")

while(1):
	x = input()
	if x == 'r':
		print("Run")
		if TEMP1 == 1:
			GPIO.output(IN1, GPIO.HIGH)
			GPIO.output(IN2, GPIO.LOW)
			print("Forward")
			x = 'z'
		else:
			GPIO.output(IN1, GPIO.LOW)
			GPIO.output(IN2, GPIO.HIGH)
			print("Backward")
			x = 'z'
	elif x == 's':
		print("Stop")
		GPIO.output(IN1, GPIO.LOW)
		GPIO.output(IN2, GPIO.LOW)
		x = 'z'
	elif x == 'f':
		print("Forward")
		GPIO.output(IN1, GPIO.HIGH)
		GPIO.output(IN2, GPIO.LOW)
		TEMP1 = 1
		x = 'z'
	elif x == 'b':
		print("Backwards")
		GPIO.output(IN1, GPIO.LOW)
		GPIO.output(IN2, GPIO.HIGH)
		TEMP1 = 0
		x = 'z'
	elif x == 'l':
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
