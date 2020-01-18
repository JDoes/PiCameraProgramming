from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.rotation = 180
camera.start_preview(alpha=150) #alpha=50 changes opacity. 0 to 256?
sleep(120) # how long the preview is active (seconds)
camera.stop_preview()
