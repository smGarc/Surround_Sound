# Surround Sound

Stevens Institute of Technology 2025

Raspberry Pi Software Guide by Simon Garcia '25

## File Overview

### [main.py](https://github.com/smGarc/Surround_Sound/blob/main/main.py)
This is the code that is executed after the Raspberry Pi starts up. It's the file that calls the other files when the time to call them arises.

### [motors.py](https://github.com/smGarc/Surround_Sound/blob/main/motors.py)
This is the code that controls the movement of the robot and is called only before an audio sample is taken to ensure the sound of the motors are not picked up by the microphone

### [audio.py](https://github.com/smGarc/Surround_Sound/blob/main/audio.py)
This is the code that controls audio playing, recording, saving, and analysis. It is only played after a button is pressed that prevents the robot from moving and initiates analysis.

## Resources Used

### Hardware

- [Raspberry Pi Zero W](https://www.raspberrypi.com/products/raspberry-pi-zero-w/)
- [L298N DC Motor Driver](https://components101.com/modules/l293n-motor-driver-module)
- 12V DC Motors
- 12V Power Supply (12V Battery Pack used)
- Jumper Wires

### Python Libraries

- [RPi.GPIO](https://pypi.org/project/RPi.GPIO/)
- [PyAudio](https://people.csail.mit.edu/hubert/pyaudio/docs/)
- [datetime](https://docs.python.org/3/library/datetime.html)

### Reference Web Pages

- [Handy Raspberry Pi Pin Chart](https://pinout.xyz/pinout/pin3_gpio2/)
- [Raspberry Pi L298N Interface Tutorial | Control a DC Motor with L298N and Raspberry Pi](https://www.electronicshub.org/raspberry-pi-l298n-interface-tutorial-control-dc-motor-l298n-raspberry-pi/)
- [Creating a new folder with python file](https://stackoverflow.com/questions/1274405/how-to-create-new-folder)

## Wiring Diagrams

Contributed by Samantha Gordon '25


## Wiring Images