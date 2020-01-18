from picamera import PiCamera
from time import sleep
import time
import datetime
from gpiozero import Button

button = Button(17)
camera = PiCamera()

camera.rotation = 180
camera.start_preview(alpha=175)

button.wait_for_press()
camera.capture('/home/pi/Desktop/image_%Y-%m-%d-%H-%M-%S.jpg')

sleep(2)

camera.stop_preview()
