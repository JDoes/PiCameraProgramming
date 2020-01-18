import time
from time import sleep
import datetime
from picamera import PiCamera

camera = PiCamera()
camera.resolution = (1024,768)
camera.rotation = 180


camera.start_preview(alpha=175)

sleep(2)
date_string = time.strftime("%Y-%m-%d-%H:%M:%S")

directory = "/home/pi/Desktop/"

full_name = directory + date_string + "_PiCam_image.jpg"
                            
camera.capture(full_name)
sleep(2)
camera.capture(full_name)
                        
sleep(3)
camera.stop_preview()
