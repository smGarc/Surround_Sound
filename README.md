# Surround Sound

__Stevens Institute of Technology 2025__

__Raspberry Pi Software Guide by Simon Garcia '25__

Surround Sound is a low-cost autonomous robot that utilizes a Raspberry Pi, a bluetooth speaker, a microphone, and mecanum wheels to measure the 3D sound field inside a room.

Innovation Expo: 5/9/2025

## File Overview

### [main.py](https://github.com/smGarc/Surround_Sound/blob/main/main.py)
This is the code that is executed after the Raspberry Pi starts up. It's the file that calls the other files when the time to call them arises.

### [motors.py](https://github.com/smGarc/Surround_Sound/blob/main/motors.py)
This is the code that controls the movement of the robot and is called only before an audio sample is taken to ensure the sound of the motors are not picked up by the microphone

### [audio.py](https://github.com/smGarc/Surround_Sound/blob/main/audio.py)
This is the code that controls audio playing, recording, saving, and analysis. It is only played after a button is pressed that prevents the robot from moving and initiates recording.

## Resources Necessary

### Hardware

- [Raspberry Pi Zero W](https://www.raspberrypi.com/products/raspberry-pi-zero-w/)
- [L298N DC Motor Driver](https://components101.com/modules/l293n-motor-driver-module) (x2)
- 12V DC Motors (x4)
- 12V Power Supply (12V Battery Pack used) (x2)
- Jumper Wires

### Python Libraries

- [RPi.GPIO](https://pypi.org/project/RPi.GPIO/)
- [PyAudio](https://people.csail.mit.edu/hubert/pyaudio/docs/)
- [datetime](https://docs.python.org/3/library/datetime.html)

### Reference Web Pages

- [Handy Raspberry Pi Pin Chart](https://pinout.xyz/pinout/pin3_gpio2/)
- [Raspberry Pi L298N Interface Tutorial | Control a DC Motor with L298N and Raspberry Pi](https://www.electronicshub.org/raspberry-pi-l298n-interface-tutorial-control-dc-motor-l298n-raspberry-pi/)
- [Creating a new folder with python file](https://stackoverflow.com/questions/1274405/how-to-create-new-folder)
- [Setting up a game controller for Raspberry Pi](https://pimylifeup.com/xbox-controllers-raspberry-pi/)
- [Using Mechanum wheels with game controller](https://gm0.org/en/latest/docs/software/tutorials/mecanum-drive.html#robot-centric-final-sample-code)
- [Mechanum Omnidirectional Robot with Raspberry Pi](https://youtu.be/_L4AiG7WWLs?t=546)

## Wiring Diagrams

Contributed by Samantha Gordon '25

## Wiring Images

### Motor Driver Connection (With one Motor)

![Wide view of the motor, motor driver, battery pack, and Raspberry Pi all connected](https://i.imgur.com/pcNu8qb.jpg)

![Connections on the Raspberry Pi](https://i.imgur.com/uqRkVxL.jpg)

![Connections on the Motor Driver](https://i.imgur.com/OXPgkaT.jpg)
