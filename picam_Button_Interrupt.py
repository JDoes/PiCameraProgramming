import time
from time import sleep
import datetime
from picamera import PiCamera
from gpiozero import Button

button = Button(17)
camera = PiCamera()
camera.resolution = (1024,768)
camera.rotation = 180


camera.start_preview(alpha=175)

sleep(2)

directory = "/home/pi/Desktop/images/"

button.wait_for_press()
sleep(1)

while not button.is_pressed:
    date_string = time.strftime("%Y-%m-%d-%H:%M:%S")
    full_name = directory + date_string + "_PiCam_image.jpg"
    camera.capture(full_name)
    print(full_name)
    sleep(2)
                       
camera.stop_preview()
