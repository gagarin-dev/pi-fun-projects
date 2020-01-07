# Bird feeder with motion detection, takes photos of birds.
# Based on https://github.com/RuiSantosdotme/RaspberryPiProject/blob/master/Code/Project_13/burglar_detector.py

# Note: to test your camera, run from the terminal:
# raspistill -o image.jpg

from gpiozero import Button, MotionSensor
from picamera import PiCamera
from datetime import datetime
from time import sleep
from signal import pause
import logging

# Set up 'logger'. DEBUG for debugging, INFO for informational messages.
logger = logging.getLogger()
#logger.setLevel(logging.DEBUG)
logger.setLevel(logging.INFO)

# Init Camera
camera = PiCamera() # https://picamera.readthedocs.io/en/release-1.13/recipes1.html#recipes1
camera.led = False # Turn the camera's LED off
camera.rotation = 180
camera.start_preview() # activate the camera

# Init PIR sensor
pir = MotionSensor(4) # at GPIO 4

# Init push-button
button = Button(2) # at GPIO 2

sleep(2) # warm-up camera and sensor


def stop_camera():
    '''stop the camera when the pushbutton is pressed'''
    camera.stop_preview()
    camera.close()
    #exit the program
    exit()


def take_photo():
    '''take photo when motion is detected'''
    timenow = datetime.now()
    filename = "foto-" + timenow.strftime("%Y-%m-%d-%H%M%S") + ".jpg"
    camera.capture(filename) # capture photo to a file
    logger.info(f'New photo in {filename}')
    sleep(10) # time-out 

## MAIN HANDLER
#assign a function that runs when the button is pressed
button.when_pressed = stop_camera
#assign a function that runs when motion is detected
pir.when_motion = take_photo

# wait for a signal from the button or sensor
pause()
